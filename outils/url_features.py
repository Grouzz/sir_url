"""Prototype : métriques d'URL et de typosquatting (analyse passive, aucune requête réseau).

Installation : pip install tldextract
Utilisation  : python url_features.py "https://exemple.com/login" ["<autre url>" ...]
"""
import ipaddress
import math
import re
import sys
from collections import Counter
from urllib.parse import urlsplit, unquote

import tldextract

# Extracteur hors ligne (liste des suffixes publics embarquée)
EXTRACT = tldextract.TLDExtract(suffix_list_urls=())

MARQUES = ["paypal", "google", "microsoft", "apple", "amazon", "facebook",
           "netflix", "laposte", "ameli", "impots", "creditagricole", "bnpparibas"]
MOTS_SENSIBLES = ["login", "signin", "verify", "account", "update", "secure",
                  "banking", "confirm", "password", "webscr", "support", "billing"]
RACCOURCISSEURS = {"bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "ow.ly", "cutt.ly", "rebrand.ly"}
TLD_A_RISQUE = {"xyz", "top", "click", "live", "icu", "buzz", "shop", "online", "site", "rest"}
# Caractères visuellement proches -> forme canonique
HOMOGLYPHES = str.maketrans({"0": "o", "1": "l", "3": "e", "5": "s", "@": "a", "$": "s",
                             "а": "a", "е": "e", "о": "o", "р": "p", "с": "c", "і": "i"})


def levenshtein(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def entropie(s):
    if not s:
        return 0.0
    n = len(s)
    return -sum(c / n * math.log2(c / n) for c in Counter(s).values())


def analyser(url):
    brut = url
    if "://" not in url:
        url = "http://" + url
    p = urlsplit(url)
    hote = (p.hostname or "").lower()
    ext = EXTRACT(hote)
    domaine = ext.top_domain_under_public_suffix or hote          # ex. paypal.com
    nom = ext.domain                                  # ex. paypal
    sous_domaines = [s for s in ext.subdomain.split(".") if s and s != "www"]

    try:
        ipaddress.ip_address(hote)
        est_ip = True
    except ValueError:
        est_ip = False

    f = {
        "longueur_url": len(brut),
        "longueur_hote": len(hote),
        "nb_sous_domaines": len(sous_domaines),
        "profondeur_chemin": len([x for x in p.path.split("/") if x]),
        "ip_au_lieu_du_nom": est_ip,
        "arobase": "@" in p.netloc or "@" in p.path,
        "double_slash_redirection": "//" in p.path,
        "port_explicite": p.port is not None,
        "https_dans_le_nom": "http" in hote,
        "tirets_dans_domaine": nom.count("-"),
        "chiffres_dans_domaine": 0 if est_ip else sum(ch.isdigit() for ch in nom),
        "punycode_idn": "xn--" in hote or any(ord(ch) > 127 for ch in hote),
        "encodage_pourcent": len(re.findall(r"%[0-9a-fA-F]{2}", brut)),
        "raccourcisseur": domaine in RACCOURCISSEURS,
        "tld": ext.suffix,
        "tld_a_risque": ext.suffix in TLD_A_RISQUE,
        "entropie_domaine": round(entropie(nom), 2),
        "mots_sensibles": [m for m in MOTS_SENSIBLES if m in unquote(brut).lower()],
    }

    # Typosquatting / usurpation de marque
    nom_affiche = nom
    if nom.startswith("xn--"):
        try:
            nom_affiche = nom.encode().decode("idna")   # ce que l'utilisateur voit dans le navigateur
        except UnicodeError:
            pass
    f["nom_affiche"] = nom_affiche if nom_affiche != nom else ""
    canon = nom_affiche.translate(HOMOGLYPHES).replace("-", "")
    identifiant = (p.username or "").lower()
    alertes = []
    for m in MARQUES:
        if nom == m:
            continue                                   # c'est la vraie marque (à confirmer avec le TLD officiel)
        d = levenshtein(canon, m)
        if canon == m:
            alertes.append(f"{m} : imitation par homoglyphes/tirets ({nom})")
        elif d <= 2 and len(m) >= 5:
            alertes.append(f"{m} : nom à {d} faute(s) de frappe ({nom})")
        elif m in canon:
            alertes.append(f"{m} : marque incluse dans un autre nom ({nom})")
        elif m in identifiant:
            alertes.append(f"{m} : marque placée avant un @, le vrai site est {domaine}")
        elif any(m in s for s in sous_domaines) or m in p.path.lower():
            alertes.append(f"{m} : marque placée hors du domaine réel ({domaine})")
    f["typosquatting"] = alertes
    f["domaine_reel"] = domaine
    return f


if __name__ == "__main__":
    for u in sys.argv[1:]:
        print(u)
        for k, v in analyser(u).items():
            if v not in (False, 0, [], ""):
                print(f"   {k}: {v}")
        print()

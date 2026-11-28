# Métriques URL et typosquatting

Toutes ces métriques se calculent à partir de la seule chaîne de l'URL : la page n'est jamais chargée, il n'y a donc aucun risque et aucun quota. Le signal le plus fort est l'usurpation de marque (typosquatting, homoglyphes, marque placée hors du domaine réel). Les autres métriques sont des indices faibles à pondérer.

## Outils

- **tldextract** (Python) isole le domaine réel grâce à la liste des suffixes publics (gère `.co.uk`, `.gouv.fr`…). C'est la base de toutes les autres métriques.
- **Distance de Levenshtein** : nombre de lettres à changer pour passer d'un nom à une marque (`paypa1` → `paypal` = 1).
- **Table d'homoglyphes + décodage punycode (idna)** : ramène `micros0ft` à `microsoft` et `xn--pypal-4ve` à `pаypal` (« а » cyrillique).
- **dnstwist** génère toutes les variantes d'une marque (1 369 pour paypal.com, dont 1 187 par homoglyphes). Il sert à surveiller une marque, pas à analyser une URL reçue : pour notre outil, il peut seulement fournir des cas de test.
- Prototype : `outils/url_features.py` (`pip install tldextract`, puis `python url_features.py "<url>"`).

## Limites

- Aucune limite de requêtes : tout est calculé localement.
- Le typosquatting ne détecte que les marques de notre liste : il faut décider laquelle utiliser (marques les plus visées en France ? top Tranco ?).
- La longueur, les tirets ou le TLD signalent aussi des sites légitimes : risque de faux positifs s'ils pèsent trop dans le score.

## Tests (27/11/2026, URL d'exemple inventées, jamais chargées)

| URL | Détecté |
|---|---|
| `https://www.paypal.com/signin` (légitime) | Rien de suspect, à part le mot « signin », normal sur le vrai site |
| `http://paypa1-secure-login.com/webscr?cmd=login` | Marque PayPal dans un autre nom, 2 tirets, 1 chiffre, 3 mots sensibles |
| `https://paypal.com.account-verify.xyz/login` | Domaine réel `account-verify.xyz`, marque en sous-domaine, TLD à risque |
| `https://xn--pypal-4ve.com/` | Punycode affiché « pаypal » avec un « а » cyrillique : homoglyphe |
| `https://micros0ft-support.live/update` | « 0 » à la place du « o », TLD à risque, mots sensibles |
| `http://www.google.com@evil.example.top/login` | Marque placée avant un @, le vrai site est `example.top` |
| `http://192.168.12.4/ameli/remboursement/index.php` | IP à la place du nom, marque Ameli dans le chemin |
| `https://bit.ly/3xYz9Ab` | Raccourcisseur : destination cachée |

## Article PhishNet (arXiv 2407.04732)

- Métriques d'URL utilisées : IP dans l'URL, « @ », longueur, profondeur (nombre de « / »), redirection « // », « http » dans le domaine, raccourcisseur, tiret dans le domaine. Elles sont toutes reprises ci-dessus.
- Données : environ 5 000 URL de phishing (PhishTank) et 5 000 URL légitimes (collection UNB de 2016). Modèle retenu : XGBoost.
- À ne pas reprendre tel quel : aucun chiffre de performance n'est donné, le nombre de métriques est incohérent (18, 16 puis 13), certains encodages contredisent leur justification, et le trafic web repose sur Alexa, arrêté en 2022 (alternative gratuite : Tranco).

## Observations

- Le domaine réel doit être extrait en premier : c'est lui qu'il faut montrer à l'utilisateur, et c'est lui que la #5 doit interroger en WHOIS/RDAP.
- Combinaison forte avec la #5 : un domaine créé il y a quelques jours qui imite une marque est un signal d'alerte majeur.
- Une URL raccourcie ne peut être jugée qu'après avoir suivi la redirection, ce qui doit se faire dans la sandbox.

## Le tableau des metriques

| Métrique | Module | Outil | Gratuit / limite | Ce que ça révèle | Explication pour l'utilisateur |
|---|---|---|---|---|---|
| Date de création du domaine | Domaine/DNS |RDAP (rdap.org), whois | Gratuit, 10 requêtes / 10 s via rdap.org, whois non standardisé|L'âge du domaine |Ce site a été créé il y a 19 jours. Un domaine récent qui imite une marque est un signal d'alerte. |
| Enregistrements DNS | Domaine/DNS |dig (A, MX, NS) |Gratuit, pas de quota annoncé |IP, hébergeur, messagerie, gestionnaire du domaine | Si la réponse est vide le domaine est suspendu |
| Domaine réel (domaine enregistré) | URL/Typosquatting | tldextract (liste des suffixes publics) | Gratuit, local, sans quota | Le vrai propriétaire du site, quel que soit le reste de l'URL | Le site réel est account-verify.xyz, pas paypal.com. |
| Adresse IP à la place du nom | URL/Typosquatting | ipaddress (Python) | Gratuit, local, sans quota | Pas de nom de domaine, donc pas de propriétaire identifiable | Un site d'entreprise utilise un nom, pas une suite de chiffres. |
| Symbole @ dans l'URL | URL/Typosquatting | Analyse de l'URL | Gratuit, local, sans quota | Tout ce qui précède @ est ignoré par le navigateur | google.com@… mène en réalité vers le site écrit après le @. |
| Marque hors du domaine réel | URL/Typosquatting | Recherche de la marque dans les sous-domaines, le chemin ou avant un @ | Gratuit, local ; liste de marques à définir | Le nom d'une marque est affiché mais le site appartient à quelqu'un d'autre | Le nom PayPal apparaît, mais ce site n'appartient pas à PayPal. |
| Typosquatting (fautes de frappe) | URL/Typosquatting | Distance de Levenshtein contre une liste de marques | Gratuit, local ; liste de marques à définir | Nom à 1 ou 2 lettres d'une marque (paypl, gooogle) | Ce nom ressemble à PayPal à une lettre près. |
| Homoglyphes et punycode | URL/Typosquatting | Décodage idna + table de caractères proches | Gratuit, local, sans quota | Lettres cyrilliques ou chiffres imitant des lettres (pаypal, micros0ft) | Ce « a » est une lettre cyrillique : le site n'est pas PayPal. |
| Mots sensibles (login, verify, account…) | URL/Typosquatting | Liste de mots-clés | Gratuit, local, sans quota | Page conçue pour faire saisir des identifiants | L'adresse cherche à vous faire saisir vos identifiants. |
| Raccourcisseur d'URL | URL/Typosquatting | Liste (bit.ly, tinyurl…) | Gratuit, local, sans quota | La destination réelle est cachée | Destination inconnue : à suivre dans la sandbox avant de conclure. |
| Tirets, chiffres, « http » dans le nom | URL/Typosquatting | Analyse de l'URL | Gratuit, local, sans quota | Noms fabriqués (paypa1-secure-login, https-paypal) | Indice faible : le nom mélange une marque et des mots rassurants. |
| Extension (TLD) à risque | URL/Typosquatting | Liste de TLD (.xyz, .top, .live…) | Gratuit, local ; liste à justifier | Extensions bon marché très utilisées pour le phishing | Indice faible : beaucoup de sites légitimes les utilisent aussi. |
| Longueur, sous-domaines, profondeur, encodage % | URL/Typosquatting | Analyse de l'URL | Gratuit, local, sans quota | URL allongée ou obfusquée pour masquer le vrai domaine | Indice faible : de nombreux sites légitimes ont des URL longues. |
| Certificat HTTPS | Certificat/Contenu | | | | |
| Autorité de certification | Certificat/Contenu | | | | |
| Page de login clonée | Certificat/Contenu | | | | |
| Présence en liste noire | Réputation | | | | |
| Verdict VirusTotal | Réputation | | | | |

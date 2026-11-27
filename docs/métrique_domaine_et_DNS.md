# Métriques domaine et DNS

## Outils

- **RDAP** et **whois** donnent les mêmes informations d'enregistrement (date de création, registrar, statuts). RDAP renvoie du JSON, donc plus simple à exploiter dans l'outil final. Whois affiche du texte libre dans le terminal.
- **dig** interroge le DNS (IP, messagerie, serveurs de noms).

## Limites

- RDAP : 10 requêtes par 10 s via rdap.org (erreur 429 au-delà), 1 requête par seconde conseillée.
- whois : limites non standardisées, variables selon le serveur.
- dig : pas de quota annoncé, requêtes en nombre raisonnable.

## Tests (27/11/2026, analyses passives : le site n'est jamais contacté)

| Domaine | Création | Âge | Registrar | DNS (A, MX, NS) |
|---|---|---|---|---|
| github.com (légitime) | 09/10/2007 | plus de 19 ans | MarkMonitor | A et MX renseignés, 8 serveurs de noms (NS1 et Route 53) |
| bak-center (flux OpenPhish) | 08/11/2026 | 19 jours | PDR Ltd (PublicDomainRegistry) | aucune réponse : domaine suspendu (clientHold, NS suspended-domain.com) |

## Observations

- Le domaine de phishing est très récent par rapport au domaine légitime. C'est un signal d'alerte, pas une preuve.
- Un domaine suspendu ne répond plus au DNS : l'outil doit gérer l'absence d'enregistrements.
- Le whois renvoie trois blocs (IANA, registre, registrar). La première date (`created: 1985-01-01`) est celle de l'extension .com, pas celle du domaine : il faut lire la ligne `Creation Date` du bloc du registre. RDAP évite ce piège (test RDAP à faire).

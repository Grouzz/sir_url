## Tableau comparatif du recensement des services de réputation gratuits

| Service | Accès | Limite / licence | Données renvoyées | Mode conseillé |
|---|---|---|---|---|
| URLhaus | Clé gratuite (Auth-Key) | Gratuit, exports toutes les 5 minutes | URL malveillantes (malware), étiquettes, statut, hébergeur | Liste locale |
| OpenPhish | Flux public | Non commercial, mise à jour toutes les 12 h, sous-ensemble | URL de phishing | Liste locale |
| PhishTank | Sans clé (inscription fermée) | Débit très limité, erreur 509 en cas de dépassement | Statut phishing, vérification communautaire | Secours |
| Google Safe Browsing | Clé Google Cloud | Gratuit, non commercial, quota par défaut | Menace probable (phishing, malware, logiciel indésirable) | API en complément, mode local si possible |
| VirusTotal | Clé gratuite | Environ 4 requêtes par minute | Verdict de nombreux moteurs, à interpréter | Cas ambigus uniquement |

Tests de réputation (26/11/2026). Le flux gratuit d'OpenPhish se télécharge sans clé (fichier texte, une URL de phishing par ligne). Une URL de ce flux a ensuite été soumise à l'API d'URLhaus (clé gratuite), qui a répondu no_results. Une URL de phishing connue d'une source peut donc être absente d'une autre : il faut croiser plusieurs sources. L'API PhishTank, testée sans clé, a renvoyé une redirection (301) : test à refaire en HTTPS.

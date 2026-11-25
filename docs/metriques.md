# Tableau des métriques (tâche #10)

Ce tableau est la base du futur score : une ligne = une métrique que l'outil pourra calculer à partir d'une URL.
Chacun remplit **les lignes de son module**. Les cases vides = à faire.

## Comment remplir (2 minutes)

1. Trouvez les lignes de votre module (colonne **Module**).
2. Remplissez les 4 colonnes vides, **une phrase courte par case**, sans retour à la ligne.
3. Pour une nouvelle métrique : copiez une ligne complète et ajoutez-la à la fin du tableau.
4. Si une case demande plus de place, mettez le détail dans l'issue GitHub du module et écrivez « voir #N » dans la case.
5. Ne mettez **jamais** une vraie URL malveillante : écrivez-la neutralisée (`hxxp://exemple[.]com`).
6. Pas de `|` dans le texte d'une case (ça casse le tableau).

### Ce qu'on attend dans chaque colonne

| Colonne | À écrire |
|---|---|
| Outil | Nom de l'outil ou de l'API qui donne l'information (ex. RDAP, `dig`, crt.sh, VirusTotal) |
| Gratuit / limite | « Gratuit », ou la limite (ex. « 4 requêtes/min »), ou « Payant » |
| Ce que ça révèle | Pourquoi cette métrique aide à repérer un phishing |
| Explication pour l'utilisateur | La phrase simple qu'on affichera dans le rapport, sans jargon |

### Exemple de ligne remplie (à ne pas recopier telle quelle)

| Métrique | Module | Outil | Gratuit / limite | Ce que ça révèle | Explication pour l'utilisateur |
|---|---|---|---|---|---|
| Date de création du domaine | Domaine/DNS | RDAP | Gratuit | Un domaine très récent est typique d'un site de phishing jetable | Ce site existe depuis quelques jours seulement, alors que les sites sérieux sont en général plus anciens. |

## Modules

| Module | Issues | Lignes concernées |
|---|---|---|
| Domaine/DNS | #5 | Date de création, enregistrements DNS |
| URL/Typosquatting | #6 | Structure de l'URL, typosquatting |
| Certificat/Contenu | #7 | Certificat HTTPS, autorité de certification, page de login clonée |
| Réputation | #8, #9 | Liste noire, VirusTotal |

## Le tableau

| Métrique | Module | Outil | Gratuit / limite | Ce que ça révèle | Explication pour l'utilisateur |
|---|---|---|---|---|---|
| Date de création du domaine | Domaine/DNS | | | | |
| Enregistrements DNS | Domaine/DNS | | | | |
| Structure de l'URL | URL/Typosquatting | | | | |
| Typosquatting | URL/Typosquatting | | | | |
| Certificat HTTPS | Certificat/Contenu | | | | |
| Autorité de certification | Certificat/Contenu | | | | |
| Page de login clonée | Certificat/Contenu | | | | |
| Présence en liste noire | Réputation | | | | |
| Verdict VirusTotal | Réputation | | | | |

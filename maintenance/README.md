# Maintenir cette application

Les neuf fonctions de validation communes se trouvent dans validators.js. La configuration de version et l’inscription commune pour l’accès hors connexion se trouvent dans app-common.js. Les contrôles d’identité des sauvegardes et les clés de stockage restent propres à chaque plan.

Les modules partagés gèrent le thème, l’accessibilité, les indications éditoriales, les téléchargements et les mises à jour. Corriger ces modules corrige les 24 variantes ; le moteur historique de lecture n’a pas été entièrement extrait.

Pour préparer une nouvelle version :

1. Archiver la dernière livraison complète.
2. Modifier les fichiers nécessaires ; conserver les clés de stockage et l’identité des plans.
3. Mettre à jour version.json, bibleAppRelease dans app-common.js, RELEASE et les deux numéros de cache dans sw.js.
4. Exécuter build_manifest.py puis validate_release.py, avec Python 3.
5. Effectuer les essais de sauvegarde/import, clavier, audio et accès hors connexion décrits dans la page de tests téléphone. Contrôler les notes et les coches avant et après mise à jour.
6. Publier TOUS les fichiers dans un même commit GitHub, y compris release-manifest.json et les nouveaux modules. Une publication partielle doit être refusée par le contrôle de cohérence.

Le service worker télécharge une version candidate et vérifie les empreintes SHA-256 avant activation. Si un fichier manque, est altéré ou appartient à une autre livraison, la version candidate n’est pas activée. Les ressources de l’application déjà installée sont servies depuis leur cache cohérent. Les nouveaux parcours sont vérifiés avant téléchargement.

Les empreintes détectent une publication incomplète ; elles ne sont pas une signature d’identité de l’éditeur. Les mots de passe et le suivi ne figurent pas dans le manifeste. Les caches de l’application et le stockage du suivi restent distincts.

La page des tests téléphone fournit un rapport manuel local. Aucun audit tiers de conformité WCAG ou de sécurité n’est revendiqué.

Le module daily-companion.js complète les repères écrits, le rythme et le bilan hebdomadaire existants. Son champ facultatif dailyCompanion est inclus dans la sauvegarde de format 11 ; les anciens fichiers sans ce champ restent acceptés. application-help.js fournit les rapports locaux, l’historique et le bouton de contrôle après export. Aucun rapport n’est transmis automatiquement.


Version 31 : 27 variantes (neuf plans), book-guides.js pour les contenus synthétiques, study.js / study.css pour leur affichage, personal-home.js et review-kit.js. Les 51 groupes protégés du parcours continuité et les catalogues initiaux demandent une relecture extérieure, non réalisée. Ne pas exécuter les anciens scripts de construction incrémentaux sur la livraison courante.


Version 32 : plan-guide.js et choisir-parcours.html ; notebook.js utilise notes, noteTopics et favoris déjà exportés, aucun nouveau champ de sauvegarde ; version-notes.js et comparer-versions.html proposent quatre comparaisons documentées, avec correspondances explicites par version. Garder le carnet local, les anciennes clés de suivi et les tableaux des journées inchangés.


## Version 2026.10.04.33
Dix plans, trente variantes, 10 950 journées. Le nouveau parcours israel-nations dispose de clés de suivi indépendantes, de douze étapes et d’une méthode. Le validateur contrôle également ses 51 regroupements protégés et ses chapitres entiers. Toute modification de ses données après publication doit préserver le sens des journées et du suivi.


## Version 2026.10.06.34
Onzième plan : Connexions, 24 séances sélectionnées, hors calendrier annuel. Le validateur annuel exclut ses pages et appelle validate_connections.py pour leur schéma distinct. Ne pas les convertir en 365 journées. Les sauvegardes de ce plan ont un format et des clés propres ; leur édition est connexions-24-v1. Toute réorganisation ultérieure doit prévoir la migration du suivi.


## Version 2026.10.06.35
Douzième parcours reseau : 50 dossiers de quatre étapes, 200 séances et dix modules, dans trois versions. validate_network.py vérifie sa structure et les repères, sans certifier les extensions thématiques. Le moteur connexions.js conserve les formats et clés du parcours de 24 séances et utilise une édition, des formats, une clé de suivi et une authentification de sauvegarde distincts pour reseau-200-v1. Ne jamais modifier l’ordre des séances publiées sans migration du suivi.

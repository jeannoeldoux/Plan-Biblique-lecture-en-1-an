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

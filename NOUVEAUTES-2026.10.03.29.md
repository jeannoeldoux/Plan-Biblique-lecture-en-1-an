# Version 2026.10.03.29 — axes 5, 6 et 7

## Qualité éditoriale

Un panneau « Lire ces passages dans leur contexte » accompagne les journées et ouvre les chapitres environnants, dans la version choisie. Les rapprochements du premier parcours sont présentés comme des pistes d’étude. Les placements discutés du parcours chronologique sont précisés. Le parcours familial indique comment adapter une question et passer une question qui ne correspond pas à l’extrait.

La méthode des huit parcours est expliquée dans qualite-des-plans.html. Les 33 formulations de rapprochement et les 70 formulations distinctes de questions familiales ont été examinées. Les références et les journées des 24 parcours sont conservées ; les coupures ne sont pas réécrites en unités littéraires. Cette révision ne constitue pas une validation théologique indépendante de chaque rapprochement.

Le contrôle éditorial porte sur les références ÉCRITES : 8 760 journées, chapitres et numéros de versets valides dans chacune des trois versions, couverture des 66 livres, relectures et pauses distinguées. Il ne déduit pas la couverture du seul chapitre audio, qui peut être plus long que l’extrait.

## Accessibilité

- Accès directs au contenu quotidien et au lecteur audio.
- Contrastes renforcés en mode clair, notamment les libellés verts et les commandes bleues des passages complémentaires.
- Focus clavier visible, commandes tactiles agrandies et prise en compte de la réduction des animations.
- Annonce du changement de jour pour les lecteurs d’écran.
- Noms des fenêtres et retour du focus au bouton d’ouverture après fermeture.
- Guide d’utilisation et tests VoiceOver/Contrôle vocal ajoutés aux essais iPhone.

Les tests physiques avec VoiceOver et Contrôle vocal restent à effectuer. La livraison ne revendique pas une certification complète WCAG.

## Maintenance et cohérence des mises à jour

Neuf fonctions identiques de validation des données sont regroupées dans validators.js. La configuration de version et la préparation commune de l’accès hors connexion sont regroupées dans app-common.js. Les contrôles d’identité et les clés de stockage restent propres à chaque plan.

Une nouvelle version est signalée automatiquement lorsqu’elle est disponible. L’installation reste une action de l’utilisateur.

Un manifeste décrit les empreintes SHA-256 des fichiers de la livraison. Le téléchargement de tous les fichiers nécessaires et leur vérification précèdent l’activation. Une publication incomplète, un fichier manquant ou un contenu altéré est refusé. Les ressources déjà installées proviennent de leur cache cohérent. Les parcours ajoutés sont également vérifiés.

Le dossier maintenance fournit les instructions et deux outils reproductibles : création du manifeste et contrôle structurel des parcours. Les empreintes détectent une incohérence de livraison ; elles ne constituent pas une signature de l’éditeur.

## Résultats des vérifications

- 24 variantes, 365 jours chacune, références écrites et couverture complète contrôlées.
- 72 contrôles page/thème sur les 36 pages : contrastes calculés, noms des commandes visibles et absence d’identifiants dupliqués.
- 216 contrôles de largeur, plus texte agrandi sur les 24 pages de plans.
- Navigation clavier, accès direct à la coche du jour, annonce du jour, fermeture par Échap et restauration du focus sur les 24 variantes.
- Zoom simulé à 200 % et espacement du texte sur les 24 variantes, sans débordement horizontal.
- Liens de contexte ouvrant le chapitre entier et présence d’un seul lecteur audio.
- Export chiffré, import dans un autre contexte de navigateur, sauvegarde classique et refus du mot de passe incorrect.
- Migration réelle de l’archive 2026.10.03.28 : stockage local identique, parcours téléchargé conservé et notes/coches disponibles hors connexion.
- Mise à jour future simulée : publication incomplète ou altérée refusée, cache actif préservé ; version complète acceptée, suivi et téléchargements choisis conservés.

La publication sur GitHub reste à effectuer. Les essais physiques sur iPhone ne sont pas remplacés par ces simulations.

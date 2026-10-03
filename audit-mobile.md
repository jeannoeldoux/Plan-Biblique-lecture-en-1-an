# Audit de l’affichage mobile — 3 octobre 2026

Version testée : 2026.10.03.12.

Les tests ont été réalisés dans Microsoft Edge sur ordinateur, avec des tailles d’écran mobiles. Ils ne remplacent pas un essai sur un iPhone réel ni une vérification dans Safari.

## Résultats

- Écrans de 320, 390, 430 et 768 pixels : aucun débordement horizontal détecté, y compris avec le texte très grand et le mode sombre.
- Un jour affiché et un lecteur audio unique.
- Version imprimable créée uniquement à la demande.
- Coupure du réseau audio simulée : bouton « Réessayer » disponible.
- Après une première visite en ligne : rechargement du plan hors connexion, modification des notes et validation d’un jour conservées après rechargement.
- Recherche dans 10 archives de 365 notes : résultats affichés par groupes de 20.
- Aucun défaut JavaScript détecté pendant cet audit.
- 40 changements de jour avec ce jeu de données : médiane 3.3 ms, maximum 5.1 ms sur cet ordinateur. Ces valeurs ne prédisent pas les performances d’un téléphone.
- Fichier HTML : environ 563 Ko. Le téléchargement des MP3 dépend du réseau et du serveur audio.

## À confirmer sur votre téléphone

1. Publier index.html et sw.js dans le même dossier GitHub Pages, puis ouvrir le site avec Internet.
2. Changer plusieurs fois de jour et essayer une recherche.
3. Écouter un chapitre, le mettre en pause, puis utiliser « Reprendre mon écoute ».
4. Essayer le mode concentration, l’enchaînement, la vitesse et le minuteur, notamment écran verrouillé.
5. Revenir au site sans réseau et vérifier que le plan, les notes et les coches restent accessibles. L’audio demande Internet.
6. Exporter une sauvegarde, vérifier le fichier téléchargé, puis tester l’aperçu avant import.

Le document lisible des notes est un fichier HTML indépendant. Il permet de lire et d’imprimer les réflexions ; la sauvegarde JSON est nécessaire pour réimporter les données dans le plan.

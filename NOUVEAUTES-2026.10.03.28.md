# Version 2026.10.03.28

Les huit plans, les trois versions bibliques, leurs références et leurs suivis distincts sont conservés.

1. **Vérifications sur téléphone** : une page de tests guidés pour votre iPhone couvre l’affichage, les notes, l’audio avec écran verrouillé, les interruptions, le minuteur, le calendrier, les sauvegardes et les mises à jour. Chaque résultat est initialement « Non testé » et reste local. Le rapport peut être téléchargé. Les essais physiques sur iPhone restent à réaliser.
2. **Sauvegardes protégées** : « Sauvegarder » crée un fichier JSON chiffré par mot de passe. L’import et le contrôle de sauvegarde acceptent les fichiers protégés et les anciens fichiers classiques. Aucun mot de passe n’est enregistré ou envoyé. Un mot de passe perdu ne peut pas être réinitialisé. Le chiffrement protège le fichier exporté, pas le stockage du navigateur ; les autres exports et la copie automatique avant import restent sans mot de passe.
3. **Écran quotidien simplifié** : le jour, la lecture, l’audio, la validation et les notes restent accessibles. Calendrier, recherches, archives et autres options sont regroupés dans « Outils et réglages ». « Afficher tous les outils » retrouve la disposition complète ; ce choix est mémorisé.
4. **Téléchargements hors connexion au choix** : le socle de l’application se prépare sans charger les 24 parcours. Un parcours ouvert est téléchargé ; vous pouvez en ajouter ou retirer dans « Mes parcours hors connexion ». Les mises à jour conservent les téléchargements choisis. Retirer un téléchargement n’efface ni coches ni notes. La recherche globale se conserve après sa première visite. Audio et textes bibliques externes nécessitent Internet.

## Vérifications sur ordinateur

- Chiffrement et déchiffrement d’une sauvegarde complète ; sel et vecteur différents pour chaque export. Mot de passe incorrect et fichier altéré refusés.
- Export réel et import entre deux contextes indépendants de navigateur ; notes, coches et date de départ conservées.
- Anciennes sauvegardes compatibles ; annulation et mot de passe incorrect sans modification du suivi.
- Contrôle de fichier protégé sans importation ; mots de passe effacés des champs après fermeture et absents du stockage.
- Cache initial sans les 24 plans ni la recherche volumineuse ; ajout, ouverture hors connexion et retrait de parcours.
- Mise à jour réussie ou échouée : toutes les données du stockage local conservées ; seuls les parcours téléchargés sont repris.
- 34 pages, 204 contrôles de largeur et 24 contrôles avec texte agrandi.
- Navigation audio : 264 contrôles de disposition sur les 24 parcours, y compris le mode concentration ; toujours un seul lecteur.
- Aucun problème JavaScript relevé durant ces vérifications.

Ces simulations ne valident pas l’audio sur un véritable iPhone verrouillé, les alertes de son calendrier ou ses choix de suspension des pages. La page tests-telephone.html permet de consigner ces essais après publication.

## Protection du fichier

Web Crypto : AES-GCM 256 bits, dérivation PBKDF2-HMAC-SHA-256 à 600 000 itérations, sel aléatoire de 16 octets et vecteur aléatoire de 12 octets par export. L’enveloppe est vérifiée avant déchiffrement. Cette fonction n’a pas fait l’objet d’un audit cryptographique indépendant.

# Application avec choix du plan

Décompressez l’archive. Copiez TOUS les fichiers de ce dossier à la racine du dépôt GitHub `Plan-Biblique-lecture-en-1-an`, en remplaçant index.html, sw.js, le manifeste et les icônes existants. Le dossier n’est pas à placer dans un sous-dossier : son contenu doit rejoindre la racine du site actuel.

L’adresse actuelle reste l’entrée de l’application. À la première ouverture, choisissez le plan. Aux ouvertures suivantes, votre dernier choix s’ouvre automatiquement. Le bouton Changer de plan affiche toujours les deux choix. Les anciens liens #jour-N ouvrent le plan précédent.

Le plan précédent utilise ses anciennes clés de stockage : son suivi sur la même adresse et dans le même navigateur est conservé. Le plan par genres conserve également ses clés distinctes. Un fichier local et le site GitHub n’ont pas le même stockage : utilisez les sauvegardes de chaque plan pour transférer le suivi.

La même application installée ouvre l’accueil et retrouve le choix mémorisé. Une première visite en HTTPS prépare les quatre plans hors connexion. L’audio et les pages bibliques externes nécessitent Internet.

Si vous avez déjà publié le plan par genres dans un sous-dossier séparé, exportez son suivi depuis cette ancienne adresse, puis importez-le dans le plan par genres de la nouvelle application. Un ancien service worker propre au sous-dossier n’est pas utilisé par ces nouvelles pages à la racine.

Cette livraison prépare les fichiers. La publication sur le dépôt GitHub reste à effectuer. L’ancienne archive conservée et les plans sources n’ont pas été modifiés.

Troisième plan : Histoire du salut. Ses notes, coches, date de départ, sauvegardes et archives sont indépendantes. Consulter methode-salut.html pour les limites et les 12 étapes. Publier aussi plan-salut.html, methode-salut.html et le nouveau sw.js.

Quatrième plan : Semaines thématiques. Publier plan-semaines.html, methode-semaines.html et le nouveau sw.js avec tous les autres fichiers. Étude hebdomadaire et lecture suivie sont distinguées dans la méthode.

## Deux versions
Publiez aussi les quatre pages plan-*-lsg.html, versions-bible.html et le nouveau sw.js. Le choix de version s’applique aux quatre plans et est mémorisé. Chaque plan/version a un suivi distinct ; les clés et les données S21 sont conservées. Voir versions-bible.html pour les ajustements, la numérotation des Psaumes et le plan classique avec ses thèmes et extraits. Tous les fichiers de cette livraison doivent rejoindre la racine du dépôt.

Mises à jour : publier aussi version.json et updates.js. Pour chaque nouvelle livraison, changer le numéro dans version.json et la constante CURRENT de updates.js, ainsi que le nom CACHE de sw.js lorsque les fichiers évoluent. Publier les fichiers ensemble. Le bouton vérifie la version publiée puis télécharge les fichiers et recharge la page. Le suivi reste dans le stockage du navigateur : conserver la même adresse GitHub Pages et les noms des clés de suivi. Les changements de structure des données devront conserver ou migrer les données existantes. La consultation locale (file://) explique que cette fonction sera disponible sur GitHub Pages.


Version 2026.10.03.20 : navigation mobile et Media Session, plus aide au transfert manuel sur chaque plan. Le suivi reste local ; le transfert export/import ne crée pas de compte ni de serveur de synchronisation. Ne pas confondre absence de serveur de suivi et absence de données techniques chez les fournisseurs : hébergement, audio et liens externes impliquent des requêtes réseau. Les fichiers de sauvegarde contiennent les notes en clair. Pour les transférer sans fournisseur tiers, utiliser un câble et conserver les fichiers en lieu sûr. Audio écran verrouillé : démarrer un chapitre puis tester sur l'appareil. Les commandes disponibles et l'enchaînement en arrière-plan dépendent du navigateur et du système. Un minuteur JavaScript peut être retardé en arrière-plan.


Troisième version : publier tous les fichiers, notamment les quatre pages plan-*-pdv.html, recherche.html, index.html, sw.js, mobile-audio.js, updates.js et version.json. Les suivis S21/LSG et leurs clés sont conservés. La PDV possède ses propres suivis et sauvegardes.

Version 2026.10.03.22 : publier aussi reminders.js, les douze pages des plans, theme.css, sw.js, updates.js et version.json. Dans Rappels calendrier : jours de semaine activables et horaires distincts, exceptions par date via un affichage mensuel. Les coches de rappel n'affectent pas les lectures validées. Les réglages sont inclus dans la sauvegarde ; leur import est facultatif et remplace le planning de rappels seulement si la case correspondante est cochée. Les sauvegardes antérieures restent acceptées. Une modification ne met pas automatiquement à jour les événements déjà importés dans le calendrier du téléphone ; réexporter et gérer les anciens événements dans un calendrier séparé pour éviter les doublons.


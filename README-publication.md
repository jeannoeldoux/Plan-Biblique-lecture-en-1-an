# Application biblique — version 2026.10.06.34

Dix parcours en un an, un parcours d’étude de 24 séances à rythme libre, et trois versions : Segond 21, Louis Segond 1910 avec Trésor Sonore et Parole de Vie 2017.

## Publier sur GitHub Pages

1. Télécharger et extraire application-biblique-version-2026.10.06.34.zip.
2. Remplacer les fichiers dans le même dépôt et au même emplacement, en une seule modification.
3. Publier tous les fichiers, y compris les nouveaux modules, sw.js, version.json et release-manifest.json. Ne pas publier seulement index.html.
4. Utiliser « Vérifier les mises à jour », puis appliquer la nouvelle version.

Les parcours téléchargés, le suivi et l’accompagnement fonctionnent hors connexion. Les textes bibliques externes et l’audio nécessitent Internet.

## Conservation du suivi

Les trente variantes des dix plans annuels, avec leurs lectures et commentaires, sont identiques à la version 33. Le onzième parcours utilise ses propres séances, clés de suivi et sauvegardes. La migration réelle de la version 33 à 34 a été testée : toutes les données locales sont conservées, avec notes et coches disponibles après un rechargement hors connexion.

Le suivi appartient au navigateur et à son adresse d’origine. Changer de domaine, vider les données du site ou changer de navigateur ou d’appareil peut rendre le suivi absent. Exporter et vérifier une sauvegarde avant ces changements. Une sauvegarde protégée nécessite son mot de passe.

## Nouveautés et limites

Voir NOUVEAUTES-2026.10.06.34.md et PARCOURS-CONNEXIONS-24-SEANCES.md. Pour les révisions théologiques précédentes : REVISION-COMMENTAIRES-2026.10.04.33.md. Le neuvième parcours garde des chapitres entiers et 51 regroupements, avec des journées de longueur variable. Ce n’est pas une analyse exhaustive des unités littéraires.

Catalogue initial : 66 introductions synthétiques, 51 jeux de questions ciblées et six rapprochements documentés. Les autres rapprochements restent des comparaisons proposées. Aucun texte biblique complet ni fichier MP3 n’a été copié dans la livraison.

Supports de relecture : relecture.html et SUPPORTS-RELECTURE.md. Aucun avis extérieur ni essai physique iPhone/VoiceOver n’a été réalisé. Aucun déploiement GitHub n’a été effectué dans cette livraison.

## Maintenance

Après modification, exécuter maintenance/build_manifest.py puis maintenance/validate_release.py. Pour une nouvelle publication, augmenter ensemble les versions de version.json, app-common.js et sw.js ainsi que les noms de caches. Ne pas modifier une version déjà publiée sans créer une nouvelle version.


Le dixième parcours possède trois nouvelles pages et sa propre méthode. Ses clés de suivi sont indépendantes des neuf anciens parcours. Voir controle-israel-nations.json pour les douze étapes et les contrôles de couverture.


Le parcours Connexions possède un suivi distinct et des sauvegardes spécifiques, incompatibles avec les sauvegardes annuelles. Pour publier, remplacer tous les fichiers de cette version. Les textes et l’audio externes restent en ligne.

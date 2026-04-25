# Projet de fin de semestre — Consignes pour les étudiants

Bonjour — voici les consignes officielles pour le projet de fin de semestre (Groupes A–D). Ce document s'adresse aux étudiants : il contient les attentes techniques, la checklist, le modèle de README, et les exigences de présentation.

## Objectif
Travaillez en groupes de 3 à 5 étudiants pour produire un projet complet, déployé et présentable. Visez des standards professionnels : code lisible, historique Git clair (commits/branches), tests et déploiement public.

## Contraintes techniques obligatoires
- Langage principal : le cœur logique de l'application doit être développé en **C**.
- Architecture : séparation Backend / Frontend.
- Intégration IA (obligatoire) : chaque projet doit intégrer au moins une API d'IA (chatbot, reconnaissance vocale, analyse d'image, traduction, etc.). Plusieurs fonctionnalités IA sont encouragées.
- Base de données : utilisez exclusivement des bases cloud — **Supabase** ou **MongoDB**. **SQLite est interdit** pour la version finale.
- Déploiement : le produit final doit être déployé et accessible publiquement (web, mobile ou desktop).

## Étapes à suivre (pour les étudiants)
1. Constituez votre groupe (3–5 étudiants).
2. Créez un dépôt sous l'organisation `chafik-boulealam-lab` en respectant la convention : `project-<groupe>-<sujet>`.
3. Ajoutez un README conforme au modèle ci-dessous, implémentez le projet et déployez-le publiquement. Ajoutez le lien de déploiement au README.
4. Invitez le professeur Chafik Bouallam (github.com/chafik-boulealam-esisa) comme collaborateur sur le dépôt.

## Modèle de README (à copier dans chaque dépôt)

Titre : <Nom du projet>

Membres :
- Prénom Nom (rôle, GitHub username)

Description :
- Brève description du projet, stack technique, fonctionnalités IA, et lien de déploiement.

Checklist obligatoire :
- Cœur logique en C : indiquer l'emplacement du code C dans le dépôt.
- Base cloud : informations de connexion (ne pas committer de secrets).
- APIs IA : liste des services utilisés et où ils sont intégrés.
- Lien de déploiement : URL publique du projet.

Comment lancer : (exemple)
1. Installer les dépendances
2. Compiler le backend C : `make build` (ou instructions similaires)
3. Lancer : `./bin/app`

Liens utiles :
- DEMO : https://<votre-deploiement>
- Publication LinkedIn : <URL de votre post LinkedIn>

## Exigences de présentation et rendu final
- Préparez une présentation visuelle et concise (évitez de lire les diapositives).
- Première diapositive : logo ESISA, nom du projet, membres, et liste des examinateurs.
- Enregistrez une vidéo de démonstration et placez le lien dans le README.
- Le dépôt GitHub doit montrer une activité visible et professionnelle de tous les membres (commits, branches, messages clairs).
- À la fin, publiez la démonstration sur LinkedIn et ajoutez le lien dans le README.

Professeurs / jury à mentionner :
- Professeur Boulealam Chafik
- Professeur Mehdi Iraqi Houssaini
- Directeur Mekouar Khalid
- Othman Mekouar
- Mekouar Youssef

## Publications courtes (texte prêt à copier)

FR (court — pour Google Chat) :
```
Lancement du projet de fin de semestre — Groupes de 3–5. Coeur en C, DB cloud (Supabase/MongoDB), IA obligatoire. Créez votre dépôt sous chafik-boulealam-lab et invitez le Prof. Chafik Boulealam. Détails : https://github.com/chafik-boulealam-lab/esisa-students/blob/main/END_OF_SEMESTER_PROJECT.md
```

EN (court — optionnel) :
```
End-of-Semester Project launched — Groups of 3–5. Core logic in C, cloud DB (Supabase/MongoDB), AI integration required. Create a repo under chafik-boulealam-lab and invite Prof. Chafik Boulealam. Details: https://github.com/chafik-boulealam-lab/esisa-students/blob/main/END_OF_SEMESTER_PROJECT.md
```

## Exemple rapide : Dockerfile (backend C)
```
FROM ubuntu:24.04
RUN apt-get update && apt-get install -y build-essential
WORKDIR /app
COPY . .
RUN gcc -O2 -std=c11 -o app src/main.c
CMD ["./app"]
```

## Bonnes pratiques
- N'ajoutez jamais de secrets en clair dans le dépôt. Utilisez des variables d'environnement ou des services de secret management.
- Documentez les étapes d'installation et d'exécution dans le README.

## Contact
En cas de question, contactez le professeur : ch.boulealam@esisa.ac.ma

---
Fin du document.
End of file.

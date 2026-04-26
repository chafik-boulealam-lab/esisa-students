# ESISA — Projet de fin de semestre — Feuille de route professionnelle

Ce document est une fiche pratique et pédagogique destinée aux étudiants : il explicite la feuille de route, les livrables exigés et les recommandations techniques. Le ton est analytique et orienté « professionnel reproducible ». Tous les livrables finaux doivent respecter la spécification complète : [END_OF_SEMESTER_PROJECT.md](./END_OF_SEMESTER_PROJECT.md).

---

## Objectif et audience

- Public : étudiants en fin de cycle (groupes de 3–5).
- Objectif : produire un produit logiciel professionnel, déployé, testé et documenté, intégrant au moins une composante IA.
- Supervision : Prof. Mehdi Iraqi Houssaini (Course) et Prof. Chafik Boulealam (TP).

---

## Calendrier

- Durée du projet : 1 mois.
- Soutenance finale (date fixe) : 30/05/2026.

---

## Vue synthétique — Livrables critiques

| Livrable | Description courte | Exigence minimale |
|---|---:|---|
| Dépôt GitHub public | Code source, issues, PRs | `project-<groupe>-<sujet>` sous `chafik-boulealam-lab` + invitation Prof. Boulealam |
| README.md | Présentation, instructions, lien demo, lien LinkedIn | Complet, clair, liens actifs |
| Backend (C) | Cœur logique compilable | Code en C + instructions build |
| Tests | Unitaires & intégration | CI ou scripts de test reproductibles |
| Déploiement | URL publique ou page distrib. | Vercel / Expo / Itch.io selon cible |
| Vidéo démo | 5–10 minutes | Lien dans README + post LinkedIn |

---

## Feuille de route condensée (4 semaines)

Semaine 1 — Conception & prototype

- Rédiger la problématique, objectifs mesurables et critères de succès.
- Documenter l'architecture (diagramme) et fournir un prototype minimal exécutable.
- Livrable : `docs/architecture.md`, prototype minimal.

Semaine 2 — Implémentation initiale

- Implémenter le backend C (cœur logique) et intégrer la première fonctionnalité IA.
- Mettre en place les tests unitaires essentiels.

Semaine 3 — Tests & intégration continue

- Étendre les tests, corriger les bugs, mesurer précision/latence IA.
- Configurer CI (GitHub Actions recommandé) et préparer le pipeline de déploiement.

Semaine 4 — Déploiement, finalisation et soutenance

- Déployer la version de production (Vercel / Expo / Itch.io selon cible).
- Préparer les slides, enregistrer la vidéo démo (5–10 min) et publier sur LinkedIn.
- Finaliser la checklist et valider les critères avant la soutenance du 30/05/2026.

---

## Checklist technique (à cocher avant soutenance)

- [ ] Dépôt public nommé correctement
- [ ] `README.md` complet avec liens de déploiement
- [ ] Backend C compilable avec instructions
- [ ] Tests automatisés et script d'exécution
- [ ] Base locale : **SQLite** (obligatoire pour tests locaux)
- [ ] Base production : Supabase ou MongoDB (si déployé)
- [ ] Déploiement actif et accessible (Vercel / Expo / Itch.io)
- [ ] Vidéo démonstration + lien LinkedIn

---

## Architecture recommandée — « Hybrid Deep Learning Architecture »

Résumé : un design « hybride » combine des composants légers exécutés localement (faible latence, offline, confidentialité) et des composants lourds exécutés côté serveur (GPU, entraînement, modèles volumineux). Cette approche maximise la portabilité tout en permettant des performances élevées en production.

Principes clefs :

- **Séparation des responsabilités** : le cœur en C gère la logique critique et le prétraitement, la couche IA est exposée via une API interne (REST/gRPC) ou via un binding FFI quand la latence est critique.
- **Modularité** : encapsulez l’inférence dans un microservice distinct (ex. FastAPI, TorchServe, Triton) afin de pouvoir mettre à jour le modèle indépendamment.
- **Interopérabilité** : exportez les modèles en ONNX/TFLite pour faciliter l’inférence depuis des clients non-Python (C, WebAssembly, mobile).
- **Fallback local** : sur l’appareil/local, fournissez un modèle léger quantifié (ONNX / TFLite) pour permettre une dégradation gracieuse hors-ligne; la base locale SQLite stocke les entrées et résultats pour synchronisation.

Flux de données (exemple simple) :

1. Entrée utilisateur → prétraitement local (C)
2. Si inference légère possible → local ONNX/TFLite inference
3. Sinon → requête au microservice IA (REST/gRPC) pour inference lourde
4. Résultat → post-traitement local + stockage (SQLite local), puis synchronisation vers DB cloud si disponible

Recommandations d’implémentation :

- Entraînement & experimentation : Python + PyTorch/Lightning (env. GPU)
- Conversion modèle : exporter en ONNX, vérifier quantification (INT8) pour déploiement edge
- Serving : FastAPI + Uvicorn / TorchServe / Triton selon contraintes
- Client C : utiliser `libcurl` ou sockets pour communiquer avec le service IA, ou lier ONNX Runtime C API pour inference intégrée
- Observabilité : journalisation, métriques, et tests de robustesse sur cas limites

Considérations pratiques :

- Protégez les données sensibles avant synchronisation.
- Pensez à la taille du modèle pour mobile/desktop.
- Mesurez latence & précision et documentez un plan de dégradation.

---

## Exemples de commandes minimales (développement local)

```bash
# Build (exemple)
make build

# Lancer l'app (exemple)
./bin/app --config config/local.yaml

# Tests
pytest tests/
```

La base locale de développement doit être **SQLite** (fichier `data/local.db`) ; les scripts d'initialisation doivent permettre d'initialiser une instance locale mimant la base cloud.

---

## Critères d’évaluation (rapide)

- Fonctionnalité & Qualité (20%) — Le projet fonctionne comme décrit et couvre les exigences.
- Intégration IA (20%) — Pertinence et qualité de l'intégration IA.
- Qualité du code & tests (10%) — Propreté, structure, tests.
- Déploiement & accessibilité (10%) — Application déployée et accessible.
- Présentation & vidéo (40%) — Clarté et professionnalisme de la soutenance et du matériel (LinkedIn, Video, Branding).

---

## Contact

Prof. Chafik Boulealam — ch.boulealam@esisa.ac.ma

---

Document court rédigé pour usage étudiant et professionnel. Pour la spécification complète et les consignes détaillées, consultez : [END_OF_SEMESTER_PROJECT.md](./END_OF_SEMESTER_PROJECT.md).

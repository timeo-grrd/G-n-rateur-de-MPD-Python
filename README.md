# Generateur-de-MPD-Python
Création d'un générateur de mot de passe simple

Un script simple et efficace en Python pour générer des mots de passe personnalisés en fonction de vos besoins de sécurité.

## 📝 Description

Ce programme permet de générer un mot de passe aléatoire en demandant à l'utilisateur :
1. Le nombre minimum de caractères souhaités.
2. S'il souhaite inclure des **chiffres**.
3. S'il souhaite inclure des **caractères spéciaux**.

Le script génère d'abord une base de lettres, puis ajoute aléatoirement des chiffres et des symboles si les options sont activées.

## ✨ Fonctionnalités

- **Personnalisation** : Choisissez la longueur minimale.
- **Sécurité adaptable** : Options pour inclure des chiffres (`0-9`) et des caractères spéciaux (`!`, `@`, `#`, etc.).
- **Aléatoire** : Utilise le module `random` de Python.

## 🚀 Comment l'utiliser ?

### Prérequis
- Avoir **Python 3** installé sur votre machine.

### Lancement
1. Clonez le dépôt ou téléchargez le fichier `.py`.
2. Ouvrez un terminal dans le dossier du projet.
3. Lancez la commande suivante :
   ```bash
   python générateur_de_mdp.py
🛠️ Aperçu du code
Le script utilise des listes prédéfinies pour :

Les lettres (majuscules et minuscules).

Les chiffres.

Une large sélection de caractères spéciaux.

Python
# Exemple de fonctionnement
# Entrez le nombre de caractères minimum souhaitez : 8
# Voulez vous des chiffres ? : o
# Voulez vous des caractères spéciaux ? : o
# Résultat : aBzTqLmP5s@

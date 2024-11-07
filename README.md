# S-P_ML_final_project
Attrition Prediction on IBM Data
Ce projet a pour objectif de développer un modèle de machine learning capable de prédire l'attrition des employés au sein d'une entreprise. L'attrition des employés, ou le taux de rotation du personnel, est un enjeu majeur pour les organisations, car elle impacte directement la productivité, les coûts de recrutement et la culture d'entreprise. En identifiant les facteurs clés qui contribuent au départ des employés, l'entreprise peut mettre en place des stratégies pour améliorer la rétention du personnel.

Table des Matières
    Introduction
    Description des Données
    Préparation des Données
    Analyse Exploratoire des Données
    Ingénierie des Caractéristiques
    Construction du Modèle
    Évaluation du Modèle
    Résultats et Discussion
    Conclusion
    Prérequis
    Auteurs et Collaborateurs


Introduction

Dans un contexte concurrentiel, la rétention des talents est cruciale pour le succès d'une entreprise. Ce projet utilise des techniques de machine learning pour analyser les données des employés et prédire lesquels sont susceptibles de quitter l'entreprise. Cela permettra aux gestionnaires de ressources humaines de prendre des mesures proactives pour retenir les employés à risque.

Description des Données

Le jeu de données utilisé provient du service des ressources humaines de l'entreprise et contient des informations sur les employés, notamment :
Données démographiques : Âge, sexe, état civil.
Informations professionnelles : Département, rôle, niveau d'éducation, nombre d'années d'expérience.
Informations salariales : Salaire, augmentations récentes, satisfaction vis-à-vis du salaire.
Engagement et performance : Satisfaction au travail, performance annuelle, nombre d'heures travaillées.
Autres facteurs : Nombre d'enfants, distance domicile-travail, formation reçue.

Le dataset comporte 35 colonnes et plusieurs milliers de lignes, chaque ligne représentant un employé.

Préparation des Données

Chargement des Données
Les données sont chargées à partir d'un fichier CSV en utilisant la bibliothèque pandas.
Gestion des Valeurs Manquantes
Variables Numériques : Les valeurs manquantes sont imputées en utilisant la moyenne de la colonne correspondante.
Variables Catégorielles : Les valeurs manquantes sont imputées avec la modalité la plus fréquente.

Encodage des Variables Catégorielles
Utilisation de l'encodage One-Hot Encoding pour transformer les variables catégorielles en variables numériques.

Normalisation des Données
Les variables numériques sont normalisées pour avoir une moyenne de 0 et un écart-type de 1, ce qui est essentiel pour certains algorithmes de machine learning.

Analyse Exploratoire des Données

Une analyse exploratoire approfondie a été réalisée pour comprendre les relations entre les variables et identifier les facteurs qui pourraient influencer l'attrition.

Visualisation des Distributions : Histogrammes, boîtes à moustaches pour analyser la distribution des variables numériques.
Matrices de corrélation : Pour identifier les corrélations entre les variables.
Analyses Bivariées : Comparaison des distributions en fonction de la variable cible (attrition).

Ingénierie des Caractéristiques

Création de nouvelles variables basées sur les données existantes, telles que le ratio salaire/satisfaction ou le nombre d'années depuis la dernière promotion.
Sélection des caractéristiques les plus pertinentes en utilisant des techniques de réduction de dimensionnalité.

Construction du Modèle

Plusieurs algorithmes de classification ont été testés :

Régression Logistique
Arbres de Décision
Forêts Aléatoires
Gradient Boosting
Support Vector Machines (SVM)

Pipeline de Modélisation

Un pipeline a été mis en place pour automatiser le processus de prétraitement et de modélisation :

Prétraitement : Imputation, encodage, normalisation.
Modélisation : Entraînement du modèle sélectionné.
Validation : Évaluation des performances via validation croisée.

Optimisation des Hyperparamètres

Utilisation de la Recherche sur Grille (GridSearchCV) pour trouver les meilleurs hyperparamètres pour chaque modèle.
Les métriques utilisées pour l'optimisation incluent l'accuracy, le rappel et le F1-score.

Évaluation du Modèle

Les modèles ont été évalués en utilisant :

Matrice de Confusion : Pour visualiser les performances du modèle en termes de vrais positifs, faux positifs, vrais négatifs et faux négatifs.
Courbe ROC et AUC : Pour évaluer la capacité du modèle à distinguer entre les classes.
Rapport de Classification : Fournissant l'accuracy, la précision, le rappel et le F1-score.

Résultats et Discussion

Le modèle de Forêt Aléatoire a obtenu les meilleures performances avec un F1-score de 0.85.
Les variables les plus importantes identifiées incluent la satisfaction au travail, le nombre d'années dans l'entreprise, et le nombre d'heures travaillées par mois.
Les résultats suggèrent que les employés insatisfaits et surmenés sont plus susceptibles de quitter l'entreprise.

Conclusion

Le projet a réussi à développer un modèle performant pour prédire l'attrition des employés. Les insights obtenus peuvent aider l'entreprise à mettre en place des politiques pour améliorer la satisfaction des employés et réduire le taux de rotation.

Prérequis

    Python 3.x
    Bibliothèques Python :
        pandas
        numpy
        matplotlib
        seaborn
        scikit-learn
    Jupyter Notebook

Auteurs et Collaborateurs

    Auteurs : Paul-Hugo Donati et Stanislas Collineau de Meezemaker
    Collaborateur : Guillaume Desforges

Remerciements

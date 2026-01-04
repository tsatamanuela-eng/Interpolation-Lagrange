import sympy as sp  # Importation de la bibliothèque sympy pour les calculs symboliques
import numpy as np  # Importation de la bibliothèque numpy pour les calculs numériques
import matplotlib.pyplot as plt  # Importation de matplotlib.pyplot pour l'affichage graphique

def interpolation_lagrange_option1():
    try:
        # Demander les noeuds
        noeuds = list(map(float, input("Entrez les noeuds séparés par des espaces: ").split()))
        if len(noeuds) != len(set(noeuds)):
            raise ValueError("Les noeuds doivent être distincts deux à deux.")  # Vérifie que les noeuds sont distinct
        # Demander les valeurs correspondantes aux noeuds
        valeurs = []
        for i, noeud in enumerate(noeuds):
            valeur = float(input(f"Entrez la valeur correspondante au noeud {noeud}: "))
            valeurs.append(valeur)  # Stocke les valeurs correspondantes aux noeuds

        x = sp.symbols('x')  # Déclare une variable symbolique x
        polynome = sp.simplify(sum(
            valeurs[i] * sp.prod([(x - noeuds[j]) / (noeuds[i] - noeuds[j]) for j in range(len(noeuds)) if j != i]) for
            i in range(len(noeuds))))  # Calcule le polynôme d'interpolation de Lagrange

        # Afficher le polynôme avec des coefficients sous forme de fractions
        polynome_fraction = sp.nsimplify(polynome, [sp.Rational])
        print(f"Polynôme d'interpolation de Lagrange (coefficients en fractions) : {polynome_fraction}")

        # Estimation d'une valeur
        valeur_estimee = float(input("Entrez une valeur pour estimer le polynôme: "))
        estimation = polynome.subs(x, valeur_estimee)  # Calcule la valeur estimée du polynôme pour l'entrée
        print(f"Valeur estimée: {estimation}")

        # Affichage du graphique
        noeuds_x = np.array(noeuds)
        valeurs_y = np.array(valeurs)
        x_vals = np.linspace(min(noeuds_x) - 1, max(noeuds_x) + 1, 400)
        y_vals = [polynome.subs(x, val) for val in x_vals]

        plt.plot(x_vals, y_vals, label="Polynôme d'interpolation de Lagrange")
        plt.scatter(noeuds_x, valeurs_y, color='red', label="Noeuds")
        plt.scatter([valeur_estimee], [estimation], color='green', label="Estimation")
        plt.grid(True)
        plt.legend()
        plt.show()  # Affiche le polynôme, les noeuds et la valeur estimée sur un graphique

    except ValueError as e:
        print(e)  # Capture et affiche les erreurs potentielles

def interpolation_lagrange_option2():
    try:
        # Demander les noeuds et la fonction
        noeuds = list(map(float, input("Entrez les noeuds séparés par des espaces: ").split()))
        fonction = input("Entrez une fonction valide en termes de x (par ex. x**2 + 2*x + 1, ln(x), 1/x): ")
        f = sp.sympify(fonction)  # Convertit la fonction d'entrée en une expression symbolique

        x = sp.symbols('x')  # Déclare une variable symbolique x
        valeurs = []
        for noeud in noeuds:
            valeur = f.subs(x, noeud)
            if not valeur.is_real:
                raise ValueError(f"Le noeud {noeud} n'est pas dans le domaine de définition de la fonction.")
            valeurs.append(valeur)  # Calcule les valeurs de la fonction aux noeuds et vérifie qu'elles sont réelles

        polynome = sp.simplify(sum(
            valeurs[i] * sp.prod([(x - noeuds[j]) / (noeuds[i] - noeuds[j]) for j in range(len(noeuds)) if j != i]) for
            i in range(len(noeuds))))  # Calcule le polynôme de Lagrange

        # Afficher le polynôme avec des coefficients sous forme de fractions
        polynome_fraction = sp.nsimplify(polynome, [sp.Rational])
        print(f"Polynôme d'interpolation de Lagrange (coefficients en fractions) : {polynome_fraction}")

        # Estimation d'une valeur
        valeur_estimee = float(input("Entrez un point pour estimer par le polynôme et la fonction: "))
        estimation_fonction = f.subs(x, valeur_estimee)  # Calcule la valeur estimée de la fonction pour l'entrée

        # Vérification du domaine de définition
        if not estimation_fonction.is_real:
            raise ValueError("Le point n'est pas dans le domaine de définition de la fonction.")

        estimation_polynome = polynome.subs(x, valeur_estimee)  # Calcule la valeur estimée du polynôme pour l'entrée
        print(f"Valeur estimée par le polynôme: {estimation_polynome}")
        print(f"Valeur estimée par la fonction: {estimation_fonction}")

        # Affichage du graphique
        noeuds_x = np.array(noeuds, dtype=float)
        valeurs_y = np.array(valeurs, dtype=float)
        x_vals = np.linspace(min(noeuds_x) - 1, max(noeuds_x) + 1, 400)
        y_vals_polynome = [float(polynome.subs(x, val).evalf()) for val in x_vals]
        y_vals_fonction = [float(f.subs(x, val).evalf()) if f.subs(x, val).is_real else np.nan for val in x_vals]

        plt.plot(x_vals, y_vals_polynome, label="Polynôme d'interpolation de Lagrange")
        plt.plot(x_vals, y_vals_fonction, label="Fonction")
        plt.scatter(noeuds_x, valeurs_y, color='red', label="Noeuds")
        plt.scatter([valeur_estimee], [estimation_polynome], color='green', label="Estimation par polynôme")
        plt.scatter([valeur_estimee], [estimation_fonction], color='blue', label="Estimation par fonction")
        plt.grid(True)
        plt.legend()
        plt.show()  # Affiche le polynôme, la fonction, les noeuds et les estimations sur un graphique

    except ValueError as e:
        print(e)  # Capture et affiche les erreurs potentielles

def main():
    print("Choisissez une option:")
    print("1. Entrer des noeuds et des valeurs d'interpolation")
    print("2. Entrer des noeuds et une fonction")
    option = input("Entrez 1 ou 2: ")  # Demande à l'utilisateur de choisir une option

    if option == '1':
        interpolation_lagrange_option1()  # Exécute la fonction correspondante à l'option choisie
    elif option == '2':
        interpolation_lagrange_option2()  # Exécute la fonction correspondante à l'option choisie
    else:
        print("Option invalide.")  # Affiche un message si l'option est invalide

if __name__ == "__main__":
    main()  # Exécute la fonction main si ce script est exécuté directement

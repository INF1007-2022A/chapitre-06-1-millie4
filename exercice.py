#!/usr/bin/env python
# -*- coding: utf-8 -*-


from itertools import count


def order(values_list: list = None) -> list:
    values_list = []
    while len(values_list) < 10:
        value = input(f"Entrez une {len(values_list)+1}me valeur: ")
        if not value.isnumeric():
            print("La valeur doit être un chiffre!")
            continue
        values_list.append(float(value))
    values_list.sort()
    return values_list


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        word0 = list(input("Entrez le premier mot: "))
        word1 = list(input("Entrez le deuxième mot: "))
    return sorted(word0) == sorted(word1)


def contains_doubles(items: list) -> bool:
    return not list(set(items)) == sorted(items)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = ""
    meilleure_moyenne = 0
    for k in student_grades:
        moyenne = sum(student_grades[k]) / len(student_grades[k])
        if moyenne > meilleure_moyenne: 
            best_student = k
            meilleure_moyenne = moyenne
    return {best_student:student_grades[best_student]}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    lettres_frequentes = []
    for c in sentence:
        if sentence.count(c) > 4 and c.isalpha():
            lettres_frequentes.append(c)
    def freq_ind(lettre):
        return sentence.count(lettre)
    lettres_frequentes.sort(reverse=True, key=freq_ind)
    tableau = {}
    for l in lettres_frequentes:
        tableau.update({sentence.count(l):l})
    return tableau


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    livre_de_recettes = {}
    is_more_recipes = True
    while is_more_recipes:
        nom = input("What are we making today? ")
        ingredients = set({})
        ingredients.add(input("FIRST INGREDIENT: "))
        is_more_ing = True
        while is_more_ing:
            question = input("Are there more ingredients? (YES or NO) ") 
            if question == "YES":
                ingredients.add(input("NEXT: "))
            elif question == "NO": 
                is_more_ing = False
                continue
            else: 
                print("huh?")
                continue
        livre_de_recettes.update({nom:ingredients})
        no_more_recipes = True
        while no_more_recipes:
            plus_de_recettes = input("Is there another recipe? (YES or NO) ")
            if plus_de_recettes == "NO":
                is_more_recipes = False
                no_more_recipes = False
            elif plus_de_recettes == "YES": no_more_recipes = False
            else: print("huh?")
    return livre_de_recettes

def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input("What recipe do you want to see? ")
    if nom in ingredients:
        return ingredients[nom]
    else: return "Recipe not found."


def main() -> None:
    #print(f"On essaie d'ordonner les valeurs...")
    #print(order())

    #print(f"On vérifie les anagrammes...")
    #print(anagrams())

    #my_list = [3, 3, 5, 6, 1, 1]
    #print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    #grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    #best_student = best_grades(grades)
    #print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    #sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    #print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()
    
    print("On affiche une recette au choix...")
    found_recipe = print_recipe(recipes)
    for ingredient in found_recipe:
        print("-", ingredient)


if __name__ == '__main__':
    main()

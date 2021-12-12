import pickle

recipes = {}


def read_recipes():
    global recipes
    try:
        file = open("recipes.txt", "r+")
        for l in file.readlines():
            tokens = l.strip().split()
            recipes[tokens[0]] = tokens[1:]
        file.close()
    except Exception as e:
        print(f"Cannot open file {e}")
    pass


def write_recipes():
    global recipes
    try:
        file = open("recipes.txt", "w")
        for recipe in recipes.keys():
            file.write(" ".join([recipe, *recipes[recipe]]))
        file.close()
        print("Saved")
    except Exception as e:
        print(f"Cannot write recipes {e}")
    pass


def show_recipes(ingredients: list = None):
    global recipes
    for ingredient in ingredients:
        matches = {}
        for recipe_name in recipes.keys():
            if ingredient in recipes[recipe_name]:
                matches[recipe_name] = recipes[recipe_name]
        if len(matches) > 0:
            print(f"Recipes with {ingredient} : ")
            print("\t ", matches)
        else:
            print(f"There are no matches for this ingredient: {ingredient}")

    if len(ingredients) == 1:
        return
    matching_all = {}
    for recipe_name in recipes.keys():
        matching_all[recipe_name] = recipes[recipe_name]
        for ingredient in ingredients:
            if ingredient not in recipes[recipe_name]:
                matching_all.pop(recipe_name)
    if len(matching_all) > 0:
        print(f"Recipes with all : {[str(i) for i in ingredients]}")
        print(matching_all, sep="\n\t")
    else:
        print(f"There are no recipes containing all the ingredients given {[str(i) for i in ingredients]}")


def add_recipe(tokens: list = None):
    if tokens is None:
        return
    global recipes
    try:
        recipes[tokens[0]] = tokens[1:]
    except Exception as e:
        print(f"Cannot write recipe {e}")


def main():
    read_recipes()
    print(" - Add a recipe with: \n\tadd <Recipe name> <ingredient1> ...<ingredient n>")
    print(" - Show matching recipes for different ingredients: \n\tshow <ingredient 1> ... <ingredient n>")
    while True:
        command = str(input(">>> "))
        tokens = command.strip().split()
        if len(tokens) == 0:
            continue
        if tokens[0].__contains__("show"):
            show_recipes(tokens[1:])
        elif tokens[0].__contains__("add"):
            add_recipe(tokens[1:])
        elif tokens[0].__contains__("save"):
            write_recipes()
        elif tokens[0].__contains__("exit"):
            write_recipes()
            exit()
        else:
            print(f"Unknown command: {tokens[0]}")
    pass


main()

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

DATA = {
    'Омлет': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'Паста': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'Бутерброд': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def home_view(request):
    template_name = 'calculator/home.html'
    pages = list(DATA.keys())

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def hello(request, recipe_name):
    templates_name = 'calculator/index.html'
    if recipe_name in DATA:
        result_value = dict()
        recipe_ingredients = DATA[recipe_name]
        servings = request.GET.get('servings', 1)
        for ingredient, value in recipe_ingredients.items():
            result_value[ingredient] = value * int(servings)
            context = {
                'recipe_name':recipe_name,
                'recipe': result_value
            }
    else:
        context = None
    return render(request, templates_name, context)



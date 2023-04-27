from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet_view(request):
    servings = request.GET.get('servings')
    if servings:
        context = {
            'recipe': { i: DATA['omlet'][i] * int(servings) for i in DATA['omlet'] }
        }
    else:
        context = {
            'recipe': DATA['omlet']
        }
    return render(request, 'calculator/index.html', context)

def pasta_view(request):
    servings = request.GET.get('servings')
    if servings:
        context = {
            'recipe': { i: DATA['pasta'][i] * int(servings) for i in DATA['pasta'] }
        }
    else:
        context = {
            'recipe': DATA['pasta']
        }
    return render(request, 'calculator/index.html', context)

def buter_view(request):
    servings = request.GET.get('servings')
    if servings:
        context = {
            'recipe': { i: DATA['buter'][i] * int(servings) for i in DATA['buter'] }
        }
    else:
        context = {
            'recipe': DATA['buter']
        }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

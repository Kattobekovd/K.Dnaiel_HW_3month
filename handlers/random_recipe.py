from aiogram import Router, types, F
from random import choice


random_recipe_router = Router()


@random_recipe_router.message(F.text == 'Хочу рецепт')
async def random_recipe_handler(message: types.Message):
    recipes = [
        {
            'photo': 'images/margarita.jpg',
            'caption': "Пицца «Маргарита»: Тесто для пиццы, помидоры, моцарелла, оливковое масло, базилик, соль и перец. Приготовление: 1. Раскатайте тесто. 2. Смажьте оливковым маслом. 3. Нарежьте помидоры и выложите на тесто. 4. Распределите моцареллу. 5. Запекайте в духовке при 220°C 15-20 минут. 6. Посыпьте базиликом, солью и перцем."
        },
        {
            'photo': 'images/roll.jpg',
            'caption': "Ролл «Калифорния»: Листы нори, рис для суши, крабовое мясо, авокадо, огурец, икра тобико. Приготовление: 1. Приготовьте рис и охладите. 2. Нарежьте авокадо и огурец. 3. На листе нори распределите рис. 4. В центр выложите крабовое мясо, авокадо и огурец. 5. Сверните ролл. 6. Нарежьте и посыпьте икрой тобико."
        },
        {
            'photo': 'images/salad.jpg',
            'caption': "Салат «Цезарь»: Куриное филе, листья римского салата, пармезан, крутоны, соус Цезарь. Приготовление: 1. Обжарьте куриное филе и нарежьте кубиками. 2. Порвите листья салата. 3. Смешайте салат, курицу, крутоны и пармезан. 4. Полейте соусом Цезарь и перемешайте."
        }
    ]

    selected_recipe = choice(recipes)

    await message.answer_photo(
        photo=types.FSInputFile(selected_recipe['photo']),
        caption=selected_recipe['caption']
    )

# ----------------------------------------------
# FitLife Console Bot     |script name         |
# V.1.00                  |script version      |
# 02.10.2026              |start project date  |
# Generalov A. Aleksandr  |author              |
# (Misticle)              |Git nickname        |
# ----------------------------------------------

print('FitLife Bot: Приветствую тебя, дружище! Добро пожаловать в FitLife!\n'
      'FitLife Bot: Как тебя зовут? Напиши свое имя:')  # 2) вежливо здоров.
user_name = input('новый пользователь:')    # 3.1 запрашивает имя
print(f'СИСТЕМА: Пользователь ->>> {user_name} <<<- зарегистрирован в '
      f'системе FitLife!\n'  # перенес строку из-за ошибки лайнера
      f'FitLife Bot: О! мощно! А сколько тебе лет? укажи числом:')

while True:  # цикл при ошибке ввода возраста (идея - ИИ агента)
    try:  # по расставленным " видно, что предложил ИИ
        user_age = int(input(f'{user_name} : '))  # 3.2 запрашивает возраст
        break  # Если всё верно, выходим из цикла
    except ValueError:  # Цикл повторяется в случае не верного ввода возраста
        print("Ошибка! Пожалуйста, введи целое число (например, 25).")


if user_age <= 20:  # 3 вариации ответа на разный возраст пользователя
    print('FitLife Bot: Молодой еще совсем! Значит энергии еще хоть отбавляй!')
elif user_age > 20 and user_age <= 40:
    print('FitLife Bot: В самом расцвете сил, значит?')
else:
    print('FitLife Bot: Солидный возраст, как я погляжу')

print('FitLife Bot: Теперь я бы хотел узнать твои вес и рост.\n'
      'СИСТЕМА: Укажите свой вес, кг.')

while True:
    try:  # запрос на введение веса тела в килограммах
        user_weight = float(input(user_name + ':'))
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введи целое число (например, 75).")

print('СИСТЕМА: Теперь, укажите свой рост, м.')

while True:
    try:  # запрос на введение роста в метрах
        user_height = float(input(user_name + ':'))
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введи число c дробной частью в метрах "
              "(например, 1.75).")

bmi = user_weight / (user_height ** 2)  # Рассчет ИМТ
bmi = round(bmi, 1)  # Округляем до одного знака после запятой

WATER_PER_KG = 30  # const: [мл/кг]
ML_IN_LITRE = 1000  # const: [л/мл]
water_ml = user_weight * WATER_PER_KG  # Рассчитать норму воды в миллилитрах
water_l = water_ml / ML_IN_LITRE  # Перевести в литры

if user_age < 5:
    age_marker = 'г'  # от 1 до 4 лет возраст - это год/года (г.)
else:
    age_marker = 'л'  # от 5 лет возраст - это лет (л.)

print(f'FitLife Bot: {user_name} Я провел расчеты и готов предоставить '
      f'отчет!\n\n'
      f'Отчет для пользователя: {user_name} {user_age}, {age_marker}.\n'
      f'Твой Индекс Массы Тела: {bmi}\n'
      f'Рекомендуемая норма воды: {water_l:.2f} л. в день\n'
      f'Расчет окончен. {user_name} Будьте здоровы!')

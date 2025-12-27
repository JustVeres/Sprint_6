from datetime import date, timedelta

"""Данные для заполнения на экране «Для кого самокат»"""
class WhoIsTheScooterFor:
    first_name = 'Бенедикт'         # Имя
    last_name = 'Камбербэтч'        # Фамилия
    city = 'Москва'                 # Адрес: куда привезти заказ
    metro_station = 'Выставочная'   # Станция метро
    number_phone = '89963212222'    # Телефон: на него позвонит курьер

"""Данные для заполнения на экране «Про аренду»"""
class AboutRent:
    next_day = date.today() + timedelta(days=1)
    next_day_order = next_day.strftime("%d.%m.%Y")  # Дата для заказа самоката (на следующий день)

    rent_a_day = 'сутки'            # Срок аренды (сутки)
    color_order = 'black'           # Цвет самоката (черный)

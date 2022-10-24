"""
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях, в доллары (курс: 1$ = 62 рубля) или в евро (курс: 1€ = 60 руб).
Для тех, кто хочет добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
"""


def summa(count: float, price: float) -> str:
    return f'{round(count * price, 2)}₽'


print(summa(305.5, 2.4))

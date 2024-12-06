salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
spend_per_months = 0
spend_itog = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
spend_in_first_month = 6000
for i in range(9):
    spend = spend * 1.03
    spend_itog += spend
salary_of_months = salary * 10
money_capital = round(spend_itog + spend_in_first_month) - salary_of_months
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
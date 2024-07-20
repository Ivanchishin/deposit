def entry(deposit, dep_term, percent_rate):
    kluch_stavka = 0.16
    platanaloga = 1000000 * kluch_stavka
    itog_deposit = round(((1 + (percent_rate / 1200)) ** dep_term) * deposit, 2)
    income_sum = round(itog_deposit - deposit, 2)
    nalog = 0
    if income_sum > platanaloga:
        nalog = round((income_sum - platanaloga) * 0.13, 2)
        income_sum = round(income_sum - nalog, 2)
        itog_deposit = deposit + income_sum
    format_income = "{:,.2f}".format(income_sum).replace(',', ' ')
    format_deposit = "{:,.2f}".format(itog_deposit).replace(',', ' ')
    format_nalog = "{:,.2f}".format(nalog).replace(',', ' ')
    print(
        f'За {dep_term} месяцев прибыль составила: {format_income} рублей\n'
        f'Сумма вклада: {format_deposit} рублей\n'
        f'Налог по вкладу составил: {format_nalog}')


if __name__ == '__main__':
    deposit = int(input("Введите сумму вклада: "))
    dep_term = int(input("Введите срок вклада в месяцах: "))
    percent_rate = float(input("Введите процентную ставку: "))
    entry(deposit, dep_term, percent_rate)

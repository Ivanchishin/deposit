def entry(deposit, dep_term, percent_rate):
    for i in range(1, dep_term + 1):
        income_sum = ((1 + (percent_rate / 1200)) ** i) * deposit
        print(
            f'За {i} месяцев прибыль составила: {round(round(income_sum, 2) - float(deposit),2)}'
            f',cумма вклада: {round(income_sum, 2)} рублей')


if __name__ == '__main__':
    deposit = int(input("ВВедите сумму вклада: "))
    dep_term = int(input("ВВедите срок вклада в месяцах: "))
    percent_rate = float(input("ВВедите процентную ставку: "))
    entry(deposit, dep_term, percent_rate)

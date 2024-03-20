#SOME SOME
def format_month_string(months):
    if months == 1:
        return "1 месяц"
    elif 2 <= months <= 4:
        return f"{months} месяца"
    else:
        return f"{months} месяцев"

def format_year_string(years):
    if years == 1:
        return "1 год"
    else:
        return f"{years} года"

def time_to_save(current_money, monthly_income, savings_percentage, target_purchase):
    if current_money >= target_purchase:
        print("У вас уже достаточно денег для покупки!")
        return

    total_savings = current_money
    months = 0

    while total_savings < target_purchase:
        total_savings += monthly_income * (savings_percentage / 100)
        months += 1

        # Увеличиваем сумму, если после окончания года не хватает денег
        if months % 12 == 0 and total_savings < target_purchase:
            total_savings += monthly_income * (savings_percentage / 100)

    years = months // 12
    remaining_months = months % 12

    print("Для накопления суммы {} вам потребуется:".format(target_purchase))
    if years > 0:
        print(format_year_string(years), end=' ')
    if remaining_months > 0:
        print(format_month_string(remaining_months), end=' ')
    print(".")

# Пример использования
current_money = float(input("Введите текущую сумму денег: "))
monthly_income = float(input("Введите ваш ежемесячный доход: "))
savings_percentage = float(input("Введите, сколько процентов от дохода вы готовы откладывать: "))
target_purchase = float(input("Введите стоимость покупки: "))

time_to_save(current_money, monthly_income, savings_percentage, target_purchase)

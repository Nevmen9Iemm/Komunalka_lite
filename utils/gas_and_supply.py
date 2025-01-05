


# Функція для розрахунку газу
def calculate_gas_and_supply(phone_number):
    try:
        if current_gas < previous_gas:
            print("Помилка: поточні показники повинні бути більшими за попередні.")
            calculate_gas_and_supply(phone_number)
            return

        rate_gas = 7.96
        rate_supply = 1.308
        usage_gas = current_gas - previous_gas
        cost_gas = usage_gas * rate_gas
        cost_supply = usage_gas * rate_supply
        total_cost = cost_gas + cost_supply

        print(f"Загальна вартість за газ: {cost_gas:.2f} грн")
        print(f"Загальна вартість за газопостачання: {cost_supply:.2f} грн")
        print(f"Загальна сума: {total_cost:.2f} грн")

    except ValueError:
        print("Будь ласка, введіть правильні числові значення.")
        calculate_gas_and_supply(phone_number)
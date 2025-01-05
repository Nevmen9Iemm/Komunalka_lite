from utils.menu_processing import bill_details


# Функція для розрахунку газу
def calculate_gas_and_supply(phone_number):
    try:
        bill_details = []
        current_gas = float(input("Введіть поточні показники (м³): "))
        previous_gas = float(input("Введіть попередні показники (м³): "))
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

    except ValueError:
        print("Будь ласка, введіть правильні числові значення.")
        calculate_gas_and_supply(phone_number)
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

        print(f"Загальна вартість за газ: {cost_gas:.2f} грн")
        print(f"Загальна вартість за газопостачання: {cost_supply:.2f} грн")
        print(f"Загальна сума: {total_cost:.2f} грн")

        bill_details.append(
            f"Газ: {" " * 23} {cost_gas:.2f} грн\n"
            f"\nПоточні показники: {" " * 16} {int(current_gas)}\n"
            f"Попередні показники: {" " * 14} {int(previous_gas)}\n"
            f"\nСпожито: {" " * 22} {usage_gas:.2f} м3\n"
            f"{"-" * 41}\n"
            f"Газопостачання: {" " * 13} {cost_supply:.2f} грн\n"
            f"Об'єм тарнспортування: {" " * 8} {usage_gas:.2f} м3\n"
            f"Разом: {" " * 22} {total_cost:.2f} грн\n"
        )

        save_bill(phone_number, bill_details)
        next_step(phone_number)

    except ValueError:
        print("Будь ласка, введіть правильні числові значення.")
        calculate_gas_and_supply(phone_number)
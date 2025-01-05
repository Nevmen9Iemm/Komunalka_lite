import os
from tests.test_input_numbers import validate_phone_number
from datetime import datetime

from utils.bill_details import BillDetails
from utils.delete_old_files import delete_old_files
from utils.save_bill import save_bill


# Ініціалізація списку для зберігання рахунку
bill_details = []


def main():
    # Запит номера телефону
    phone_number = "380938094594" #input("Введіть номер телефону у форматі 380XXXXXXXXXX: ")
    if not validate_phone_number(phone_number):
        print("Неправильний формат номера телефону. Будь ласка, спробуйте знову.")
        main()
    bill = BillDetails(phone_number)
    choose_services(phone_number)
    next_step(phone_number)


def choose_services(phone_number):
    print(
    "Зробіть вибір комунальних послуг:",
    "1. Електроенергія",
    "2. Газ та газопостачання",
    "3. Повернутись до вибору номера телефону",
    "4. Видалити старі файли біллів та закінчити роботу",
    sep = "\n"
    )

    choice = '1' # input("Зробіть вибір (1, 2, 3 або 4): \n")

    if choice == '1':
        choose_electricity_tariff(phone_number)
    elif choice == '2':
        calculate_gas_and_supply(phone_number)
    elif choice == '3':
        main()
    elif choice == '4':
        delete_old_files("bill")
        exit()
    else:
        print("Неправильний вибір. Спробуйте ще раз")
        choose_services(phone_number)


def next_step(phone_number):    # Запит на продовження або завершення
    print(
        f" Виберіть:",
        f" 1) Продовжити",
        f" 2) Завершити",
        sep = "\n"
        )
    next_action = input("Введіть номер вибору (1 або 2): ")

    if next_action == '1':
        choose_services(phone_number)
    elif next_action == '2':
        delete_old_files("bill")
        exit()
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
        return next_action


def choose_electricity_tariff(phone_number):
    print(
        f"Оберіть тариф на електроенергію:",
        f" 1. Однозонний",
        f" 2. Двозонний",
        f" 3. Трьохзонний",
        f" 4. Повернутись до вибору комунальних послуг",
        sep = "\n"
        )

    tariff_choice = '1' # input("Введіть номер тарифу (1, 2, 3 або 4): ")

    if tariff_choice == '1':
        BillDetails(phone_number).calculate_single_zone_electricity(
            current_single_zone=1661,
            previous_single_zone=1513
        )
        save_bill(phone_number, bill_details)
        # print(bill.generate_bill())
        next_step(phone_number)
        # calculate_single_zone_electricity(phone_number)
    elif tariff_choice == '2':
        calculate_two_zone_electricity(phone_number)
    elif tariff_choice == '3':
        calculate_three_zone_electricity(phone_number)
    elif tariff_choice == '4':
        choose_services(phone_number)
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
        choose_electricity_tariff(phone_number)

# Функція для розрахунку електроенергіі з одною зон
def calculate_single_zone_electricity(phone_number):
    try:
        current_single_zone = float(input("Введіть поточні показники (кВт): "))
        previous_single_zone = float(input("Введіть попередні показники (кВт): "))
        if current_single_zone < previous_single_zone:
            print("Помилка: поточні показники повинні бути більшими за попередні.")
            calculate_single_zone_electricity(phone_number)
            return
        usage = current_single_zone - previous_single_zone
        rate = 4.32
        cost = usage * rate
        print(f"Загальна вартість за електроенергію: {cost:.2f} грн")
        bill_details.append(
            f"Електроенергія (Однозонний): {cost:.2f} грн\n"
            f"Поточні показники: {" " * 15} {int(current_single_zone)}\n"
            f"Попередні показники: {" " * 13} {int(previous_single_zone)}\n"
            f"Кількість кВт: {" " * 21} {int(usage)}\n"
        )

        save_bill(phone_number, bill_details)
        next_step(phone_number)

    except ValueError:
        print("Будь ласка, введіть правильні числові значення")
        calculate_single_zone_electricity(phone_number)


# Функція для розрахунку електроенергіі з двох зон
def calculate_two_zone_electricity(phone_number):
    try:
        current_day_two_zone = float(input("Введіть поточні показники в зоні День (кВт): "))
        current_night_two_zone = float(input("Введіть поточні показники в зоні Ніч (кВт): "))
        previous_day_two_zone = float(input("Введіть попередні показники в зоні День (кВт): "))
        previous_night_two_zone = float(input("Введіть попередні показники в зоні Ніч (кВт): "))
        if current_day_two_zone < previous_day_two_zone or current_night_two_zone < previous_night_two_zone:
            print("Помилка: поточні показники повинні бути більшими за попередні.")
            calculate_two_zone_electricity(phone_number)
            return

        rate_day = 4.32
        rate_nigh = 2.16
        cost_day= current_day_two_zone - previous_day_two_zone
        cost_night = current_night_two_zone - previous_night_two_zone
        total_cost_day = cost_day * rate_day
        total_cost_night = cost_night * rate_nigh
        total_cost_two_zone = total_cost_day + total_cost_night
        print(f"Загальна вартість за електроенергію (Двозонний тариф): {total_cost_two_zone:.2f} грн")
        bill_details.append(
            f"Електроенергія (Двозонний):  {total_cost_two_zone:.2f} грн\n"
            f"\nПоточні показники День: {" " * 10} {int(current_day_two_zone)}\n"
            f"Поточні показники Ніч: {" " * 11} {int(current_night_two_zone)}\n"
            f"Попередні показники День: {" " * 8} {int(previous_day_two_zone)}\n"
            f"Попередні показники Ніч: {" " * 9} {int(previous_night_two_zone)}\n"
            f"Кількість кВт (День): {" " * 14} {int(cost_day)}\n"
            f"Кількість кВт (Ніч): {" " * 15} {int(cost_night)}\n"
        )

        save_bill(phone_number, bill_details)
        next_step(phone_number)

    except ValueError:
        print("Будь ласка, введіть правильні числові значення.")
        calculate_two_zone_electricity(phone_number)

# Функція для розрахунку електроенергіі з трьох зон
def calculate_three_zone_electricity(phone_number):
    try:
        current_night_three_zone = float(input("Введіть поточні показники Ніч (кВт): "))
        current_half_peak = float(input("Введіть поточні показники Напівпік (кВт): "))
        current_peak = float(input("Введіть поточні показники Пік (кВт): "))
        previous_night_three_zone = float(input("Введіть попередні показники Ніч (кВт): "))
        previous_half_peak = float(input("Введіть попередні показники Напівпік (кВт): "))
        previous_peak = float(input("Введіть попередні показники Пік (кВт): "))
        if current_night_three_zone < previous_night_three_zone or current_half_peak < previous_half_peak or current_peak < previous_peak:
            print("Помилка: поточні показники повинні бути більшими за попередні.")
            calculate_three_zone_electricity(phone_number)
            return

        peak_rate = 6.48
        half_peak_rate = 4.32
        night_rate = 1.728

        total_night_three_zone = current_night_three_zone - previous_night_three_zone
        cost_night_three_zone = total_night_three_zone * night_rate
        total_half_peak = current_half_peak - previous_half_peak
        cost_half_peak = total_half_peak * half_peak_rate
        total_peak = current_peak - previous_peak
        cost_peak = total_peak * peak_rate
        total_cost = cost_night_three_zone + cost_half_peak + cost_peak
        print(f"Загальна вартість за електроенергію (Трьохзонний тариф): {total_cost:.2f} грн")
        bill_details.append(
            f"Електроенергія (Трьохзонний): {total_cost:.2f}грн\n"
            f"\nПоточні показники Ніч: {" " * 11} {int(current_night_three_zone)}\n"
            f"Поточні показники Напівпік: {" " * 6} {int(current_half_peak)}\n"
            f"Поточні показники Пік: {" " * 11} {int(current_peak)}\n"
            f"Попередні показники Ніч: {int(previous_night_three_zone)}\n"
            f"Попередні показники Напівпік: {" " * 4} {int(previous_half_peak)}\n"
            f"Попередні показники Пік: {" " * 9} {int(previous_peak)}\n"
            f"Кількість кВт при Нічному тарифі:    {int(total_night_three_zone)}\n"
            f"Кількість кВт при Напівпік тарифі:   {int(total_half_peak)}\n"
            f"Кількість кВт при Пік тарифі: {" " * 6} {int(total_peak)}\n"
        )

        save_bill(phone_number, bill_details)
        next_step(phone_number)

    except ValueError:
        print("Будь ласка, введіть правильні числові значення.")
        calculate_three_zone_electricity(phone_number)


# Функція для розрахунку газу
def calculate_gas_and_supply(phone_number):
    try:
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


if __name__ == "__main__":
    main()
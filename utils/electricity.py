
from utils.bill_details import BillDetails


def choose_electricity_tariff(phone_number):
    print(
        f"Оберіть тариф на електроенергію:",
        f" 1. Однозонний",
        f" 2. Двозонний",
        f" 3. Трьохзонний",
        f" 4. Повернутись до вибору комунальних послуг",
        sep = "\n"
        )

    tariff_choice = input("Введіть номер тарифу (1, 2, 3 або 4): ")

    if tariff_choice == '1':
        bill = BillDetails(phone_number)
        bill.calculate_single_zone_electricity(
            current_single_zone='1661', #input("Введіть поточні показники (кВт): "),
            previous_single_zone='1513', #input("Введіть попередні показники (кВт): ")
        )

    elif tariff_choice == '2':
        bill = BillDetails(phone_number)
        bill.calculate_two_zone_electricity(
            current_day_two_zone='5956', #input("Введіть поточні показники в зоні День (кВт): "),
            current_night_two_zone='1661', #input("Введіть поточні показники в зоні Ніч (кВт): "),
            previous_day_two_zone='5323', #input("Введіть попередні показники в зоні День (кВт): "),
            previous_night_two_zone='1513', #input("Введіть попередні показники в зоні Ніч (кВт): ")
        )

    elif tariff_choice == '3':
        bill = BillDetails(phone_number)
        bill.calculate_three_zone_electricity(
        current_night_three_zone = '1661', #input("Введіть поточні показники Ніч (кВт): ")),
        current_half_peak = '1500', #input("Введіть поточні показники Напівпік (кВт): ")),
        current_peak = '5956', #input("Введіть поточні показники Пік (кВт): ")),
        previous_night_three_zone = '1513', #input("Введіть попередні показники Ніч (кВт): ")),
        previous_half_peak = '1200', #input("Введіть попередні показники Напівпік (кВт): ")),
        previous_peak = '5323', #input("Введіть попередні показники Пік (кВт): "))
        )
    elif tariff_choice == '4':
        choose_services(phone_number)
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
        choose_electricity_tariff(phone_number)

# Функція для розрахунку електроенергіі з одною зон
def calculate_single_zone_electricity(phone_number):
    try:
        if current_single_zone < previous_single_zone:
            print("Помилка: поточні показники повинні бути більшими за попередні.")
            calculate_single_zone_electricity(phone_number)
            return
        usage = current_single_zone - previous_single_zone
        rate = 4.32
        cost = usage * rate
        print(f"Загальна вартість за електроенергію: {cost:.2f} грн")

    except ValueError:
        print("Будь ласка, введіть правильні числові значення")
        calculate_single_zone_electricity(phone_number)


# Функція для розрахунку електроенергіі з двох зон
def calculate_two_zone_electricity(phone_number):
    try:
        if current_day_two_zone < previous_day_two_zone or current_night_two_zone < previous_night_two_zone:
            print("Помилка: поточні показники повинні бути більшими за попередні.")
            calculate_two_zone_electricity(phone_number)
            return

        rate_day = 4.32
        rate_nigh = 2.16
        cost_day= int(current_day_two_zone) - int(previous_day_two_zone)
        cost_night = int(current_night_two_zone) - int(previous_night_two_zone)
        total_cost_day = cost_day * rate_day
        total_cost_night = cost_night * rate_nigh
        total_cost_two_zone = total_cost_day + total_cost_night

    except ValueError:
        print("Будь ласка, введіть правильні числові значення.")
        calculate_two_zone_electricity(phone_number)

# Функція для розрахунку електроенергіі з трьох зон
def calculate_three_zone_electricity(phone_number):
    try:
        if current_night_three_zone < previous_night_three_zone or current_half_peak < previous_half_peak or current_peak < previous_peak:
            print("Помилка: поточні показники повинні бути більшими за попередні.")
            calculate_three_zone_electricity(phone_number)
            return

        peak_rate = 6.48
        half_peak_rate = 4.32
        night_rate = 1.728

        total_night_three_zone = int(current_night_three_zone) - int(previous_night_three_zone)
        cost_night_three_zone = total_night_three_zone * night_rate
        total_half_peak = int(current_half_peak) - int(previous_half_peak)
        cost_half_peak = total_half_peak * half_peak_rate
        total_peak = int(current_peak) - int(previous_peak)
        cost_peak = total_peak * peak_rate
        total_cost = cost_night_three_zone + cost_half_peak + cost_peak

    except ValueError:
        print("Будь ласка, введіть правильні числові значення.")
        calculate_three_zone_electricity(phone_number)
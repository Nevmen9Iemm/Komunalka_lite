from utils.bill_details import BillDetails



def choose_electricity_tariff(phone_number: str) -> None:
    print(
        f"Оберіть тариф на електроенергію:",
        f" 1. Однозонний",
        f" 2. Двозонний",
        f" 3. Трьохзонний",
        f" 4. Перейти до ведення показників газу та газопостачання",
        sep = "\n"
        )

    tariff_choice = input("Введіть номер тарифу (1, 2, 3 або 4): ")

    if tariff_choice == '1':
        bill = BillDetails(phone_number)
        bill.calculate_single_zone_electricity(
            current_single_zone = input("Введіть поточні показники (кВт): "),
            previous_single_zone = input("Введіть попередні показники (кВт): ")
        )

    elif tariff_choice == '2':
        bill = BillDetails(phone_number)
        bill.calculate_two_zone_electricity(
            current_day_two_zone = input("Введіть поточні показники в зоні День (кВт): "),
            current_night_two_zone = input("Введіть поточні показники в зоні Ніч (кВт): "),
            previous_day_two_zone = input("Введіть попередні показники в зоні День (кВт): "),
            previous_night_two_zone = input("Введіть попередні показники в зоні Ніч (кВт): ")
        )

    elif tariff_choice == '3':
        bill = BillDetails(phone_number)
        bill.calculate_three_zone_electricity(
        current_night_three_zone = input("Введіть поточні показники Ніч (кВт): "),
        current_half_peak = input("Введіть поточні показники Напівпік (кВт): "),
        current_peak = input("Введіть поточні показники Пік (кВт): "),
        previous_night_three_zone = input("Введіть попередні показники Ніч (кВт): "),
        previous_half_peak = input("Введіть попередні показники Напівпік (кВт): "),
        previous_peak = input("Введіть попередні показники Пік (кВт): ")
        )
    elif tariff_choice == '4':
        choose_gas_tariff(phone_number)
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
        choose_electricity_tariff(phone_number)


def choose_gas_tariff(phone_number: str) -> None:
    bill = BillDetails(phone_number)
    bill.calculate_gas_and_supply(
        current_gas=input("Введіть поточні показники (м³): "),
        previous_gas=input("Введіть попередні показники (м³): ")
    )
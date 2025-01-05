from utils.bill_details import BillDetails
from utils.electricity import choose_electricity_tariff
from utils.gas_and_supply import calculate_gas_and_supply
from utils.save_bill import save_bill
from utils.delete_old_files import delete_old_files

bill_details = []

def choose_services(phone_number):
    print(
    "Зробіть вибір комунальних послуг:",
    "1. Електроенергія",
    "2. Газ та газопостачання",
    "3. Видалити старі файли біллів та закінчити роботу",
    sep = "\n"
    )

    attempts = 0  # Лічильник невдач

    while attempts < 3:
        choice = input("Зробіть вибір (1, 2 або 3): ")

        if choice == '1':
            choose_electricity_tariff(phone_number)
            next_step(phone_number)
        elif choice == '2':
            bill = BillDetails(phone_number)
            bill.calculate_gas_and_supply(
                current_gas = 30800, #int(input("Введіть поточні показники (м³): ")),
                previous_gas = 29600, #int(input("Введіть попередні показники (м³): "))
            )
            next_step(phone_number)
        elif choice == '3':
            delete_old_files("bill")
            exit()
        else:
            attempts += 1  # Збільшуємо лічильник спроб
            print(f"Неправильний вибір. Спробуйте ще раз ({3 - attempts} спроб залишилося).")

    print("Спроби закінчились. Робота завершена.")

def next_step(phone_number):    # Запит на продовження або завершення
    print(
        f" Виберіть:",
        f" 1) Продовжити ",
        f" 2) Завершити",
        sep = "\n"
        )
    next_action = input("Введіть номер вибору (1 або 2): ")

    if next_action == '1':
        choose_services(phone_number)
    elif next_action == '2':
        delete_old_files("bill")
        print("Робота завершена")
        exit()
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
        return next_action
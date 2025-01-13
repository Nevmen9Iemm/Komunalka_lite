from tests.test_input_numbers import validate_phone_number
from utils.keeping_records import choose_electricity_tariff, choose_gas_tariff
from utils.delete_old_files import delete_old_files


def phone_numbers():
    # Запит номера телефону
    phone_number = input("Введіть номер телефону у форматі 380XXXXXXXXXX: ")

    if not validate_phone_number(phone_number):
        print("Неправильний формат номера телефону. Будь ласка, спробуйте знову.")
        phone_numbers()

    choose_services(phone_number)


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
            choose_gas_tariff(phone_number)
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
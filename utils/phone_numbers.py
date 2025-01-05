from utils.menu_processing import choose_services
from tests.test_input_numbers import validate_phone_number


def phone_numbers():
    # Запит номера телефону
    phone_number = '380938094594' #input("Введіть номер телефону у форматі 380XXXXXXXXXX: ")
    if not validate_phone_number(phone_number):
        print("Неправильний формат номера телефону. Будь ласка, спробуйте знову.")
        main()

    choose_services(phone_number)
import os
from datetime import datetime


def save_bill(phone_number, bill_details):
    # Створення папки Bill, якщо її ще немає
    if not os.path.exists("Bill"):
        os.makedirs("Bill")

    # Отримання поточного часу
    timedate = datetime.now().strftime("%Y%m%d")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Створення файлу з рахунком
    file_name = f"{timedate}_{phone_number}.txt"
    file_path = f"Bill/{file_name}.txt"
    with open(file_path, "a") as file:
        # Дата і час
        file.write(f"\n---- Рахунок від {timestamp} ----\n")
        file.write(f"\nРахунок для телефону: {" " * 5} {phone_number}\n")
        file.write("\n" + " " * 13 + "Деталі рахунку:\n")
        for item in bill_details:
            file.write(f"{item}\n")
        file.write("Дякуємо за користування нашими послугами!")
        file.write("\n" + "-" * 41 + "\n")

    print(f"Рахунок збережено у файлі: {file_name}")
import os
from datetime import datetime, timedelta

def delete_old_files(directory, age_in_years=1):
    """
    Видаляє файли, старші за вказану кількість років, у заданій папці.

    :param directory: Шлях до папки, в якій потрібно видалити файли.
    :param age_in_years: Кількість років, старші за яку файли будуть видалені.
    """
    # Поточна дата
    now = datetime.now()
    # Гранична дата (файли, створені раніше цієї дати, будуть видалені)
    cutoff_date = now - timedelta(days=age_in_years * 365)

    if not os.path.exists(directory):
        print(f"Папка {directory} не існує.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Перевіряємо, чи це файл
        if os.path.isfile(file_path):
            # Отримуємо час останньої зміни файлу
            file_creation_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            # Видаляємо файл, якщо він старший за граничну дату
            if file_creation_time < cutoff_date:
                os.remove(file_path)
                print(f"Файл {file_path} видалено, бо він старший за {age_in_years} рік(и).")
            else:
                print(f"Жодного файлу не видалено, бо він не старший за {age_in_years} рік(и).")
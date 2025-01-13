from utils.save_bill import save_bill


class BillDetails:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.electricity = None
        self.gas = None
        self.total_cost = 0.0

    def calculate_single_zone_electricity(self, current_single_zone, previous_single_zone, rate=4.32):
        bill_details = []
        if current_single_zone >= previous_single_zone:
            usage = int(current_single_zone) - int(previous_single_zone)
            cost = usage * rate

            self.electricity = {
                "type": "Однозонний",
                "current_single_zone": current_single_zone,
                "previous_single_zone": previous_single_zone,
                "usage": usage,
                "cost": cost,
            }
            self.total_cost += cost

            print(f"Загальна вартість за електроенергію: {cost:.2f} грн")

            bill_details.append(
                f"Електроенергія (Однозонний): {cost:.2f} грн\n"
                f"Поточні показники: {" " * 15} {int(current_single_zone)}\n"
                f"Попередні показники: {" " * 13} {int(previous_single_zone)}\n"
                f"Кількість кВт: {" " * 21} {int(usage)}\n"
            )

            save_bill(self.phone_number, bill_details)

        else:
            print("Будь ласка, введіть правильні числові значення")


    def calculate_two_zone_electricity(
            self,
            current_day_two_zone,
            current_night_two_zone,
            previous_day_two_zone,
            previous_night_two_zone,
            rate_day = 4.32,
            rate_nigh = 2.16
        ):
        bill_details = []
        usage_day = int(current_day_two_zone) - int(previous_day_two_zone)
        usage_night = int(current_night_two_zone) - int(previous_night_two_zone)
        cost = (usage_day * rate_day) + (usage_night * rate_nigh)
        self.electricity = {
            "type": "Двозонний",
            "current_day_two_zone": current_day_two_zone,
            "current_night_two_zone": current_night_two_zone,
            "previous_day_two_zone": previous_day_two_zone,
            "previous_night_two_zone": previous_night_two_zone,
            "usage_day": usage_day,
            "usage_night": usage_night,
        }
        self.total_cost += cost

        print(f"Загальна вартість за електроенергію (Двозонний тариф): {self.total_cost:.2f} грн")

        bill_details.append(
            f"Електроенергія (Двозонний):  {self.total_cost:.2f} грн\n"
            f"\nПоточні показники День: {" " * 10} {int(current_day_two_zone)}\n"
            f"Поточні показники Ніч: {" " * 11} {int(current_night_two_zone)}\n"
            f"Попередні показники День: {" " * 8} {int(previous_day_two_zone)}\n"
            f"Попередні показники Ніч: {" " * 9} {int(previous_night_two_zone)}\n"
            f"Кількість кВт (День): {" " * 14} {int(usage_day)}\n"
            f"Кількість кВт (Ніч): {" " * 15} {int(usage_night)}\n"
        )

        save_bill(self.phone_number, bill_details)

    def calculate_three_zone_electricity(
            self,
            current_peak,
            current_half_peak,
            current_night_three_zone,
            previous_peak,
            previous_half_peak,
            previous_night_three_zone,
            peak_rate=6.48,
            half_peak_rate=4.32,
            night_rate=1.728
        ):
        bill_details = []
        usage_peak = int(current_peak) - int(previous_peak)
        usage_half_peak = int(current_half_peak) - int(previous_half_peak)
        usage_night = int(current_night_three_zone)- int(previous_night_three_zone)
        cost = (usage_peak * peak_rate) + (usage_half_peak * half_peak_rate) + (usage_night * night_rate)
        self.electricity = {
            "type": "Трьохзонний",
            "current_peak": current_peak,
            "current_half_peak": current_half_peak,
            "current_night_three_zone": current_night_three_zone,
            "previous_peak": previous_peak,
            "previous_half_peak": previous_half_peak,
            "previous_night_three_zone": previous_night_three_zone,
            "cost": cost,
        }
        self.total_cost += cost

        print(f"Загальна вартість за електроенергію (Трьохзонний тариф): {self.total_cost:.2f} грн")

        bill_details.append(
            f"Електроенергія (Трьохзонний): {self.total_cost:.2f}грн\n"
            f"\nПоточні показники Ніч: {" " * 11} {int(current_night_three_zone)}\n"
            f"Поточні показники Напівпік: {" " * 6} {int(current_half_peak)}\n"
            f"Поточні показники Пік: {" " * 11} {int(current_peak)}\n"
            f"Попередні показники Ніч: {" " * 9} {int(previous_night_three_zone)}\n"
            f"Попередні показники Напівпік: {" " * 4} {int(previous_half_peak)}\n"
            f"Попередні показники Пік: {" " * 9} {int(previous_peak)}\n"
            f"Кількість кВт при Нічному тарифі:    {usage_night}\n"
            f"Кількість кВт при Напівпік тарифі:   {usage_half_peak}\n"
            f"Кількість кВт при Пік тарифі: {" " * 6} {usage_peak}\n"
        )

        save_bill(self.phone_number, bill_details)

    def calculate_gas_and_supply(self, current_gas, previous_gas, rate_gas=7.96, rate_supply=1.308):
        bill_details = []
        usage_gas = int(current_gas - previous_gas)
        cost_gas = usage_gas * rate_gas
        usage_supply = usage_gas
        cost_supply = usage_supply * rate_supply
        self.gas = {
            "current_gas": current_gas,
            "previous_gas": previous_gas,
            "usage_gas": usage_gas,
            "usage_supply": usage_supply,
            "cost_gas": cost_gas,
            "cost_supply": cost_supply
        }
        self.total_cost += cost_gas + cost_supply

        print(f"Загальна вартість за газ: {cost_gas:.2f} грн")
        print(f"Загальна вартість за газопостачання: {cost_supply:.2f} грн")
        print(f"Загальна сума: {self.total_cost:.2f} грн")

        bill_details.append(
            f"Газ: {" " * 23} {cost_gas:.2f} грн\n"
            f"\nПоточні показники: {" " * 16} {int(current_gas)}\n"
            f"Попередні показники: {" " * 14} {int(previous_gas)}\n"
            f"\nСпожито: {" " * 22} {usage_gas} м3\n"
            f"{"-" * 41}\n"
            f"Газопостачання: {" " * 13} {cost_supply:.2f} грн\n"
            f"Об'єм тарнспортування: {" " * 8} {usage_gas} м3\n"
            f"Загальна вартість: {" " * 9} {self.total_cost:.2f} грн\n"
        )

        save_bill(self.phone_number, bill_details)

    def generate_bill(self):
        bill_details = f"Номер телефону: {self.phone_number}\n"
        if self.electricity:
            bill_details += f"\nЕлектроенергія ({self.electricity['type']}):\n"
            for key, value in self.electricity.items():
                if key != "type":
                    bill_details += f"  {key.capitalize()}: {value}\n"
        if self.gas:
            bill_details += "\nГаз та газопостачання:\n"
            for key, value in self.gas.items():
                bill_details += f"  {key.capitalize()}: {value}\n"
        bill_details += f"\nЗагальна вартість: {self.total_cost:.2f} грн\n"
        save_bill(phone_number=self.phone_number, bill_details=bill_details)

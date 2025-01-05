from utils.save_bill import save_bill


class BillDetails:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.electricity = None
        self.gas = None
        self.total_cost = 0.0

    def calculate_single_zone_electricity(self, current_single_zone, previous_single_zone, rate=4.32):
        bill_details = []

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

    def calculate_two_zone_electricity(
            self,
            current_day_two_zone,
            current_night_two_zone,
            previous_day_two_zone,
            previous_night_two_zone,
            rate_day = 4.32,
            rate_nigh = 2.16
        ):
        usage_day = current_day_two_zone - previous_day_two_zone
        usage_night = current_night_two_zone - previous_night_two_zone
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
        usage_peak = current_peak - previous_peak
        usage_half_peak = current_half_peak - previous_half_peak
        usage_night = current_night_three_zone - previous_night_three_zone
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

    def calculate_gas(self, current_gas, previous_gas, rate_gas=7.96):
        usage_gas = current_gas - previous_gas
        cost = usage_gas * rate_gas
        self.gas = {
            "current_gas": current_gas,
            "previous_gas": previous_gas,
            "usage_gas": usage_gas,
            "cost": cost,
        }
        self.total_cost += cost

    def calculate_supply(self, current_gas, previous_gas, rate_supply=1.308):
        usage_supply = current_gas - previous_gas
        cost = usage_supply * rate_supply
        self.gas = {
            "current_gas": current_gas,
            "previous_gas": previous_gas,
            "usage_supply": usage_supply,
            "cost": cost,
        }
        self.total_cost += cost

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

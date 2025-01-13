import unittest
from unittest.mock import patch, MagicMock
from utils.menu_processing import choose_services, next_step
from utils.keeping_records import choose_electricity_tariff
from utils.gas_and_supply import calculate_gas_and_supply
from utils.save_bill import save_bill
from utils.delete_old_files import delete_old_files


class TestUtilities(unittest.TestCase):
    @patch("utils.electricity.choose_electricity_tariff")
    @patch("utils.menu_processing.next_step")
    def test_choose_services_option_1(self, mock_next_step, mock_choose_electricity_tariff):
        phone_number = "380638094594"

        # Мокування вибору "1"
        with patch("builtins.input", return_value="1"):
            choose_services(phone_number)

        # Перевіряємо виклики
        mock_choose_electricity_tariff.assert_called_once_with(phone_number)
        mock_next_step.assert_called_once_with(phone_number)

    @patch("utils.gas_and_supply.calculate_gas_and_supply")
    @patch("utils.menu_processing.next_step")
    def test_choose_services_option_2(self, mock_next_step, mock_calculate_gas_and_supply):
        phone_number = "380638094594"

        # Мокування вибору "2"
        with patch("builtins.input", return_value="2"):
            choose_services(phone_number)

        # Перевіряємо виклики
        mock_calculate_gas_and_supply.assert_called_once_with(phone_number)
        mock_next_step.assert_called_once_with(phone_number)

    @patch("utils.menu_processing.main")
    def test_choose_services_option_3(self, mock_main):
        phone_number = "380638094594"

        # Мокування вибору "3"
        with patch("builtins.input", return_value="3"):
            choose_services(phone_number)

        # Перевіряємо виклик функції main
        mock_main.assert_called_once()

    @patch("utils.delete_old_files.delete_old_files")
    @patch("builtins.exit")
    def test_choose_services_option_4(self, mock_exit, mock_delete_old_files):
        phone_number = "380638094594"

        # Мокування вибору "4"
        with patch("builtins.input", return_value="4"):
            choose_services(phone_number)

        # Перевіряємо виклики
        mock_delete_old_files.assert_called_once_with("bill")
        mock_exit.assert_called_once()

    @patch("utils.delete_old_files.delete_old_files")
    @patch("builtins.exit")
    def test_next_step_option_2(self, mock_exit, mock_delete_old_files):
        phone_number = "380638094594"

        # Мокування вибору "2" (завершення)
        with patch("builtins.input", return_value="2"):
            next_step(phone_number)

        # Перевіряємо, чи видаляються файли і чи програма завершується
        mock_delete_old_files.assert_called_once_with("bill")
        mock_exit.assert_called_once()

    @patch("utils.menu_processing.choose_services")
    def test_next_step_option_1(self, mock_choose_services):
        phone_number = "380638094594"

        # Мокування вибору "1" (продовження)
        with patch("builtins.input", return_value="1"):
            next_step(phone_number)

        # Перевіряємо, чи викликається `choose_services`
        mock_choose_services.assert_called_once_with(phone_number)


if __name__ == "__main__":
    unittest.main()
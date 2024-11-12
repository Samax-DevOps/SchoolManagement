import time

from pageobjects.dashboard_page import DashboardPage
from pageobjects.holiday_list_page import HolidayListPage
from utilities.ConfigReader import read_configuration
from pageobjects.login_page import LoginPage


class Test_Holiday_List:

    def test_add_holiday(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "username"),
                            read_configuration(self.environment, "password"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_holiday_list_tab()
        holiday_list_page = HolidayListPage(self.driver)
        holiday_list_page.click_on_date_field()
        holiday_list_page.click_on_today_day()
        holiday_list_page.enter_title("demo title")
        holiday_list_page.enter_description("demo desc")
        time.sleep(2)
        # holiday_list_page.click_on_reset_btn()
        holiday_list_page.click_on_submit_btn()
        success_msg = holiday_list_page.get_toast_msg()
        print(success_msg)
        assert success_msg in "Data Saved Successfully"
        time.sleep(5)

    def test_delete_holiday(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "username"),
                            read_configuration(self.environment, "password"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_holiday_list_tab()
        holiday_list_page = HolidayListPage(self.driver)
        holiday_list_page.delete_holiday()
        holiday_list_page.click_on_yes_delete_btn()
        success_msg = holiday_list_page.get_toast_msg()
        print(success_msg)
        assert 'Deleted' in success_msg

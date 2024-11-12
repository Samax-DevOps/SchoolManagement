import time

import pytest

from pageobjects.dashboard_page import DashboardPage
from pageobjects.timetable_page import TimetablePage
from utilities.ConfigReader import read_configuration
from pageobjects.login_page import LoginPage
from TestData import DataUtil


class Test_Timetable:

    @pytest.mark.parametrize("class_name, subject_name", DataUtil.dp2('test_create_timetable'))
    def test_create_timetable(self, class_name, subject_name):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "username"),
                            read_configuration(self.environment, "password"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_create_timetable()
        timetable_page = TimetablePage(self.driver)
        time.sleep(3)
        timetable_page.click_on_edit_button(class_name)
        time.sleep(1)
        timetable_page.drag_subject_to_day_and_time(subject_name)
        msg = timetable_page.get_toast_msg()
        assert "Saved" in msg

    @pytest.mark.parametrize("class_name", DataUtil.dp2('test_delete_timetable'))
    def test_delete_timetable(self, class_name):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "username"),
                            read_configuration(self.environment, "password"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_create_timetable()
        timetable_page = TimetablePage(self.driver)
        time.sleep(3)
        timetable_page.click_on_edit_button(class_name)
        time.sleep(1)
        timetable_page.delete_time_table()
        msg = timetable_page.get_toast_msg()
        assert "Deleted" in msg

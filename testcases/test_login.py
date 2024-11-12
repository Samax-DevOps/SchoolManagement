import time

import pytest
from selenium import webdriver

from pageobjects.dashboard_page import DashboardPage
from utilities.ConfigReader import read_configuration
from pageobjects.login_page import LoginPage


class Test_Login:

    def test_do_login(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "username"),
                            read_configuration(self.environment, "password"))
        dashboard_page = DashboardPage(self.driver)
        title = dashboard_page.get_page_title()
        assert "Dashboard" in title
        print(title)
        time.sleep(2)

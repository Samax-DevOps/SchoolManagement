import time

import pytest

from pageobjects.create_topic_page import CreateTopicPage
from pageobjects.dashboard_page import DashboardPage
from utilities.ConfigReader import read_configuration
from pageobjects.login_page import LoginPage


class Test_Create_Topic:

    def test_create_topic(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "teacheruser"),
                            read_configuration(self.environment, "teacherpassword"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_subject_lesson_tab()
        dashboard_page.click_on_create_topic_link()
        create_topic_page = CreateTopicPage(self.driver)
        create_topic_page.click_on_class_section_drpdwn()
        create_topic_page.select_class_section("7th Stars B - Telugu")
        create_topic_page.select_subject("Telugu Low (Theory)")
        create_topic_page.select_lesson("Demokjjsdsds")
        create_topic_page.enter_topic_name("DEMjk455")
        create_topic_page.enter_topic_description("Topis dedsdsh")
        create_topic_page.click_on_submit_btn()
        msg = create_topic_page.get_toast_msg()
        assert "Saved" in msg

    def test_delete_topic(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "teacheruser"),
                            read_configuration(self.environment, "teacherpassword"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_subject_lesson_tab()
        dashboard_page.click_on_create_topic_link()
        create_topic_page = CreateTopicPage(self.driver)
        create_topic_page.click_on_class_section_under_list_topic()
        create_topic_page.select_class_under_list_topic("7th Stars B - Telugu")
        create_topic_page.select_subject_under_list_topic("Telugu Low (Theory)")
        create_topic_page.click_on_delete_btn()
        create_topic_page.click_on_yes_delete_btn()
        msg = create_topic_page.get_toast_msg()
        assert "Delete" in msg

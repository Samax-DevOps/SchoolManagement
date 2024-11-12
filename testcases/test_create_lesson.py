import time

import pytest

from pageobjects.create_lesson_page import CreateLessonPage
from pageobjects.dashboard_page import DashboardPage
from utilities.ConfigReader import read_configuration
from pageobjects.login_page import LoginPage


class Test_Create_Lesson:

    def test_create_lesson(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "teacheruser"),
                            read_configuration(self.environment, "teacherpassword"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_subject_lesson_tab()
        dashboard_page.click_on_create_lesson_link()
        create_lesson_page = CreateLessonPage(self.driver)
        create_lesson_page.select_class("7th Stars B - Telugu")
        create_lesson_page.select_subject("Telugu Low (Theory)")
        create_lesson_page.enter_lesson_name('name')
        create_lesson_page.enter_lesson_description('des')
        create_lesson_page.click_on_submit_btn()
        msg = create_lesson_page.get_toast_msg()
        assert "Saved" in msg

    def test_create_lesson_with_attachment(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "teacheruser"),
                            read_configuration(self.environment, "teacherpassword"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_subject_lesson_tab()
        dashboard_page.click_on_create_lesson_link()
        create_lesson_page = CreateLessonPage(self.driver)
        create_lesson_page.select_class("7th Stars B - Telugu")
        create_lesson_page.select_subject("Telugu Low (Theory)")
        create_lesson_page.enter_lesson_name('name1dsds')
        create_lesson_page.enter_lesson_description('des')
        create_lesson_page.click_on_add_new_files_btn()
        time.sleep(1)
        create_lesson_page.select_file_type()
        create_lesson_page.enter_file_name('demo')
        create_lesson_page.upload_file()
        create_lesson_page.click_on_submit_btn()
        msg = create_lesson_page.get_toast_msg()
        assert "Saved" in msg

    # @pytest.mark.skip
    @pytest.mark.parametrize('execution_number', range(2))
    def test_delete_lesson(self, execution_number):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "teacheruser"),
                            read_configuration(self.environment, "teacherpassword"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_subject_lesson_tab()
        dashboard_page.click_on_create_lesson_link()
        create_lesson_page = CreateLessonPage(self.driver)
        create_lesson_page.click_on_list_lesson_class_section_drpdwn()
        create_lesson_page.select_class_from_list_lesson_drpdwn("7th Stars B - Telugu")
        # create_lesson_page.click_on_subject_drpdwn_list_lesson()
        create_lesson_page.select_subject_from_list_lesson_drpdwn2("Telugu Low (Theory)")
        time.sleep(3)
        create_lesson_page.click_on_delete_btn()
        create_lesson_page.click_on_yes_delete_btn()
        msg = create_lesson_page.get_toast_msg()
        assert "Deleted" in msg

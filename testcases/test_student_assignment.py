import time

import pytest

from pageobjects.dashboard_page import DashboardPage
from pageobjects.student_assignment_page import StudentAssignmentPage
from utilities.ConfigReader import read_configuration
from pageobjects.login_page import LoginPage
from TestData import DataUtil


class Test_Assignment:

    # @pytest.mark.parametrize("class_name, subject_name", DataUtil.dp2('test_create_timetable'))
    def test_create_assignment(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "teacheruser"),
                            read_configuration(self.environment, "teacherpassword"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_student_assignment_tab()
        dashboard_page.click_on_create_assignment_link()
        student_assignment_page = StudentAssignmentPage(self.driver)
        student_assignment_page.click_on_class_section_drpdwn()
        student_assignment_page.select_class_from_drpdwn("7th Stars B - Telugu")
        student_assignment_page.select_subject('Telugu Low (Theory)')
        student_assignment_page.enter_assignment_name('assign_name')
        student_assignment_page.enter_assignment_instructions('assign_instruct')
        student_assignment_page.click_on_last_submission_date()
        student_assignment_page.click_on_submit_btn()
        msg = student_assignment_page.get_toast_msg()
        assert "Saved" in msg

    # @pytest.mark.parametrize("class_name, subject_name", DataUtil.dp2('test_create_timetable'))
    def test_delete_assignment(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login(read_configuration(self.environment, "teacheruser"),
                            read_configuration(self.environment, "teacherpassword"))
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_student_assignment_tab()
        dashboard_page.click_on_create_assignment_link()
        student_assignment_page = StudentAssignmentPage(self.driver)
        student_assignment_page.delete_assignment()
        student_assignment_page.click_on_yes_delete_btn()
        msg = student_assignment_page.get_toast_msg()
        assert "Deleted" in msg

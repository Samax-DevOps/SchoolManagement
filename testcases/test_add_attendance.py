import time

from pageobjects.add_attendance_page import AddAttendancePage
from pageobjects.dashboard_page import DashboardPage
from utilities.ConfigReader import read_configuration
from pageobjects.login_page import LoginPage


class Test_Add_Attendance:

    def test_add_attendance(self):
        self.driver.get(read_configuration(self.environment, "url"))
        login_page = LoginPage(self.driver)
        login_page.do_login("rishab12@yopmail.com", "02031984")
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_attendance_tab()
        dashboard_page.click_on_add_attendance_link()
        add_attendance_page = AddAttendancePage(self.driver)
        add_attendance_page.click_on_select_class_drpdwn()
        add_attendance_page.select_class("12 C ( Commerce ) - English")
        add_attendance_page.click_on_date_picker()
        add_attendance_page.click_on_today_date()
        add_attendance_page.mark_present_absent()
        add_attendance_page.click_on_submit_btn()
        time.sleep(5)

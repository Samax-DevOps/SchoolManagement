import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class AddAttendancePage:
    select_class_drpdwn = "span#select2-timetable_class_section-container"
    class_list = "ul#select2-timetable_class_section-results > li"
    date_picker = "input#date"
    today_date = "div.datepicker-days > table > tbody > tr > td[class='today day']"
    student_list = "//table[@id='table_list']/tbody/tr[position() < last()]"
    # student_list = "//table[@id='table_list']/tbody/tr"
    submit_btn = "create-btn"

    def __init__(self, driver):
        self.driver = driver

    def click_on_select_class_drpdwn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.select_class_drpdwn).click()

    def select_class(self, class_name):
        eles = self.driver.find_elements(By.CSS_SELECTOR, self.class_list)
        for item in eles:
            if item.text == class_name:
                item.click()
                break

    def click_on_date_picker(self):
        self.driver.find_element(By.CSS_SELECTOR, self.date_picker).click()

    def click_on_today_date(self):
        self.driver.find_element(By.CSS_SELECTOR, self.today_date).click()

    def mark_present_absent(self):
        # time.sleep(2)
        eles = self.driver.find_elements(By.XPATH, self.student_list)
        for i in range(1, len(eles) + 2):
            c = 0
            if i % 2 == 0:
                c = 2
            else:
                c = 1
            self.driver.find_element(By.CSS_SELECTOR, "table#table_list > tbody > tr:nth-of-type(" + str(
                i) + ") > td:nth-of-type(5) > div > div:nth-of-type(" + str(c) + ")").click()

    def click_on_submit_btn(self):
        self.driver.find_element(By.ID, self.submit_btn).click()

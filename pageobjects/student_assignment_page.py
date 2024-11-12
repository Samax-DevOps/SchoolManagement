import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from utilities.utils import get_current_time, get_one_day_ahead_date


class StudentAssignmentPage:
    class_section_drpdwn = "select2-class-section-id-container"
    class_list = "ul#select2-class-section-id-results > li"
    subject_drpdwn = "select#subject-id"
    assignment_name_textbox = "input[placeholder='Assignment Name']"
    assignment_instructions_textbox = "textarea[placeholder='Assignment Instructions']"
    last_submission_date = "input#due_date"
    submit_btn = "#create-btn"
    toast_msg = "//div[@class='jq-toast-wrap top-right']"
    delete_btn = "//table[@id='table_list']/tbody/tr[1]/td[13]/a[2]"
    confirm_delete_btn = "//button[text()='Yes, delete it']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_class_section_drpdwn(self):
        self.driver.find_element(By.ID, self.class_section_drpdwn).click()

    def select_class_from_drpdwn(self, class_name):
        eles = self.driver.find_elements(By.CSS_SELECTOR, self.class_list)
        for item in eles:
            if item.text == class_name:
                item.click()
                break

    def select_subject(self, subject_name):
        subject_drpdwn = self.driver.find_element(By.CSS_SELECTOR, self.subject_drpdwn)
        select = Select(subject_drpdwn)
        select.select_by_visible_text(subject_name)

    def enter_assignment_name(self, name):
        self.driver.find_element(By.CSS_SELECTOR, self.assignment_name_textbox).send_keys(
            get_current_time() + ' ' + name)

    def enter_assignment_instructions(self, instructions):
        self.driver.find_element(By.CSS_SELECTOR, self.assignment_instructions_textbox).send_keys(
            get_current_time() + ' ' + instructions)

    def click_on_last_submission_date(self):
        cal_icon = self.driver.find_element(By.CSS_SELECTOR, self.last_submission_date)
        size = cal_icon.size
        location = cal_icon.location
        act = ActionChains(self.driver)
        # act.move_to_element_with_offset(cal_icon, size.get('width')*0.45, 2).click().perform()
        self.driver.execute_script("arguments[0].value='" + get_one_day_ahead_date() + "'",
                                   self.driver.find_element(By.CSS_SELECTOR, "input#due_date"))

    def click_on_submit_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.submit_btn).click()

    def get_toast_msg(self):
        return self.driver.find_element(By.XPATH, self.toast_msg).text

    def delete_assignment(self):
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element(By.XPATH, self.delete_btn)).click().perform()

    def click_on_yes_delete_btn(self):
        self.driver.find_element(By.XPATH, self.confirm_delete_btn).click()
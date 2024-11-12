import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from utilities.utils import get_root_of_project


class CreateLessonPage:
    class_section_drpdwn = "#select2-class-section-id-container"
    class_section_list = "ul#select2-class-section-id-results > li"
    subject_drpdwn = "select#subject-id"
    lesson_name_box = "input#name"
    lesson_description_box = "textarea#description"
    submit_btn = "input#create-btn"
    class_section_list_lesson_drpdwn = "span#select2-filter-class-section-id-container"
    class_section_list_lesson_list = "ul#select2-filter-class-section-id-results > li"
    subject_drpdwn_list_lesson_section = "span#select2-filter-subject-id-container"
    subject_list_lesson_list = "ul#select2-filter-subject-id-results > li"
    delete_btn = "table#table_list > tbody >tr:first-of-type > td:nth-of-type(7) > a:last-of-type"
    confirm_delete_btn = "//button[text()='Yes, delete it']"
    toast_msg = "//div[@class='jq-toast-wrap top-right']"
    add_new_files_btn = "button.add-lesson-topic-file"
    file_type_drpdwn = "select#file_type"
    file_name_textbox = "input[placeholder='File Name']"
    choose_file_button = "#file_div > input[type='file']"
    subject_list_lesson_list2 = "#filter-subject-id"

    def __init__(self, driver):
        self.driver = driver

    def select_class(self, class_name):
        self.driver.find_element(By.CSS_SELECTOR, self.class_section_drpdwn).click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, self.class_section_list)
        for item in eles:
            if item.text == class_name:
                item.click()
                break

    def select_subject(self, subject_name):
        subject_drpdwn = self.driver.find_element(By.CSS_SELECTOR, self.subject_drpdwn)
        select = Select(subject_drpdwn)
        select.select_by_visible_text(subject_name)

    def enter_lesson_name(self, name):
        self.driver.find_element(By.CSS_SELECTOR, self.lesson_name_box).send_keys(name)

    def enter_lesson_description(self, description):
        self.driver.find_element(By.CSS_SELECTOR, self.lesson_description_box).send_keys(description)

    def click_on_submit_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.submit_btn).click()

    def click_on_list_lesson_class_section_drpdwn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.class_section_list_lesson_drpdwn).click()

    def select_class_from_list_lesson_drpdwn(self, class_name):
        eles = self.driver.find_elements(By.CSS_SELECTOR, self.class_section_list_lesson_list)
        for item in eles:
            if item.text == class_name:
                item.click()
                break

    def click_on_subject_drpdwn_list_lesson(self):
        self.driver.find_element(By.CSS_SELECTOR, self.subject_drpdwn_list_lesson_section).click()

    def select_subject_from_list_lesson_drpdwn(self, subject_name):
        eles = self.driver.find_elements(By.CSS_SELECTOR, self.subject_list_lesson_list)
        for item in eles:
            if item.text == subject_name:
                item.click()
                break

    def select_subject_from_list_lesson_drpdwn2(self, subject_name):
        select = Select(self.driver.find_element(By.CSS_SELECTOR, self.subject_list_lesson_list2))
        select.select_by_visible_text(subject_name)

    def click_on_delete_btn(self):
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element(By.CSS_SELECTOR, self.delete_btn)).click().perform()

    def click_on_yes_delete_btn(self):
        self.driver.find_element(By.XPATH, self.confirm_delete_btn).click()

    def get_toast_msg(self):
        return self.driver.find_element(By.XPATH, self.toast_msg).text

    def click_on_add_new_files_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add_new_files_btn).click()

    def select_file_type(self):
        select = Select(self.driver.find_element(By.CSS_SELECTOR, self.file_type_drpdwn))
        select.select_by_visible_text('File Upload')

    def enter_file_name(self, name):
        self.driver.find_element(By.CSS_SELECTOR, self.file_name_textbox).send_keys(name)

    def upload_file(self):
        self.driver.find_element(By.CSS_SELECTOR, self.choose_file_button).send_keys(
            str(get_root_of_project()) + "/TestData/assi.pdf")

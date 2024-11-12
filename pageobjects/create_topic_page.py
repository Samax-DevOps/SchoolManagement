import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class CreateTopicPage:
    class_section_drpdwn = "select2-class-section-id-container"
    class_section_values = "#select2-class-section-id-results >li"
    subject_drpdwn = "select#subject-id"
    lesson_drp_dwn = "select#topic-lesson-id"
    topic_name_box = "input#name"
    topic_description_box = "textarea#description"
    submit_btn = "create-btn"
    toast_msg = "//div[@class='jq-toast-wrap top-right']"
    class_Section_drp_under_list_topic = "select2-filter-class-section-id-container"
    class_list_under_list_topic = "ul#select2-filter-class-section-id-results > li"
    subject_values_under_list_topic = "filter-subject-id"
    delete_btn = "table#table_list > tbody > tr:first-of-type > td:nth-of-type(8) > a:last-of-type"
    confirm_delete_btn = "//button[text()='Yes, delete it']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_class_section_drpdwn(self):
        self.driver.find_element(By.ID, self.class_section_drpdwn).click()

    def select_class_section(self, class_name):
        eles = self.driver.find_elements(By.CSS_SELECTOR, self.class_section_values)
        for item in eles:
            if item.text == class_name:
                item.click()
                break

    def select_subject(self, subject):
        select = Select(self.driver.find_element(By.CSS_SELECTOR, self.subject_drpdwn))
        select.select_by_visible_text(subject)

    def select_lesson(self, lesson):
        select = Select(self.driver.find_element(By.CSS_SELECTOR, self.lesson_drp_dwn))
        select.select_by_visible_text(lesson)

    def enter_topic_name(self, name):
        self.driver.find_element(By.CSS_SELECTOR, self.topic_name_box).send_keys(name)

    def enter_topic_description(self, description):
        self.driver.find_element(By.CSS_SELECTOR, self.topic_description_box).send_keys(description)

    def click_on_submit_btn(self):
        self.driver.find_element(By.ID, self.submit_btn).click()

    def get_toast_msg(self) -> str:
        return self.driver.find_element(By.XPATH, self.toast_msg).text

    def click_on_class_section_under_list_topic(self):
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element(By.ID, self.class_Section_drp_under_list_topic)).click().perform()

    def select_class_under_list_topic(self, class_name):
        eles = self.driver.find_elements(By.CSS_SELECTOR, self.class_list_under_list_topic)
        for item in eles:
            if item.text == class_name:
                item.click()
                break

    def select_subject_under_list_topic(self, subject):
        select = Select(self.driver.find_element(By.ID, self.subject_values_under_list_topic))
        select.select_by_visible_text(subject)

    def click_on_delete_btn(self):
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element(By.CSS_SELECTOR, self.delete_btn)).click().perform()

    def click_on_yes_delete_btn(self):
        self.driver.find_element(By.XPATH, self.confirm_delete_btn).click()

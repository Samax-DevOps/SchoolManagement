import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        
        # Explicit wait for toast message
        msg = WebDriverWait(self.driver, 10).until(
            lambda driver: create_topic_page.get_toast_msg()
        )
        assert "Saved" in msg or "Topic is already exists" in msg  # Adjusted to handle both outcomes

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
        
        # Wait until delete button is clickable
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Delete')]"))
        )
        delete_button.click()
        
        # Confirm deletion with explicit wait
        confirm_delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Yes, delete it']"))
        )
        confirm_delete_button.click()
        
        # Wait for deletion toast message
        msg = WebDriverWait(self.driver, 10).until(
            lambda driver: create_topic_page.get_toast_msg()
        )
        assert "Delete" in msg

from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    email_box = "email"
    password_box = "password"
    login_btn = "login_btn"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_box).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_box).send_keys(password)

    def click_on_login_btn(self):
        self.driver.find_element(By.ID, self.login_btn).click()

    def do_login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_login_btn()

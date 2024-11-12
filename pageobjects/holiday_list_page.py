import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HolidayListPage:
    date_field = "(//input[@placeholder='Date'])[1]"
    today_day = "//td[@class='today day']"
    title_field = "(//input[@placeholder='Title'])[1]"
    description_box = "(//textarea[@placeholder='Description'])[1]"
    reset_btn = "//input[@value='Reset']"
    submit_btn = "//input[@value='Submit']"
    toast_msg = "//div[@class='jq-toast-wrap top-right']"
    delete_btn = "//a[@title='Delete']"
    confirm_delete_btn = "//button[text()='Yes, delete it']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_date_field(self):
        self.driver.find_element(By.XPATH, self.date_field).click()

    def click_on_today_day(self):
        self.driver.find_element(By.XPATH, self.today_day).click()

    def enter_title(self, title):
        self.driver.find_element(By.XPATH, self.title_field).click()
        self.driver.find_element(By.XPATH, self.title_field).send_keys(title)

    def enter_description(self, description):
        self.driver.find_element(By.XPATH, self.description_box).send_keys(description)

    def click_on_reset_btn(self):
        self.driver.find_element(By.XPATH, self.reset_btn).click()

    def click_on_submit_btn(self):
        self.driver.find_element(By.XPATH, self.submit_btn).click()

    def get_toast_msg(self):
        return self.driver.find_element(By.XPATH, self.toast_msg).text

    def delete_holiday(self):
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element(By.XPATH, self.delete_btn)).click().perform()

    def click_on_yes_delete_btn(self):
        self.driver.find_element(By.XPATH, self.confirm_delete_btn).click()
        time.sleep(2)

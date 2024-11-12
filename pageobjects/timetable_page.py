import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TimetablePage:
    date_field = "(//input[@placeholder='Date'])[1]"
    today_day = "//td[@class='today day']"
    timetable_row = "//table[@id='table_list']/tbody/tr/td[2]"
    subject_card = "//div[@id='external-events']/div/div"
    sx = "//td[2][@data-time = '12:30:00']"
    day_row = "(//div[@class='fc-timegrid-slots']/table/tbody/tr/td[2])[1]"
    cross_btn = "//div[@class='fc-event-title fc-sticky']/../following-sibling::div[1]/span"
    confirm_delete_btn = "//button[text()='Yes, delete it']"
    toast_msg = "//div[@class='jq-toast-wrap top-right']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_edit_button(self, class_name):
        eles: list = self.driver.find_elements(By.XPATH, self.timetable_row)
        for item in range(0, len(eles)):
            # text = eles[item].find_element(By.XPATH, "//td[2]").text
            text = eles[item].text
            if text == class_name:
                # item.find_element(By.XPATH, "//td[10]/a[1]").click()
                ele = self.driver.find_element(By.XPATH,
                                               "//table[@id='table_list']/tbody/tr[" + str(item + 1) + "]/td[10]/a[1]")
                act = ActionChains(self.driver)
                act.move_to_element(ele).click().perform()
                break

    def drag_subject_to_day_and_time(self, subj):
        eles = self.driver.find_elements(By.XPATH, self.subject_card)
        for i in eles:
            text = i.text
            if subj in text:
                act = ActionChains(self.driver)
                ele = self.driver.find_element(By.XPATH, self.day_row)
                ele_size = ele.size
                height = ele_size.get("height")
                width = ele_size.get("width")
                distributed_width = width / 7
                ele_location = ele.location
                x_cor = ele_location.get("x")
                y_cor = ele_location.get("y")

                source_location = i.location
                source_x_cor = source_location.get("x")
                source_y_cor = source_location.get("y")
                act.drag_and_drop_by_offset(i, (x_cor + (distributed_width / 2) * 10) - source_x_cor,
                                            (y_cor + 0) - source_y_cor - 5).perform()
                break

    def delete_time_table(self):
        eles = self.driver.find_elements(By.XPATH, self.cross_btn)
        for i in eles:
            i.click()
            self.driver.find_element(By.XPATH, self.confirm_delete_btn).click()

    def get_toast_msg(self):
        return self.driver.find_element(By.XPATH, self.toast_msg).text

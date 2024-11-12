from selenium.webdriver.common.by import By


class DashboardPage:
    title = "//h3[@class='page-title']"
    holiday_list_tab = "//span[text()='Holiday List']"
    timetable_tab = "//a[@href='#timetable-menu']"
    create_timetable = "//a[normalize-space() ='Create Timetable']"
    student_assignment_tab = "a[href*=student-assignment]"
    create_assignment_link = "//a[normalize-space()='Create Assignment']"
    subject_lesson_tab = "a[href*=subject-lesson-menu]"
    create_lesson_link = "//a[text()=' Create Lesson']"
    attendance_tab = "a[href*='attendance-menu']"
    add_attendance_link = "//a[normalize-space()='Add Attendance']"
    create_topic_link = "//a[normalize-space()='Create Topic']"

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.find_element(By.XPATH, self.title).text

    def click_on_holiday_list_tab(self):
        self.driver.find_element(By.XPATH, self.holiday_list_tab).click()

    def click_on_create_timetable(self):
        self.driver.find_element(By.XPATH, self.timetable_tab).click()
        self.driver.find_element(By.XPATH, self.create_timetable).click()

    def click_on_student_assignment_tab(self):
        self.driver.find_element(By.CSS_SELECTOR, self.student_assignment_tab).click()

    def click_on_create_assignment_link(self):
        self.driver.find_element(By.XPATH, self.create_assignment_link).click()

    def click_on_subject_lesson_tab(self):
        self.driver.find_element(By.CSS_SELECTOR, self.subject_lesson_tab).click()

    def click_on_create_lesson_link(self):
        self.driver.find_element(By.XPATH, self.create_lesson_link).click()

    def click_on_attendance_tab(self):
        self.driver.find_element(By.CSS_SELECTOR, self.attendance_tab).click()

    def click_on_add_attendance_link(self):
        self.driver.find_element(By.XPATH, self.add_attendance_link).click()

    def click_on_create_topic_link(self):
        self.driver.find_element(By.XPATH, self.create_topic_link).click()

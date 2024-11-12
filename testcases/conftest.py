import sys
from datetime import datetime

import pytest
from selenium import webdriver
from Configurations import environmentConfig
import chromedriver_autoinstaller


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            file_name = "screenshot_" + test_name1 + ".png"
            # _capture_screenshot(file_name)
            driver.save_screenshot(sys.path[0] + "/Reports/" + file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    return report


@pytest.fixture(autouse=True)
def setup(browser, environment, request):
    global test_name1
    test_name1 = str(request.node.name)
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        chromedriver_autoinstaller.install()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)

    if environment == 'staging':
        environmentConfig.environment = 'staging'
    elif environment == 'production':
        environmentConfig.environment = 'production'
    else:
        environment = 'production'
        environmentConfig.environment = 'production'
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.environment = environment


@pytest.fixture(autouse=True)
def tear_down():
    yield
    if driver is not None:
        driver.close()


def pytest_addoption(parser):  # This will get ṭhe value from CLI /hooks
    parser.addoption("--browser")  # We can pass multiple parameters
    parser.addoption("--environment")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  # This will return the browser value to setup method


@pytest.fixture()
def environment(request):
    return request.config.getoption("--environment")  # This will return the environment value to setup method

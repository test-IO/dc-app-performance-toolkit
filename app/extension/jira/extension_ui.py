import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_accept_testio_bug(webdriver):
    page = BasePage(webdriver)
    project_key = 'AANES'
    page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/{project_key}/test-io-issues")
    @print_timing("selenium_app_accept_testio_bug")
    def measure():
        @print_timing("selenium_app_accept_testio_bug:accept_testio_bug")
        def sub_measure():
            page.wait_until_visible((By.XPATH, "//div[contains(@class, 'test-io-accept-button')]"), 60).click()  # Accept testio bug
        sub_measure()
    measure()

def app_change_severity_testio_bug(webdriver):
    page = BasePage(webdriver)
    project_key = 'AANES'
    page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/{project_key}/test-io-issues")
    @print_timing("selenium_app_change_severity_testio_bug")
    def measure():
        @print_timing("selenium_app_change_severity_testio_bug:change_testio_bug_severity")
        def sub_measure():
            page.wait_until_visible((By.ID, "test-io-change-severity-button"), 60).click()  # Change testio bug severity
            page.wait_until_visible((By.ID, "new-severity-selector-input"), 60).click()
            page.wait_until_visible((By.CLASS_NAME, "aui-select-suggestion"), 60).click()
            page.wait_until_visible((By.ID, "change_issue_severity_submit"), 60).click()
        sub_measure()
    measure()

def view_testio_specific_bug(webdriver):
    page = BasePage(webdriver)
    project_key = 'AANES'
    issue_key = 1
    @print_timing("selenium_app_custom_action:view_testio_bugs")
    def sub_measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/{project_key}/test-io-issues")
        page.wait_until_visible((By.CLASS_NAME, "test-io-issue"), 60)  # Wait for you test-io-issues-list UI element by ID selector
    sub_measure()

    @print_timing("selenium_app_custom_action:open_specific_testio_bug")
    def sub_measure():
        page.wait_until_visible((By.CLASS_NAME, "test-io-issue"), 60).click()  # Open specific testio bug
    sub_measure()


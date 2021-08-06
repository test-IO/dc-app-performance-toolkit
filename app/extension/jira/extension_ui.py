import random

from selenium.webdriver.common.by import By
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS

def app_accept_testio_bug(webdriver):
    page = BasePage(webdriver)
    project_key = 'UOO'
    page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/{project_key}/test-io-issues")
    @print_timing("selenium_app_accept_testio_bug")
    def measure():
        @print_timing("selenium_app_accept_testio_bug:accept_testio_bug")
        def sub_measure():
            page.wait_until_visible((By.ID, "test-io-accept-button")).click()  # Accept testio bug
        sub_measure()
    measure()

def app_reject_testio_bug(webdriver):
    page = BasePage(webdriver)
    project_key = 'UOO'
    page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/{project_key}/test-io-issues")
    @print_timing("selenium_reject_testio_bug")
    def measure():
        @print_timing("selenium_reject_testio_bug:reject_testio_bug")
        def sub_measure():
            page.wait_until_visible((By.ID, "test-io-reject-button")).click()  # Reject testio bug
        sub_measure()
    measure()

def app_change_severity_testio_bug(webdriver):
    page = BasePage(webdriver)
    project_key = 'UOO'
    page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/{project_key}/test-io-issues")
    @print_timing("selenium_app_change_severity_testio_bug")
    def measure():
        @print_timing("selenium_app_change_severity_testio_bug:change_testio_bug_severity")
        def sub_measure():
            page.wait_until_visible((By.ID, "test-io-change-severity-button")).click()  # Change testio bug severity
            page.wait_until_visible((By.ID, "new-severity-selector-input")).click()
            page.wait_until_visible((By.CLASS_NAME, "aui-select-suggestion")).click()
            page.wait_until_visible((By.ID, "change_issue_severity_submit")).click()
        sub_measure()
    measure()

def view_testio_specific_bug(webdriver):
    page = BasePage(webdriver)
    project_key = 'UOO'
    issue_key = 1
    @print_timing("selenium_app_custom_action:view_testio_bugs")
    def sub_measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/{project_key}/test-io-issues")
        page.wait_until_visible((By.CLASS_NAME, "test-io-issue"))  # Wait for you test-io-issues-list UI element by ID selector
    sub_measure()

    @print_timing("selenium_app_custom_action:open_specific_testio_bug")
    def sub_measure():
        page.wait_until_visible((By.CLASS_NAME, "test-io-issue")).click()  # Open specific testio bug
    sub_measure()
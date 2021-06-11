import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS

def app_accept_testio_bug(webdriver, datasets):
    page = BasePage(webdriver)
    project_key = datasets['project_key']
    issue_key = datasets['custom_issue_key']

    @print_timing("selenium_app_accept_testio_bug")
    def measure():
        view_testio_specific_bug(page, project_key, issue_key)

        @print_timing("selenium_app_accept_testio_bug:accept_testio_bug")
        def sub_measure():
            page.wait_until_visible((By.CLASS_NAME, ".test-io-accept-button")).click()  # Accept testio bug
        sub_measure()
    measure()

def app_reject_testio_bug(webdriver, datasets):
    page = BasePage(webdriver)
    project_key = datasets['project_key']
    issue_key = datasets['custom_issue_key']

    @print_timing("selenium_reject_testio_bug")
    def measure():
        view_testio_specific_bug(page, project_key, issue_key)

        @print_timing("selenium_reject_testio_bug:reject_testio_bug")
        def sub_measure():
            page.wait_until_visible((By.CLASS_NAME, ".test-io-reject-button")).click()  # Reject testio bug
        sub_measure()
    measure()

def app_change_severity_testio_bug(webdriver, datasets):
    page = BasePage(webdriver)
    project_key = datasets['project_key']
    issue_key = datasets['custom_issue_key']

    @print_timing("selenium_app_change_severity_testio_bug")
    def measure():
        view_testio_specific_bug(page, project_key, issue_key)

        @print_timing("selenium_app_change_severity_testio_bug:change_testio_bug_severity")
        def sub_measure():
            page.wait_until_visible((By.CLASS_NAME, ".test-io-reject-button")).click()  # Change testio bug severity
        sub_measure()
    measure()

def app_testio_bug_fix_confirmation(webdriver, datasets):
    page = BasePage(webdriver)
    project_key = datasets['project_key']
    issue_key = datasets['custom_issue_key']

    @print_timing("selenium_app_testio_bug-fix_confirmation")
    def measure():
        @print_timing("selenium_app_custom_action:view_bug")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/{project_key}/issues/{issue_key}/external-bug-fix-confirmation")
            page.wait_until_visible((By.CLASS_NAME, "issueaction-workflow-transition")).click()
            page.wait_until_visible((By.ID, "external-bug-fix-confirmation"))
        sub_measure()

        @print_timing("selenium_app_accept_testio_bug:open_external_confirmation")
        def sub_measure():
            page.wait_until_visible((By.ID, "external-bug-fix-confirmation")).click()
            page.wait_until_visible((By.ID, "confirm-issue-fix-form"))  # Accept testio bug
        sub_measure()

        page.wait_until_visible((By.ID, "select-products")).selectByIndex(1)
        page.wait_until_visible((By.ID, "select-environments")).selectByIndex(1)

        @print_timing("selenium_app_accept_testio_bug:submit_external_confirmation_dialog")
        def sub_measure():
            page.wait_until_visible((By.ID, "submit-bug-fix-confirmation")).click()
            page.wait_until_visible((By.ID, "bug-fix-confirm-dialog"))
        sub_measure()

        @print_timing("selenium_app_accept_testio_bug:submit_external_confirmation")
        def sub_measure():
            page.wait_until_visible((By.ID, "confirm-issue-fix-dialog-submit")).click()
            page.wait_until_visible((By.ID, "bug-fix-confirm-dialog"))
        sub_measure()
    measure()

def view_testio_specific_bug(page, project_key, issue_key):
    @print_timing("selenium_app_custom_action:view_testio_bugs")
    def sub_measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/{project_key}/test-io-issues")
        page.wait_until_visible((By.ID, "test-io-issues-list"))  # Wait for you test-io-issues-list UI element by ID selector
    sub_measure()

    @print_timing("selenium_app_custom_action:open_specific_testio_bug")
    def sub_measure():
        page.wait_until_visible((By.ID, f"{issue_key}")).click()  # Open specific testio bug
        page.wait_until_visible((By.LINK_TEXT, f"{issue_key}"))
    sub_measure()
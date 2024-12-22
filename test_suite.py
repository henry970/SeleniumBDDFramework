# features/steps/login_steps.py

from behave import given, when, then
from selenium import webdriver

from LoginAction.loginActionPage import LoginPageActions


@given('the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/')
    context.login_actions = LoginPageActions(context.driver)

@when('the user enters "{username}" and "{password}"')
def step_impl(context):
    context.login_actions.enter_username("standard_user")
    context.login_actions.enter_password("secret_sauce")
    context.login_actions.click_login_button()

@then('the user should be redirected to the dashboard page')
def step_impl(context):
    assert "Dashboard" in context.driver.title
    context.driver.quit()

@then('the user should see an error message')
def step_impl(context):
    error_message = context.login_actions.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    context.driver.quit()

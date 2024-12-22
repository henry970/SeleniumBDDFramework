# features/login.feature

Feature: Login functionality

  Scenario: User logs in with valid credentials
    Given the user is on the login page
    When the user enters "testuser" and "password123"
    Then the user should be redirected to the dashboard page

  Scenario: User logs in with invalid credentials
    Given the user is on the login page
    When the user enters "invaliduser" and "wrongpassword"
    Then the user should see an error message

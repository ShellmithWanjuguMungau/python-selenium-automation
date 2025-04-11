# Created by USER at 18/03/2025
Feature: Login & signin feature

  Scenario: Logged out user can signin
    Given open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify "Sign in or create account" message is shown



 Scenario: User can open and close Terms and Conditions from sign in page
   Given open target main page
   And Click Sign In
   And From right side navigation menu, click Sign In
   And enter test email
   And click continue to the signin page
   And Store original window
   When Click on terms and conditions link
   And Switch to new window
   Then Verify Terms and Conditions page is opened
   And Close current page
   And Return to original window

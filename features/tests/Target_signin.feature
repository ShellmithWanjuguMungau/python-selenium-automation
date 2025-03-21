# Created by USER at 18/03/2025
Feature: Login & signin feature

  Scenario: Logged out user can signin
    Given open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened

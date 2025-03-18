# Created by USER at 18/03/2025
Feature: user logged user can signin

  Scenario: Logged out user can signin
    Given Open target.com
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened

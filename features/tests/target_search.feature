# Created by USER at 17/03/2025
Feature: Jumia search testcases

  Scenario: User can search for a product on Jumia
    Given Open Jumia main page
    And Close newsletter popup
    When Search for books
    Then Verify correct results shown

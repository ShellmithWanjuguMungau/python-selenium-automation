# Created by USER at 18/03/2025
Feature: Cart feature

  Scenario: users cart is empty
    Given open target main page
    When click on Cart icon
    Then verify “Your cart is empty” message is shown
    And verify cart page opens


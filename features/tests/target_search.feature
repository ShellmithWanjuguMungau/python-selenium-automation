# Created by USER at 17/03/2025

Feature: Target search test cases

#  Scenario: User can search for a product on Target
#    Given Open target main page
#    When Search for tea
#    Then Verify correct search results for tea


  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search results for <expected_result>
    Examples:
    |search_word  |expected_result |
    |cup          |for “cup”       |
    |shoe         |for “shoe”      |
    |tea          |for “tea”       |






#Feature: Jumia /target search testcases
#  Scenario: User can search for a product on Jumia
#    Given Open Jumia main page
#    And Close newsletter popup
#    When Search for books
#    Then Verify correct results shown


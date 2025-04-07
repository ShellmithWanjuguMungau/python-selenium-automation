# Created by USER at 20/03/2025
  #3. Create a test case to add any Target’s product into the
# cart, and make sure it’s there (check that your cart has individual
# cart items OR the total price, up to you!)
Feature: Add to cart feature

  Scenario Outline: verify that product is added to cart
    Given open target main page
    When  search for <search_word>
    When click on add to cart button
#    And Store product name
    When click add to cart from side navigation
    Then verify "Added to cart" message is shown
#    When click on view cart and checkout
#    Then verify cart has correct product
#    Then verify <expected_product> is  added to cart

    Examples:
    |search_word                                  |expected_product                            |
    |30ct Cutlery Set Gold - Spritz™              |30ct Cutlery Set Gold - Spritz™             |
#    |Hefty Party On! Disposable Cups - 80ct/16oz  |Hefty Party On! Disposable Cups - 80ct/16oz |
#    |Paper Mate Clearpoint Color 6/Cd             |Paper Mate Clearpoint Color 6/Cd            |
#    |Kendra Scott Anna Band Ring                  |Kendra Scott Anna Band Ring                 |


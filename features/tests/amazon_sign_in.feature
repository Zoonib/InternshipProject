Feature:   Test for sign in

Scenario:  Verify that a user can click on orders
    Given Open Amazon page
    When Click on orders
    Then Verify Sign in text is Sign in

Scenario: Verify that a user can click on shopping cart
    Given Open Amazon page
    When Click on shopping cart icon
    Then Verify cart result is Your Amazon Cart is empty
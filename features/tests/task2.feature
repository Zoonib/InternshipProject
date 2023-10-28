Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can filter the Secondary deals by Unit price range

  Given Open main page
  When Log in to the page
  And Click on Secondary option at the left side menu.
  Then Verify the right page opens
  And Filter the products by price range from 1200000 to 2000000.
  Then Verify the price in all cards is inside the range 1200000 to 2000000.
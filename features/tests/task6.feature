Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can filter the Secondary deals by Unit price range on mobile

  Given Open main page on mobile
  When  Log in to the page on mobile
  And Click on Filter button
  And Input amount 1200000 to 2000000
  Then Verify amount 1200000 to 200000
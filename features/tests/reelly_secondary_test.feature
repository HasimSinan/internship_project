# Created by HSM at 3/18/2024
Feature: UI Tests for reelly.com secondary page
  # Enter feature description here

  Scenario: User can filter the Secondary deals by “want to buy” option
    Given Open the main page.
    When Log in to the page.
    When Click on secondary option.
    Then Verify the secondary page opens.
    When Filter the products by want to buy.
    Then Verify all cards have “want to buy” tag.
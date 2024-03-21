# Created by HSM at 3/13/2024
Feature: UI Tests for reelly.com community Page
  # Enter feature description here

  Scenario: User can open the community page
    Given Open the main page.
    When Log in to the page.
    When Click on settings option.
    When Click on Community option.
    Then Verify the right page opens.
    Then Verify “Contact support” button is available and clickable.
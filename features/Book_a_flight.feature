Feature: Register

Scenario: Success submit
    Given Go to Mercury Tours site
    When Click on Register tab
    And Fill out all required fields
    And Click Submit
    Then Verify that submit is successful
Feature: Register

Scenario: Success submit
    Given Go to Mercury Tours site
    When Click on Register tab
    And Fill out all required fields with valid credentials
    And Click Submit
    Then Verify that submit is successful

Scenario: Unsuccessful sign-in
    Given Click on sign-in link
    When Fill out username and password with error credentials
    And Click Submit
    Then Verify that login is unsuccessful

Scenario: Successful sign-in
    Given Click on sign-in link
    When Fill out username and password with valid credentials
    And Click Submit
    Then Verify that login is successful

Scenario: Flight finder
    When Fill in Flight Details and Preferences
    And Click Submit
    Then Verify that page with listed flights is showing

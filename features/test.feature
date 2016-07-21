# Created by onikiforov at 7/21/16
Feature: Test feature

  Scenario: Test scenario to get list of users
    Given I set base URL to "context.staging_url"
    And I set "Accept" header to "application/json"
    When I make a GET request to "users"
    Then the response status code should equal 200
    And the response status message should equal "OK"
    And the response header "Content-Type" should equal "application/json; charset=utf-8"
    And the response structure should equal "usersData"
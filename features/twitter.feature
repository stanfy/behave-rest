# Created by onikiforov at 7/26/16
Feature: Twitter search

  Background: Setup environment
    Given I set base URL to "https://api.twitter.com/1.1/search"
    And I set "Authorization" header to "context.twitter_auth"
  
  Scenario: Search for tweets
    When I make a GET request to "tweets.json" with parameters
    |q|
    |stanfy|
    Then the response status code should equal 200
    And the response structure should equal "twitterSearchData"
    And the response header "status" should equal "200 OK"
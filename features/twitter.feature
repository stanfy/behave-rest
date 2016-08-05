# Created by onikiforov at 7/26/16
Feature: Twitter API tests

  Background: Setup environment
    Given I set base URL to "https://api.twitter.com/1.1"
    And I set "Authorization" header to "context.twitter_auth"

  @search @twitter
  Scenario: Search for tweets
    When I make a GET request to "search/tweets.json" with parameters
    |q|
    |stanfy|
    Then the response status code should equal 200
    And the response status code should be among 200, 201
    And the response structure should equal "twitterSearchData"
    And the response header "status" should equal "200 OK"

   @tweets @twitter
   Scenario: Get my tweets
     When I make a GET request to "statuses/user_timeline.json" with parameters
     |screen_name|
     |ddr3ams    |
     Then the response status code should equal 200
     And the response structure should equal "twitterUserTimelineData"
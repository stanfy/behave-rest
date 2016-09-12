# Created by onikiforov at 7/21/16
Feature: Test feature

  Background: Set base url and headers
    Given I set base URL to "context.staging_url"
    And I set "Accept" header to "application/json"

  @test
  Scenario: Test scenario to get list of users
    When I make a GET request to "users"
    Then the response status code should equal 200
    And the response status message should equal "OK"
    And the response header "Content-Type" should equal "application/json; charset=utf-8"
    And the response structure should equal "usersData"

  @test
  Scenario: Compare different objects
    Given I set base URL to "http://www.mocky.io/v2"
    And I make a GET request to "57b6d6740f00000e0a0b7a5a"
    Then the response parameter "array" should equal [1,2,3]
    And the response parameter "boolean" should equal true
    And the response parameter "null" should equal null
    And the response parameter "int" should equal 123
    And the response parameter "object" should equal {"a": "b", "c": "d", "e": "f"}
    And the response parameter "string" should equal "Hello World"
    And the response parameter "float" should equal 3.0
    And the response parameter "long" should equal 9223372036854775808

  @test @json_path
  Scenario: Compare different objects providing path
    Given I set base URL to "http://www.mocky.io/v2"
    And I make a GET request to "57b6d6740f00000e0a0b7a5a"
    Then JSON at path ".data.array" should equal [1,2,3]
    Then JSON at path ".data.boolean" should equal true
    Then JSON at path ".data.null" should equal null
    Then JSON at path ".data.object" should equal {"a": "b", "c": "d", "e": "f"}
    Then JSON at path ".data.string" should equal "Hello World"
    Then JSON at path ".data.numbers.int" should equal 123
    Then JSON at path ".data.numbers.float" should equal 3.0
    Then JSON at path ".data.numbers.long" should equal 9223372036854775808
    Then JSON at path ".data.numbers" should equal {"int": 123, "float": 3.0, "long": 9223372036854775808}

   @test @baseurl
     Scenario: Test adding path to baseurl
     Given I set base URL to "context.base_url"
     And I add path "v2" to base URL
     Then I want to print it

   @test @param
     Scenario: Test storing parameter with specified path
      Given I set base URL to "http://www.mocky.io/v2"
      And I make a GET request to "57b6d6740f00000e0a0b7a5a"
      Then I want to reuse parameter "long" at path ".data.numbers.long"
      And JSON at path ".data.numbers.long" should equal context.long
      And the response parameter "long" should equal context.long
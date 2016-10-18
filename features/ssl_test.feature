# Created by onikiforov at 10/17/16
Feature: #Enter feature name here
  # Enter feature description here

    Background: Set base url and headers
    Given I set base URL to "https://expired.badssl.com"

  @test @ssl @fail
  Scenario: # Test ssl error
    Given I make a GET request to "/"

  @test @ssl
  Scenario: # Test request without ssl validation
    Given I make an untrusted GET request to "/"
    Then the response status code should equal 200

  @test @ssl
  Scenario: # Test parametrized request without ssl validation
    Given I make an untrusted GET request to "/" with parameters
    |param|
    |value|
    Then the response status code should equal 200

  @test @ssl
  Scenario: # Test turning off global SSL check
    Given I do not want to verify SSL certs
    When I make a GET request to "/"
    Then the response status code should equal 200

  @test @ssl @fail
  Scenario: # Test turning on global SSL check
    Given I want to verify SSL certs
    When I make a GET request to "/"
# behave-rest

BDD-style Rest API testing tool

It uses python's requests (https://pypi.python.org/pypi/requests/) for performing HTTP requests, nose (https://pypi.python.org/pypi/nose/1.3.7) for most assertions, trafaret (https://github.com/Deepwalker/trafaret) for json validation and behave (https://pypi.python.org/pypi/behave/1.2.5) for BDD style of tests.

## Installation
Clone project

Run `pip install -r requirements.txt` to install required dependencies

## Running

```bash
# to execute all feature files (all tests)
behave

# to execture specific feature
behave features/twitter.feature

# to see printed output add --no-capture
behave --no-capture

# run features with specific tags
behave --tags=without_login --tags=slow

```
More about behave tool you can read here https://pythonhosted.org/behave/index.html

## Test example
```cucumber
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
```

## CI reports
Behave support JUnit reports, that are easily parsed by CI tools

To enable JUnit reports, create `behave.ini` file:
```
[behave]
junit=true
```
Reports are generated into `/reports` folder

Another useful options to add into `behave.ini` are:

`stdout_capture=False` to add printed output into reports

`show_timings=no` to hide timing of each step

## Project Structure

Feature files are intended to locate in `/features` folder

Corresponding steps are located in `/features/steps`

Overall project structure is as follows:

```
+-- requirements.txt // store python requirements

+-- behave_rest/
    
    +-- environment.py // contains common actions related to scenarios (e.g. clearting headers after running each feature file)

    +-- steps/

        +-- __init__.py // contains common steps definitions

+-- features/

    +-- conf.yaml // store project config (urls, global variables, etc.)

    +-- environment.py // context setup steps (e.g. load from config)

    +-- *.feature // feature files

    +-- steps/

        +-- __init__.py // used to import predefined steps

        +-- json_responses.py // response structures described in Trafaret format

        +-- *.py // steps related to corresponding feature (e.g. "login.py" contains steps that are related to "login.feature")  
        
```

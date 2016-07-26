# behave-rest
BDD-style Rest API testing tool

It uses python's requests (https://pypi.python.org/pypi/requests/) for performing HTTP requests, nose (https://pypi.python.org/pypi/nose/1.3.7) for most assertions, trafaret (https://github.com/Deepwalker/trafaret) for json validation and behave (https://pypi.python.org/pypi/behave/1.2.5) for BDD style of tests.


### Running

To run a particular feature file, use `behave` + filename (e.g. `behave features/login.feature`) Don't forget to specify path to the feature file!

To run all feature files use `behave`

Add `--no-capture` to see printed output: `behave --no-capture`

Use `--tags=tagname` to run feature with a particular tag (e.g. 'positive', 'negative'): `behave --tags=positive`


### Dependencies:

-behave

-nose

-requests

-trafaret


Run `pip install -r requirements.txt` to install required dependencies


### Project Structure:

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

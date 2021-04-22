# seleniumbase-qa-interview
just having fun with selenium base and a start project that can be used to help QA/SDET interviews.  This is based off and using www.seleniumbase.io

# Pre-requisites
Having the following installed
* python
* pip
* seleniumbase

Selenium base has good documentation how to install python, pip and sbase here (This will also take care of all webdriver needs)
https://seleniumbase.io/help_docs/install_python_pip_git/

From there you can install seleniumbase with pip: ```pip install seleniumbase```

# Write the following tests for MyTestClass(BaseCase):
```
 # hit the lets go button and run a speed test
        
        #  navigation menu:
        # go to any sub page for each of the following navigation items apps, insights, network, developers

        # Under the Log In button menu, go to Settings

        # switch to 24-hr global settings from 12

        # Set Distance to Kilometers

        # navigate away and go back and assert:
        # the changes are still 24 hours

        # and the Distance is set to Kilometers.

        ## Extra ##
        ## Navigate to the Results history (under login) page
        # and write any tests you find interesting
 ```

# How to run the test file
```
pytest qa_interview.py      
```

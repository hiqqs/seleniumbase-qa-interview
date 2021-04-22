from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basics(self):
        self.open("https://www.speedtest.net/")
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
        ## If you finish that really easily try going to the Results history (under login) page
        # and write any tests you find interesting
from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basics(self):
        self.open("https://www.speedtest.net/"),
        # hit the lets go button and run a speed test
        self._run_speed_test(),

        # Under the Log In button menu, go to Settings, switch to 24-hr global settings from 12,
        # Set Distance to Kilometers, navigate away and go back and assert:
        # the changes are still 24 hours, and the Distance is set to Kilometers.
        self._test_setting_changes_stay_after_navigate_away(),

        ## Extra ##
        ## If you finish that really easily try going to the Results history (under login) page
        # and write any tests you find interesting
        self._test_results_history(),

        # navigation menu:
        # go to any sub page for each of the following navigation items apps, insights, network, developers

        # Apps -> IOS
        self._test_apps_ios(),

        # Insights -> Blog
        self._test_insights_blog(),

        # I got 429 too many request error when I was testing the navigation menu, please comment out
        # the following 2 test cases all together if you see 429 error.(network and developers)

        # Network
        # self._test_network(),

        # Developers
        # self._test_developers(),


    def _test_apps_ios(self):
        self.hover_and_click('.nav-menu li:first-child', '.nav-menu li:first-child .sub-menu li:first-child a'),
        self.assert_title("Speedtest for iOS - Download Speedtest for the iPhone and iPad on the App Store"),
        self.assert_no_404_errors()

    def _test_insights_blog(self):
        self.hover_and_click('.nav-menu > li:nth-child(2)', '.nav-menu > li:nth-child(2) .sub-menu li:first-child a'),
        self.assert_title("Speedtest Stories & Analysis: Data-driven articles on internet speeds"),
        self.assert_no_404_errors()

    def _test_network(self):
        self.click_link('Network'),
        self.assert_title("Speedtest Servers | Ookla"),
        self.assert_no_404_errors()

    def _test_developers(self):
        self.click_link("Developers"),
        self.assert_title("Speedtest CLI - Internet connection measurement for developers"),
        self.assert_no_404_errors()

    def _test_setting_changes_stay_after_navigate_away(self):
        # Under the Log In button menu, go to Settings
        self.hover_and_click('.nav-menu > li:nth-child(7)', '.nav-menu > li:nth-child(7) .sub-menu > li:nth-child(2) a'),
        # switch to 24-hr global settings from 12
        self.click('#global-settings-form .radio-label-input input[type=radio]+label[for="2"]'),
        # Set Distance to Kilometers
        self.click('.radio-label-input input[type=radio]+label[for="kilometers"]'),
        # navigate away and go back and assert:
        # the changes are still 24 hours
        self.click('.nav-menu > li:nth-child(4) a'),
        self.hover_and_click('.nav-menu > li:nth-child(7)', '.nav-menu > li:nth-child(7) .sub-menu > li:nth-child(2) a'),
        self.is_checked('.radio-label-input input[type=radio][value="2"]'),
        # and the Distance is set to Kilometers.
        self.is_checked('.radio-label-input input[type=radio][value="kilometers"]')

    def _run_speed_test(self):
        self.click('.start-button a.js-start-test'),
        # close the pop up ads after the speed run complete
        self.click('.desktop-app-prompt-modal a.notification-dismiss.close-btn', timeout=60),
        # result should have download speed
        self.assert_element('.result-item-download span.download-speed'),
        # result should have ping
        self.assert_element('.result-item-ping span.ping-speed'),

        # result should have upload speed
        self.assert_element('.result-item-upload span.upload-speed')

    def _test_results_history(self):
        self.hover_and_click('.nav-menu > li:nth-child(7)', '.nav-menu > li:nth-child(7) .sub-menu > li:first-child a'),
        # confirm there is one result
        self.assert_element('.result-row'),
        # take a screenshot of the results page
        self.save_screenshot("result_page")
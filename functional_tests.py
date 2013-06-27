import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', browser.title)
        self.fail('Finish the test!')

        # She is invited to neter a to-do item straight away

        #She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item on a to-do list

        # There is still a text box inviting her ot add another item. She
        # enters "Use peacock feathers to make a fly" (Edisth is very methodical)

        # The page updates again, and now shows boht items on her list

        #Edit wonders whetehr the site will remember he list. Then she sees
        # that the site has generated a unique URL for her -- there is som
        # explanatory text to that effect.

        # She visists that URL - her to-do list is still there.

        # Satisfied, she goes back to cleep

if __name__ == "__main__":
    unittest.main()

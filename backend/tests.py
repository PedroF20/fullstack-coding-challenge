import unittest
from app import app
from app import unbabel_api, hackernews_api, database


class AppTestCase(unittest.TestCase):

	def setUp(self):
		# creates a test client
		self.app = app.test_client()
		# propagate the exceptions to the test client
		self.app.testing = True

	# testing the route
	def test_show_items_page():
		r = self.app.get('/')
		# assert the status code of the response
        self.assertEqual(r.status_code, 200)

    # testing the hackernews_api
    def test_get_10_top_items():
    	top_items = hackernews_api.get_10_top_items()
    	self.assertEqual(len(top_items), 10)

    # testing the hackernews_api
    def test_get_details():
    	top_items = hackernews_api.get_10_top_items()
    	random_item = get_details(top_items[0])
    	self.assertTrue(random_item['title'])
        self.assertTrue(random_item['by'])
        self.assertTrue(random_item['url'])



if __name__ == '__main__':
    unittest.main()
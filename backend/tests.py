import unittest
from app.yetanotherhackernews import app
from app import unbabel_api, hackernews_api, database, yetanotherhackernews


class AppTestCase(unittest.TestCase):

	def setUp(self):
		# creates a test client
		self.app = app.test_client()
		# propagate the exceptions to the test client
		self.app.testing = True

	# testing the route
	def test_show_items_page(self):
		r = self.app.get('/')
		# assert the status code of the response
		self.assertEqual(r.status_code, 200)

    # testing the hackernews_api
	def test_get_10_top_items(self):
		top_items = hackernews_api.get_10_top_items()
		self.assertEqual(len(top_items), 10)

    # testing the hackernews_api
	def test_get_details(self):
		top_items = hackernews_api.get_10_top_items()
		random_item = hackernews_api.get_details(top_items[0])
		self.assertTrue(random_item['title'])
		self.assertTrue(random_item['by'])
		self.assertTrue(random_item['url'])

    # testing the unbabel_api
	def test_post_translation(self):
		r = unbabel_api.post_translation("this is a test", "pt")
		self.assertTrue(r['uid'])

    # testing the unbabel_api
	def test_get_translation(self):
		r = unbabel_api.post_translation("this is a test", "pt")
		d = unbabel_api.get_translation(r['uid'])
		self.assertTrue(d['status'])

    # testing the database


if __name__ == '__main__':
	unittest.main()
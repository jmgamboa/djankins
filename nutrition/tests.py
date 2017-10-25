from django.test import TestCase

# Create your tests here.
class TestQuestion(TestCase):

	def test_question(self):
		print 'made it to the test question'
		assert 1 == 1

import unittest
from app. models import Articles

class TestSources(unittest.TestCase):
    def setUp(self):

        self.new_source = Articles("al-jazeera-english","Al Jazeera English","News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.","http://www.aljazeera.com","general","en","us")

    def test_init(self):

        self.assertEqual(self.new_source.author,"al-jazeera-english")
        self.assertEqual(self.new_source.title,"Al Jazeera English")
        self.assertEqual(self.new_source.description,"News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.")
        self.assertEqual(self.new_source.url,"http://www.aljazeera.com")
        self.assertEqual(self.new_source.urlToImage,"general")
        self.assertEqual(self.new_source.publishedAt,"en")
        self.assertEqual(self.new_source.content,"us")
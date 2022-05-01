import unittest
from app. models import Sources

class TestSources(unittest.TestCase):
    def setUp(self):

        self.new_source = Sources("al-jazeera-english","Al Jazeera English","News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.","http://www.aljazeera.com","general","en","us")

    def test_init(self):

        self.assertEqual(self.new_source.id,"al-jazeera-english")
        self.assertEqual(self.new_source.name,"Al Jazeera English")
        self.assertEqual(self.new_source.description,"News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.")
        self.assertEqual(self.new_source.url,"http://www.aljazeera.com")
        self.assertEqual(self.new_source.category,"general")
        self.assertEqual(self.new_source.language,"en")
        self.assertEqual(self.new_source.country,"us")
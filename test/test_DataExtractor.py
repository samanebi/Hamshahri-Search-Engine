from unittest import TestCase
from src.DataExtractor import *

class TestExtractor(TestCase):
    def test_extract(self):
        target = Extractor()
        target.extract()

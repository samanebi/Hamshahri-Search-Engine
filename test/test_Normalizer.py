from unittest import TestCase
from src.Normalizer import *
from src.DataExtractor import *
class Testnormalizer(TestCase):
    def test_normalize(self):
        e = Extractor()
        n = normalizer(e.extract())
        n.normalize()

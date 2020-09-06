import pyterrier as pt
import unittest
from .base import BaseTestCase


class TestTopicsParsing(BaseTestCase):

    def testSingleLine(self):
        import os
        topics = pt.Utils.parse_singleline_topics_file(
            os.path.dirname(os.path.realpath(__file__)) + "/fixtures/singleline.topics")
        self.assertEqual(2, len(topics))
        self.assertTrue("qid" in topics.columns)
        self.assertTrue("query" in topics.columns)
        self.assertEqual(topics["qid"][0], "1")
        self.assertEqual(topics["qid"][1], "2")
        self.assertEqual(topics["query"][0], "one")
        self.assertEqual(topics["query"][1], "two words")

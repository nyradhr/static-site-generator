import unittest

from extractlinks import *

class TestExtractLinks(unittest.TestCase):

    def test_extract_one_link(self):
        tuples = extract_markdown_links("This one is a link: [yes](no)")
        expected = [("yes", "no")]
        self.assertEqual(tuples, expected)

    def test_extract_one_image(self):
        tuples = extract_markdown_images("Here is an image: ![desc](url)")
        expected = [("desc", "url")]
        self.assertEqual(tuples, expected)

    def test_extract_multiple_links(self):
        tuples = extract_markdown_links("Link one is [one](first.dot), link two is [two](second.dot)")
        expected = [("one", "first.dot"), ("two", "second.dot")]
        self.assertEqual(tuples, expected)

    def test_extract_multiple_images(self):
        tuples = extract_markdown_images("First image is ![flower](flower.img), second image is ![car](car.img)")
        expected = [("flower", "flower.img"), ("car", "car.img")]
        self.assertEqual(tuples, expected)

    def test_extract_no_link(self):
        tuples = extract_markdown_links("This string does not contain links")
        expected = []
        self.assertEqual(tuples, expected)

    def test_extract_no_image(self):
        tuples = extract_markdown_images("This string does not contain images")
        expected = []
        self.assertEqual(tuples, expected)

    def test_fail_extract_link_from_image(self):
        tuples = extract_markdown_links("This is not a link: ![desc](image)")
        expected = []
        self.assertEqual(tuples, expected)

    def test_fail_extract_image_from_link(self):
        tuples = extract_markdown_images("This is not an image: [click here](boo.gotcha)")
        expected = []
        self.assertEqual(tuples, expected)

    def test_extract_link_no_anchor(self):
        tuples = extract_markdown_links("This link doesn't have clickable text: [](howcanthis.be)")
        expected = [("", "howcanthis.be")]
        self.assertEqual(tuples, expected)

    def test_extract_image_no_alt(self):
        tuples = extract_markdown_images("This image doesn't have a description: ![](phantom.jpg)")
        expected = [("", "phantom.jpg")]
        self.assertEqual(tuples, expected)

    def test_extract_link_punctuation(self):
        tuples = extract_markdown_links("[Hello, World!?](example.com)")
        expected = [("Hello, World!?", "example.com")]
        self.assertEqual(tuples, expected)

    def test_extract_link_unicode(self):
        tuples = extract_markdown_links("[èé & á çù§°#*](https://école.edu)")
        expected = [("èé & á çù§°#*", "https://école.edu")]
        self.assertEqual(tuples, expected)

    def test_extract_link_url_parameters(self):
        tuples = extract_markdown_links("[search](https://search.com?q=test&page=1)")
        expected = [("search", "https://search.com?q=test&page=1")]
        self.assertEqual(tuples, expected)

    def test_extract_link_quotes(self):
        tuples = extract_markdown_links("[\"quotes\'](https://yay.wee)")
        expected = [("\"quotes\'", "https://yay.wee")]
        self.assertEqual(tuples, expected)
    
    def test_extract_link_multiple_spaces(self):
        tuples = extract_markdown_links("[  spaces  ](lo%20tsof.%20space%20)")
        expected = [("  spaces  ", "lo%20tsof.%20space%20")]
        self.assertEqual(tuples, expected)

    def test_extract_link_url_subdomain_paths(self):
        tuples = extract_markdown_links("[example](https://subdomain.second.top/content-page)")
        expected = [("example", "https://subdomain.second.top/content-page")]
        self.assertEqual(tuples, expected)

    def test_extract_image_basic_special_chars(self):
        tuples = extract_markdown_images("![Alt & Text!](image.jpg)")
        expected = [("Alt & Text!", "image.jpg")]
        self.assertEqual(tuples, expected)
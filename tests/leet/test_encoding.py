# encoding: utf-8

import unittest

from leetehao.leet import encoding


class EncodingTestCase(unittest.TestCase):

    def test_coding(self):

        message, encoded = 'hello world', '}{[-[_[_<>@@vv<>[z[_|)'

        # normal case
        self.assertEqual(encoding.encode(message), encoded)
        self.assertEqual(encoding.decode(encoded), message.upper())

    def test_class(self):

        message, encoded = 'hello world', '}{[-[_[_<>@@vv<>[z[_|)'

        en, de = encoding.LeetEncoder(), encoding.LeetDecoder()

        self.assertEqual(en.encode(message), encoded)
        self.assertEqual(de.decode(encoded), message.upper())

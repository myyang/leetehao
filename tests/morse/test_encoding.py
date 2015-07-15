# encoding: utf-8

import unittest

from leetehao.morse import encoding


class EncodingTestCase(unittest.TestCase):

    def test_coding(self):

        message, encoded = 'hello world', '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'

        # normal case
        self.assertEqual(encoding.encode(message), encoded)
        self.assertEqual(encoding.decode(encoded), message.upper())

        # encode error
        msg = '錯'
        self.assertRaises(encoding.MorseEncodeError, encoding.encode, msg)

        # decode error
        msg = '.--------------.'
        self.assertRaises(encoding.MorseDecodeError, encoding.decode, msg)

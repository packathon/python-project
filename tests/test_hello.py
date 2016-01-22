import io
import unittest

import hello


class HelloTest(unittest.TestCase):

    def test_hello(self):
        output = io.StringIO()
        hello.say_hello('cihann', file=output)
        self.assertEqual(output.getvalue(), 'Hello, cihann!\n')


if __name__ == '__main__':
    unittest.main()

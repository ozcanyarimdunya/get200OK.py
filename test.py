import unittest
import io
import sys
from get200ok import get200ok


class TestGet200Ok(unittest.TestCase):
    """
    Test class for Get200Ok
    """

    def test_success(self):
        """test for success"""
        working_urls = [
            "https://google.com/",
            "https://facebook.com/",
            "https://youtube.com/",
        ]
        output = io.StringIO()
        sys.stdout = output
        get200ok(working_urls)
        sys.stdout = sys.__stdout__
        self.assertGreaterEqual(
            len(output.getvalue().split('SUCCESS')),
            1
        )

    def test_failed(self):
        """test for success"""
        working_urls = [
            "_-_-_-_google.com/",
            "_-_-_-_facebook.com/",
            "_-_-_-_youtube.com/",
        ]
        output = io.StringIO()
        sys.stdout = output
        get200ok(working_urls)
        sys.stdout = sys.__stdout__
        self.assertGreaterEqual(
            len(output.getvalue().split('FAILED')),
            1
        )


if __name__ == '__main__':
    unittest.main()

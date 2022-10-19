import unittest

import src.upload.router as router


class BasicTest(unittest.TestCase):
    """Test basic functionality for "upload" route."""

    def test_base(self):
        self.assertEqual(router.upload_http(), "ASD")

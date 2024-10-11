import unittest

from . import create_file_name


class TestMig(unittest.TestCase):
    def test_get_resource_name(self) -> None:
        got = create_file_name("demo", "foo")
        expected = "ZGVtbw==_foo"

        self.assertEqual(got, expected)

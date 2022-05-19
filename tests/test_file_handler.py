from unittest import TestCase

from main.file_handler import FileHandler


class TestFileHandler(TestCase):
    PATH = './files/logdata.txt'
    file_reader = FileHandler()

    def test_read_file(self):

        response = self.file_reader.read_file(self.PATH)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

    def test_extract_lines(self):
        self.file_reader.read_file(self.PATH)
        response = self.file_reader.extract_lines()

        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)
        self.assertEqual(979, len(response))

    def test_split_items(self):
        self.file_reader.read_file(self.PATH)
        self.file_reader.extract_lines()

        response = self.file_reader.split_items()

        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)
        self.assertEqual(979, len(response))

    def test_build_final_response(self):
        self.file_reader.read_file(self.PATH)
        self.file_reader.extract_lines()
        expected = {
            'host': '146.204.224.152',
            'user_name': 'feest6811',
            'time': '[21/Jun/2019:15:45:24 -0700]',
            'request': '"POST /incentivize HTTP/1.1"'
        }

        response = self.file_reader.build_final_response()

        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(979, len(response))
        self.assertEqual(expected, response[0])

import unittest
from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def setUp(self):
        self.func = write_file
        self.wd = "calculator"

    def test_lorem(self):
        print("Result for 'lorem.txt'")
        print(self.func("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    def test_pkg_morelorem(self):
        print("Result for 'pkg/morelorem.txt'")
        print(self.func("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    def test_tmp_temp(self):
        print("Result for '/tmp/temp.txt'")
        print(self.func("calculator", "/tmp/temp.txt", "this should not be allowed"))


if __name__ == "__main__":
    unittest.main()

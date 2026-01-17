import unittest
from functions.get_file_content import get_file_content


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.func = get_file_content
        self.wd = "calculator"

    def test_lorem(self):
        print("Result for 'lorem.txt'")
        print(self.func("calculator", "lorem.txt"))

    def test_main(self):
        print("Result for 'main.py'")
        print(self.func("calculator", "main.py"))

    def test_pkg_calculator(self):
        print("Result for 'pkg/calculator.py'")
        print(self.func("calculator", "pkg/calculator.py"))
              
    def test_bin_cat(self):
        print("Result for '/bin/cat'")
        print(self.func("calculator", "/bin/cat"))

    def test_pkg_does_not_exist(self):
        print("Result for 'pkg/does_not_exist.py'")
        print(self.func("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    unittest.main()

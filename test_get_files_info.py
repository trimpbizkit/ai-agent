import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.func = get_files_info
        self.wd = "calculator"

    def print_result(self, result):
        lines = result.split("\n")
        for line in lines:
            if line.startswith("-"):
                print(f"  {line}")
            elif line.startswith("Error:"):
                print(f"    {line}")


    def test_current_directory(self):
        print("Result for current directory:")
        result = self.func(self.wd, ".")
        self.print_result(result)

    def test_pkg(self):
        print("Result for 'pkg' directory:")
        result = self.func(self.wd, "pkg")
        self.print_result(result)

    def test_bin(self):
        print("Result for '/bin' directory:")
        result = self.func(self.wd, "/bin")
        self.print_result(result)

    def test_parent_directory(self):
        print("Result for '../' directory:")
        result = self.func(self.wd, "../")
        self.print_result(result)


if __name__ == "__main__":
    unittest.main()

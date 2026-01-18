import unittest
from functions.run_python_file import run_python_file


class TestRunPythonFile(unittest.TestCase):
    def setUp(self):
        self.func = run_python_file
        self.wd = "calculator"

    def test_main(self):
        print("Result for 'main.py' with no arguments")
        print(self.func("calculator", "main.py"))
        print("Result for 'main.py' with arguments")
        print(self.func("calculator", "main.py", ["3 + 5"]))
        print("Result for 'main.py' with bad relative path")
        print(self.func("calculator", "../main.py"))

    def test_tests(self):
        print("Result for 'tests.py'")
        print(self.func("calculator", "tests.py"))
        
    def test_nonexistent(self):
        print("Result for 'nonexistent.py'")
        print(self.func("calculator", "nonexistent.py"))

    def test_lorem(self):
        print("Result for 'lorem.txt'")
        print(self.func("calculator", "lorem.txt"))   

if __name__ == "__main__":
    unittest.main()

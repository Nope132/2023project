#!/usr/bin/python
# coding utf-8

import unittest

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual("foo".upper(),"FOO")

    def test_3(self):
        self.assertTrue(2>1)

    def test_2(self):
        self.assertFalse(1>2)

    def mytest_4(self):
        self.assertTrue(True)
def loadTests():

    tests =list()

    module = __import__("__main__")

    for part in dir(module):
	print(part)
        attr = getattr(module,part)
	if isinstance(attr,type) and issubclass(attr,unittest.TestCase):
           tests.append(attr)
    return tests

def runTests(tests):
    #print(tests)
    for test in tests:
        obj=test()
        for part in dir(test):
            if parts.startswith("test") and callable(getattr(obj,part)):
	       case.append(part)
            for c in sorted(cases):
		print(c)
	        func=getattr(obj,c)
	        func()
def main():
    tests=loadTests()
    runTests(tests)
main()
from __future__ import print_function

TEST_INDENT = "      "

verbose = False

class UnitTestError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Test failed! " + repr(self.value)

def test(a):
    if not a:
        raise UnitTestError(a)
    if verbose:
        print(TEST_INDENT + "SUCCESS  " + a)

def test_equal(a, b):
    if a != b:
        raise UnitTestError(str(a) + " != " + str(b))
    if verbose:
        print(TEST_INDENT + "SUCCESS  " + str(a) + " == " + str(b))

def section(sec):
    print("\n---  " + sec + "----------------")
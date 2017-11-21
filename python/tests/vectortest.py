import unittest

class TestVector(unittest.TestCase):

    def test_mul(self):
        pass


if __name__ != "__main__":
    from geometry import vector

    unittest.verbose = True
    unittest.section("Vector tests")
    v = vector.Vector3(1, 2, 3)
    print "print vector (1, 2, 3):\n\t\t", v
    print "repr:\n\t\t{!r}".format(v)
    print "dimension of vector:\n\t\t", v.dim
    #v[4]=2
    #print "wrong index:\n", v[4]
    u = vector.Vector3(2, 3, 4)
    print "Vector3(1, 2, 3) + Vector(2, 3, 4) =", u + v
    print "Vector3(1, 2, 3) - Vector(2, 3, 4) =", u - v
    print "Vector3(1, 2, 3) * Vector(2, 3, 4) =", u * v

    unittest.test_equal(u * v, 20)

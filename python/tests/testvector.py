import unittest
from geometry import vector

class TestVector(unittest.TestCase):

    def test_print(self):
        print("__str__ of Vector class: ", end="")
        print("__repr__ of Vector class: ", end="")
        print("__str__ of Vector3 class: ", end="")
        print("__repr__ of Vector3 class: ", end="")
        v = vector.Vector3(1, 2, 3)
        print(v)

    def test_add(self):
        v = vector.Vector3(1, 2, 3)
        u = vector.Vector3(3.5, -3, 3.2)
        w = vector.Vector3(4.5, -1.0, 6.2)
        v = u + v
        self.assertAlmostEqual(v.x, w.x)
        self.assertAlmostEqual(v.y, w.y)
        self.assertAlmostEqual(v.z, w.z)

    def test_sub(self):
        v = vector.Vector3(1, 2, 3)
        u = vector.Vector3(3.5, -3, 3.2)
        w = vector.Vector3(2.5, -5.0, 0.2)
        v = u - v
        self.assertAlmostEqual(v.x, w.x)
        self.assertAlmostEqual(v.y, w.y)
        self.assertAlmostEqual(v.z, w.z)

    def test_mul(self):
        v = vector.Vector3(1, 2, 3)
        u = vector.Vector3(3, 6, 9)
        v *= 3
        self.assertEqual(u, v)

    def test_div(self):
        v = vector.Vector3(1, 2, 3)
        v /= 5.0
        u = vector.Vector3(0.2, 0.4, 0.6)
        self.assertAlmostEqual(v.x, u.x)
        self.assertAlmostEqual(v.y, u.y)
        self.assertAlmostEqual(v.z, u.z)
        with self.assertRaises(AssertionError):
            v /= 0.0

"""
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
"""
if __name__ == '__main__':
    unittest.main()
"""Vector classes and vector helper functions."""
import math

######### Error strings #######################################################
STR_INEQUAL_DIMENSIONS = "Vector dimensions must be equal"
STR_TINY_DENOMINATOR = "The denominator is too small"
###############################################################################

EPSILON = 1e-10

class Vector(object):
    """General vector class."""

    def __new__(cls, *args, **kwargs):
        cls.__rmul__ = cls.__mul__
        cls.__truediv__ = cls.__div__
        return super(Vector, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args):
        self._vec = [float(arg) for arg in args]

    @property
    def dim(self):
        return len(self._vec)

    def length2(self):
        """Calculate v*v."""
        length2 = 0.0
        for v in self._vec:
            length2 += v * v
        return length2

    def length(self):
        """Calculate the length of the vector."""
        return math.sqrt(self.length2())

    def __getitem__(self, index):
        if index < 0 or index >= len(self._vec):
            raise IndexError("Index " + str(index) + " out of range [0,"
                    + str(self.dim) + ")")
        return self._vec[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self._vec):
            raise IndexError("Index " + str(index) + " out of range [0,"
                    + str(self.dim) + ")")
        self._vec[index] = value

    def __abs__(self):
        return self.__class__(*[math.fabs(x) for x in self._vec])

    def __eq__(self, vec):
        assert self.dim == vec.dim, STR_INEQUAL_DIMENSIONS
        for i in xrange(len(self._vec)):
            if self._vec[i] != vec._vec[i]:
                return False
        return True

    def __ne__(self, vec):
        assert self.dim == vec.dim, STR_INEQUAL_DIMENSIONS
        return not (self == vec)

    def __add__(self, vec):
        if isinstance(vec, Vector):
            assert self.dim == vec.dim, STR_INEQUAL_DIMENSIONS
            return self.__class__(
                *[u + v for u, v in zip(self._vec, vec._vec)])
        else:
            return self.__class__(*[u + vec for u in self._vec])

    def __sub__(self, vec):
        if isinstance(vec, Vector):
            assert self.dim == vec.dim, STR_INEQUAL_DIMENSIONS
            return self.__class__(
                *[u - v for u, v in zip(self._vec, vec._vec)])
        else:
            return self.__class__(*[u - vec for u in self._vec])

    def __mul__(self, vec):
        if isinstance(vec, Vector):
            assert self.dim == vec.dim, STR_INEQUAL_DIMENSIONS
            return sum([u * v for u, v in zip(self._vec, vec._vec)])
        else:
            return self.__class__(*[u * vec for u in self._vec])

    def __div__(self, scalar):
        assert abs(scalar) > EPSILON, STR_TINY_DENOMINATOR
        return self.__class__(*[u / scalar for u in self._vec])

    def __repr__(self):
        string_strips = []
        ## Add class label
        string_strips.append("{cls}".format(cls=self.__class__))
        ## Add GUID
        string_strips.append(" id={guid} ".format(guid=id(self)))
        ## Add all vector components
        string_strips.append(self.__str__())
        return "".join(string_strips)

    def __str__(self):
        string_strips = []
        string_strips.append("(")
        def to_float_str(num):
            return "{:f}".format(num)
        v = map(to_float_str, self._vec)
        s = ", ".join(v)
        string_strips.append(s)
        string_strips.append(")")
        return "".join(string_strips)

class Vector3(Vector):
    """A vector class having 3 components."""

    def __init__(self, x=0, y=0, z=0):
        super(Vector3, self).__init__(x, y, z)

    @property
    def x(self):
        return self._vec[0]

    @x.setter
    def x(self, value):
        self._vec[0] = value

    @property
    def y(self):
        return self._vec[1]

    @y.setter
    def y(self, value):
        self._vec[1] = value

    @property
    def z(self):
        return self._vec[2]

    @z.setter
    def z(self, value):
        self._vec[2] = value

    def __repr__(self):
        return "{cls} id={guid} ({x:f}, {y:f}, {z:f})".format(
                cls=self.__class__, guid=id(self),
                x=self.x, y=self.y, z=self.z
                )

    def __str__(self):
        return "({x}, {y}, {z})".format(x=self.x, y=self.y, z=self.z)

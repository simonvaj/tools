"""Vector classes and vector helper functions."""

class Vector(object):
    """General vector class."""

    def __init__(self, *args):
        self._vec = [float(arg) for arg in args]

    @property
    def dim(self):
        return len(self._vec)

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
        return "{} id={} ({:f}, {:f}, {:f})".format(
                self.__class__, id(self), self.x, self.y, self.z
                )

    def __str__(self):
        return "({:f}, {:f}, {:f})".format(self.x, self.y, self.z)

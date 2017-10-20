if __name__ != "__main__":
    from geometry import vector

    v = vector.Vector3(1, 2, 3)
    print "print vector (1, 2, 3):\n\t\t", v
    print "repr:\n\t\t{!r}".format(v)
    print "dimension of vector:\n\t\t", v.dim
    v[4]=2
    print "wrong index:\n", v[4]


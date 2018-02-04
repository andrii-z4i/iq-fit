class FitObject(object):

    def __init__(self, side_a, side_b):
        if not isinstance(side_a, tuple) or not isinstance(side_b, tuple):
            raise Exception("Side a and side b have to be instance of tuple")

        if len(side_a) != len(side_b):
            raise Exception("Sides have to be the same side")

        for i in range(0, len(side_a)):
            if len(side_a[i]) != len(side_b[i]):
                raise Exception(
                    "x,y size of side a has to be the same as x,y of side b")

        self._side_a = side_a
        self._side_b = side_b
        self._active_side = 'a'

    @property
    def side_a(self):
        return self._side_a

    @property
    def side_b(self):
        return self._side_b

    @property
    def active_side(self):
        return self._side_a if self._active_side == 'a' else self._side_b

    @property
    def active_side_name(self):
        return self._active_side

    def switch_active_side(self):
        self._active_side = 'b' if self._active_side == 'a' else 'b'

    def rotate_left(self):
        self._side_a = tuple(zip(*self._side_a))[::-1]
        self._side_b = tuple(zip(*self._side_b))[::-1]

    def rotate_right(self):
        self._side_a = tuple(zip(*self._side_a[::-1]))
        self._side_b = tuple(zip(*self._side_b[::-1]))

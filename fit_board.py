from fit_object import FitObject
from copy import deepcopy


class _FitObjectWrapper(object):
    def __init__(self, fit_object, x, y):
        self._fit_object = fit_object
        self._x = x
        self._y = y

    def __str__(self):
        return "Object :={side: %s, shape: %s, on (x=%d, y=%d) }" %\
            (
                self._fit_object.active_side_name,
                self._fit_object.active_side,
                self._x,
                self._y
            )

    def __repr__(self):
        return "Object :={side: %s, shape: %s, on (x=%d, y=%d) }" %\
            (
                self._fit_object.active_side_name,
                self._fit_object.active_side,
                self._x,
                self._y
            )

    @property
    def fit_object(self):
        return self._fit_object

    @property
    def coordinates(self):
        return dict(x=self._x, y=self._y)


class FitBoard(object):
    def __init__(self, size_x, size_y):
        self._board = [[0 for y in range(size_y)] for i in range(size_x)]
        self._objects_on_board = []

    @property
    def board(self):
        return self._board

    @property
    def objects_list(self):
        return self._objects_on_board

    def can_object_be_placed(self, fit_object, x, y):
        _copy_of_board = deepcopy(self._board)
        _active_object_side = fit_object.active_side
        try:
            self._add_object(_active_object_side, _copy_of_board, x, y, True)
        except:
            return False
        return True

    def add_object(self, fit_object, x, y):
        if not self.can_object_be_placed(fit_object, x, y):
            raise Exception(
                'Object can\'t be placed on board with coordinates %d, %d' % (x, y))

        _active_object_side = fit_object.active_side
        self._add_object(_active_object_side, self._board, x, y)

        self._objects_on_board.append(
            _FitObjectWrapper(deepcopy(fit_object), x, y))

    def _add_object(self, _active_object_side, _board, x, y, _raise_if_overlap=False):
        _index_y = 0
        for _y_row in _active_object_side:
            _index_x = 0
            for _x in _y_row:
                if _raise_if_overlap and _x and _board[y + _index_y][x + _index_x]:
                    raise Exception('Value in (%d, %d) is already set' % (
                        x + _index_x, y + _index_y))

                if _x:
                    _board[y + _index_y][x + _index_x] = _x

                _index_x += 1
            _index_y += 1

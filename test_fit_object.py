import unittest
from fit_object import FitObject


class FitObjectTest(unittest.TestCase):

    def test_create_object(self):
        FitObject(((1, 0), (1, 0), (1, 1), (1, 0)),
                  ((1, 0), (1, 1), (1, 1), (1, 0)))

    def test_rotate_left(self):
        _side_a = ((1, 0), (1, 0), (1, 1), (1, 0))
        _side_b = ((1, 0), (1, 1), (1, 1), (1, 0))
        _side_a_rotated = ((0, 0, 1, 0), (1, 1, 1, 1))
        _side_b_rotated = ((0, 1, 1, 0), (1, 1, 1, 1))
        _object = FitObject(_side_a, _side_b)
        _object.rotate_left()
        self.assertTupleEqual(_side_a_rotated, _object.side_a)
        self.assertTupleEqual(_side_b_rotated, _object.side_b)

    def test_rotate_right(self):
        _side_a = ((1, 0), (1, 0), (1, 1), (1, 0))
        _side_b = ((1, 0), (1, 1), (1, 1), (1, 0))
        _side_a_rotated = ((1, 1, 1, 1), (0, 1, 0, 0))
        _side_b_rotated = ((1, 1, 1, 1), (0, 1, 1, 0))
        _object = FitObject(_side_a, _side_b)
        _object.rotate_right()
        self.assertTupleEqual(_side_a_rotated, _object.side_a)
        self.assertTupleEqual(_side_b_rotated, _object.side_b)

    def test_rotate_right_4_times(self):
        _side_a = ((1, 0), (1, 0), (1, 1), (1, 0))
        _side_b = ((1, 0), (1, 1), (1, 1), (1, 0))
        _object = FitObject(_side_a, _side_b)
        _object.rotate_right()
        _object.rotate_right()
        _object.rotate_right()
        _object.rotate_right()
        self.assertTupleEqual(_side_a, _object.side_a)
        self.assertTupleEqual(_side_b, _object.side_b)

    def test_rotate_left_4_times(self):
        _side_a = ((1, 0), (1, 0), (1, 1), (1, 0))
        _side_b = ((1, 0), (1, 1), (1, 1), (1, 0))
        _object = FitObject(_side_a, _side_b)
        _object.rotate_left()
        _object.rotate_left()
        _object.rotate_left()
        _object.rotate_left()
        self.assertTupleEqual(_side_a, _object.side_a)
        self.assertTupleEqual(_side_b, _object.side_b)

    def test_switch_active_side(self):
        _side_a = ((1, 0), (1, 0), (1, 1), (1, 0))
        _side_b = ((1, 0), (1, 1), (1, 1), (1, 0))
        _object = FitObject(_side_a, _side_b)
        self.assertTupleEqual(_side_a, _object.active_side)
        self.assertEqual('a', _object.active_side_name)
        _object.switch_active_side()
        self.assertTupleEqual(_side_b, _object.active_side)
        self.assertEqual('b', _object.active_side_name)

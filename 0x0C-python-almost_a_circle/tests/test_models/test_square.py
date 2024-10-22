#!/usr/bin/python3
'''Moduli kwa ajili ya majaribio ya Square.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    '''Testi za darasa la Base.'''

    def setUp(self):
        '''Inagiza moduli, inaunda darasa'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Inafuta baada ya kila test_method.'''
        pass

    def test_A_class(self):
        '''Inajaribu aina ya darasa la Square.'''
        self.assertEqual(
                str(Square),
                "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        '''Inajaribu kama Square inarithi kutoka Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        '''Inajaribu saini ya muundaji.'''
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Inajaribu saini ya muundaji.'''
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but
        6 were given"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Inajaribu kuanzisha.'''
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''Inajaribu kuanzisha kwa njia ya nafasi.'''
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Inajaribu kuanzisha kwa njia ya nenosiri.'''
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Inajaribu kama id inarithiwa kutoka Base.'''
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''Inajaribu wapokeaji wa mali.'''
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    def invalid_types(self):
        '''Inarudisha tupia ya aina kwa ajili ya uthibitishaji.'''
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''Inajaribu uthibitishaji wa mali.'''
        r = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(r, "width", invalid_type)
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''Inajaribu uthibitishaji wa mali.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Inajaribu uthibitishaji wa mali.'''
        r = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''Inajaribu uthibitishaji wa mali.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''Inajaribu kuweka/kuondoa mali.'''
        r = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''Inajaribu kuweka/kuondoa mali.'''
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_I_area_no_args(self):
        '''Inajaribu saini ya njia ya area().'''
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Inajaribu hesabu ya njia ya area().'''
        r = Square(6)
        self.assertEqual(r.area(), 36)
        w = randrange(10) + 1
        r.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, 7, 8, 9)
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(7, 8, 9)
        self.assertEqual(r.area(), 49)

    def test_J_str(self):
        '''Inajaribu __str__().'''
        r = Square(6, 3, 5, 9)
        self.assertEqual(str(r), "[Square] (9) 3/5 - 6")

    def test_K_update_args(self):
        '''Inajaribu update().'''
        r = Square(6, 3, 5, 9)
        r.update(89)
        self.assertEqual(str(r), "[Square] (89) 3/5 - 6")
        r.update(1, 2)
        self.assertEqual(str(r), "[Square] (1) 3/5 - 2")
        r.update(1, 2, 3)
        self.assertEqual(str(r), "[Square] (1) 3/5 - 2")
        r.update(1, 2, 3, 4)
        self.assertEqual(str(r), "[Square] (1) 4/5 - 2")

    def test_L_update_kwargs(self):
        '''Inajaribu update() kwa njia ya nenosiri.'''
        r = Square(6, 3, 5, 9)
        r.update(id=89)
        self.assertEqual(str(r), "[Square] (89) 3/5 - 6")
        r.update(size=1)
        self.assertEqual(str(r), "[Square] (89) 3/5 - 1")
        r.update(size=2, x=4)
        self.assertEqual(str(r), "[Square] (89) 4/5 - 2")
        r.update(size=2, y=5, x=6)
        self.assertEqual(str(r), "[Square] (89) 6/5 - 2")

    def test_M_to_dict(self):
        '''Inajaribu to_dictionary().'''
        r = Square(6, 3, 5, 9)
        d = {'id': 9, 'size': 6, 'x': 3, 'y': 5}
        self.assertDictEqual(r.to_dictionary(), d)

    def test_N_save_to_file(self):
        '''Inajaribu save_to_file().'''
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([Square(6, 3, 5, 9)])
        with open("Square.json", "r") as f:
            self.assertEqual
            (f.read(), '[{"id": 9, "size": 6, "x": 3, "y": 5}]')

    def test_O_load_from_file(self):
        '''Inajaribu load_from_file().'''
        Square.save_to_file([Square(6, 3, 5, 9)])
        r = Square.load_from_file()
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0].__dict__, Square(6, 3, 5, 9).__dict__)

    def test_P_save_to_file_csv(self):
        '''Inajaribu save_to_file_csv().'''
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "")
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "")
        Square.save_to_file_csv([Square(6, 3, 5, 9)])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "9,6,3,5\n")

    def test_Q_load_from_file_csv(self):
        '''Inajaribu load_from_file_csv().'''
        Square.save_to_file_csv([Square(6, 3, 5, 9)])
        r = Square.load_from_file_csv()
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0].__dict__, Square(6, 3, 5, 9).__dict__)

    def test_R_save_to_file_json(self):
        '''Inajaribu save_to_file_json().'''
        Square.save_to_file_json(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file_json([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file_json([Square(6, 3, 5, 9)])
        with open("Square.json", "r") as f:
            self.assertEqual(
                    f.read(), '[{"id": 9, "size": 6, "x": 3, "y": 5}]')

    def test_S_load_from_file_json(self):
        '''Inajaribu load_from_file_json().'''
        Square.save_to_file_json([Square(6, 3, 5, 9)])
        r = Square.load_from_file_json()
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0].__dict__, Square(6, 3, 5, 9).__dict__)


if __name__ == '__main__':
    unittest.main()

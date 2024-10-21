#!/usr/bin/python3
'''Moduli kwa ajili ya majaribio ya Rectangle.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    '''Testi za darasa la Base.'''

    def setUp(self):
        '''Inagiza moduli, inaandika darasa'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Inasafisha baada ya kila test_method.'''
        pass

    # ----------------- Tests for #2 ------------------------

    def test_A_class(self):
        '''Inajaribu aina ya darasa la Rectangle.'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''Inajaribu kama Rectangle inarithi kutoka Base.'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_C_constructor_no_args(self):
        '''Inajaribu sahihi ya mjenzi.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() inakosa 2 masharti ya lazima: 'width' \
na 'height'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Inajaribu sahihi ya mjenzi.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__() inachukua kutoka 3hadi 6
        mashartiya lazimalakini7 yalitolewa"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_one_args(self):
        '''Inajaribu sahihi ya mjenzi.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() inakosa 1 masharti ya lazima: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Inajaribu kuunda mfano.'''
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, "4")
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -2)
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -3)
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -4)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''Inajaribu kuunda mfano kwa kutumia nafasi.'''
        r = Rectangle(5, 10, 15, 20)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Rectangle(5, 10, 15, 20, 98)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Inajaribu kuunda mfano kwa kutumia maneno muhimu.'''
        r = Rectangle(100, 200, id=421, y=99, x=101)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Inajaribu kama id inarithi kutoka Base.'''
        Base._Base__nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''Inajaribu getters/setters za mali.'''
        r = Rectangle(5, 9)
        r.width = 100
        r.height = 101
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 101, '_Rectangle__width': 100,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 101)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    def invalid_types(self):
        '''Inarudisha tuple ya aina za uthibitisho.'''
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''Inajaribu uthibitisho wa mali.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''Inajaribu uthibitisho wa mali.'''
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Inajaribu uthibitisho wa mali.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''Inajaribu uthibitisho wa mali.'''
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''Inajaribu kuweka/kupata mali.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''Inajaribu kuweka/kupata mali.'''
        r = Rectangle(1, 2)
        r.width = 1
        r.height = 1
        r.x = 1
        r.y = 1
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_H_property_negative(self):
        '''Inajaribu kuweka mali hasi.'''
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError) as e:
            r.width = -1
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            r.height = -1
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(ValueError) as e:
            r.x = -1
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            r.y = -1
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_I_area(self):
        '''Inajaribu kuhesabu eneo.'''
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_I_area(self):
        '''Inajaribu kuhesabu eneo.'''
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_J_str(self):
        '''Inajaribu kuonyesha uandishi wa Rectangle.'''
        r = Rectangle(4, 6, 2, 3, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/3 - 4/6")

    def test_K_display(self):
        '''Inajaribu kuonyesha Rectangle.'''
        r = Rectangle(3, 2)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
        self.assertEqual(output, "###\n###\n")

        r = Rectangle(2, 2, 2, 2)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
        self.assertEqual(output, "  ##\n  ##\n")

    def test_L_to_dictionary(self):
        '''Inajaribu kubadilisha Rectangle kuwa kamusi.'''
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(
            r.to_dictionary(),
            {'id': 10, 'width': 10, 'height': 10, 'x': 10, 'y': 10})

    def test_M_create(self):
        '''Inajaribu kuunda Rectangle kutoka kamusi.'''
        r = Rectangle.create(**{'id': 89, 'width': 2, 'height': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 4)

    def test_N_update(self):
        '''Inajaribu kusasisha Rectangle.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_N_update_kwargs(self):
        '''Inajaribu kusasisha Rectangle kwa kutumia maneno muhimu.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=2, height=3, y=4)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 4)

    def test_N_update_invalid(self):
        '''Inajaribu kusasisha Rectangle kwa masharti yasiyo sahihi.'''
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError) as e:
            r.update(x=-2)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            r.update(y=-2)
        self.assertEqual(str(e.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as e:
            r.update(width=-2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            r.update(height=-2)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_N_update_invalid_type(self):
        '''Inajaribu kusasisha Rectangle kwa aina zisizo sahihi.'''
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError) as e:
            r.update(width="str")
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_O_save_to_file(self):
        '''Inajaribu kuokoa Rectangle kwa faili.'''
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 46)

    def test_O_save_to_file_none(self):
        '''Inajaribu kuokoa Rectangle kwa faili bila yaliyomo.'''
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_P_load_from_file(self):
        '''Inajaribu kupakia Rectangle kutoka faili.'''
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)

    def test_P_load_from_file_empty(self):
        '''Inajaribu kupakia Rectangle kutoka faili tupu.'''
        with open("Rectangle.json", "w") as f:
            f.write("[]")
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 0)

    def test_P_load_from_file_invalid_json(self):
        '''Inajaribu kupakia Rectangle kutoka faili iliyo json isiyo sahihi.'''
        with open("Rectangle.json", "w") as f:
            f.write("{this is not json}")
        with self.assertRaises(ValueError) as e:
            Rectangle.load_from_file()
        self.assertEqual(str(e.exception), "faili isiyo sahihi")


if __name__ == "__main__":
    unittest.main()

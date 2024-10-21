#!/usr/bin/python3
'''Moduli kwa ajili ya vipimo vya msingi.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Inapima darasa la Base.'''

    def setUp(self):
        '''Inaleta moduli, inaunda darasa'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Inasafisha baada ya kila mtihani.'''
        pass

    def test_A_nb_objects_private(self):
        '''Inapima kama nb_objects ni mali ya darasa ya kibinafsi.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Inapima kama nb_objects imeanzishwa kuwa sifuri.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Inapima kuanzishwa kwa Base().'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        '''Inapima saini ya mjenzi.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() inakosa hoja moja ya lazima: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        '''Inapima saini ya mjenzi na hoja 2 zisizo za self.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() inachukua kutoka 1 hadi 2 lkni 3 imepewa"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        '''Inapima ids zinazofuata.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''Inapima usawazishaji kati ya darasa na id ya mfano.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_F_id_synced_more(self):
        '''Inapima usawazishaji kati ya darasa na id ya mfano.'''
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''Inapima id ya kawaida ya int.'''
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        '''Inapima id ya kawaida ya int.'''
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_id_keyword(self):
        '''Inapima id iliyopewa kama hoja ya funguo.'''
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)
        '''Inapima saini ya to_json_string():'''
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "to_json_string() inakosa hoja moja ya lazima: 'list_dictionaries'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{"foobarrooo": 989898}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}]')

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}, {}]')

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    def test_H_test_from_json_string(self):
        '''Inapima saini ya from_json_string():'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "from_json_string() inakosa hoja moja ya lazima: 'json_string'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        s = '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"foobarrooo": 989898}]
        s = '[{"foobarrooo": 989898}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        s = '[{"x": 101, "y": 20123, "width": 312321, "id": 522244, \
"height": 34340}]'
        self.assertEqual(Base.from_json_string(s), d)

    def test_H_test_save_to_file(self):
        '''Inapima saini ya save_to_file():'''
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        Rectangle.save_to_file([r1, r2, r3])
        with open("Rectangle.json", "r") as f:
            self.assertNotEqual(f.read(), "[]")
        d = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
             {'id': 2, 'width': 1, 'height': 2, 'x': 3, 'y': 4},
             {'id': 3, 'width': 2, 'height': 3, 'x': 4, 'y': 5}]
        self.assertEqual(len(Rectangle.to_json_string(d)), len(f.read()))
        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        Square.save_to_file([r1, r2, r3])
        with open("Square.json", "r") as f:
            self.assertNotEqual(f.read(), "[]")
        d = [{'id': 1, 'size': 10, 'x': 2, 'y': 7},
             {'id': 2, 'size': 1, 'x': 3, 'y': 2},
             {'id': 3, 'size': 2, 'x': 4, 'y': 3}]
        self.assertEqual(len(Square.to_json_string(d)), len(f.read()))

    def test_I_test_load_from_file(self):
        '''Inapima saini ya load_from_file():'''
        with self.assertRaises(FileNotFoundError):
            Base.load_from_file()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        Rectangle.save_to_file([r1, r2, r3])
        lst = Rectangle.load_from_file()
        self.assertEqual(len(lst), 3)
        self.assertIsInstance(lst[0], Rectangle)
        self.assertEqual(lst[0].width, 10)
        self.assertEqual(lst[0].height, 7)
        self.assertEqual(lst[1].width, 1)
        self.assertEqual(lst[1].height, 2)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        Square.save_to_file([r1, r2, r3])
        lst = Square.load_from_file()
        self.assertEqual(len(lst), 3)
        self.assertIsInstance(lst[0], Square)
        self.assertEqual(lst[0].size, 10)
        self.assertEqual(lst[0].x, 2)
        self.assertEqual(lst[0].y, 7)
        self.assertEqual(lst[1].size, 1)
        self.assertEqual(lst[1].x, 3)
        self.assertEqual(lst[1].y, 2)

    def test_J_test_create(cls):
        '''Inapima saini ya create():'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        r1 = Square(10, 7, 2)
        r2 = Square.create(**r1.to_dictionary())
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.size, r2.size)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)

    def test_K_create_return_type(self):
        '''Inapima saini ya create():'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsInstance(r2, Rectangle)
        r1 = Square(10, 7, 2)
        r2 = Square.create(**r1.to_dictionary())
        self.assertIsInstance(r2, Square)


if __name__ == '__main__':
    unittest.main()

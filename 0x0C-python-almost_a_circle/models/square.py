#!/usr/bin/python3
'''Moduli ya darasa la Square.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Darasa la Square.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Mjenzi.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Inarudisha taarifa ya maandiko kuhusu mraba huu.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Ukubwa wa mraba huu.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Njia ya ndani inayosasisha sifa za mfano kupitia */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Inasasisha sifa za mfano kupitia args zisizo na funguo
            na funguo za nenosiri.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Inarudisha uwakilishi wa kamusi wa darasa hili.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}

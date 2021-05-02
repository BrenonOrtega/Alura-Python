my_lista = [
    ('i1', 'a'),  ('i2', 'my_obj.property'),   ('i3','c'), 
    ('i4', None), ('i5', None), ('i6', None),
    ('i7', None), ('i8', None)
]

class myClass:
    def __init__(self, **kwargs):
        my_list = [(key, value) for key, value in kwargs.items() if value != None]
        return my_list

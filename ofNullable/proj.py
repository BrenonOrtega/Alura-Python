
def func(a='', b='', c='', d='', e='', f='',g='', h=''):
    print(a,b,c,d,e,f,g,h)


a = func('a','b','c')

my_lista = [
    ('i1', 'a'),  ('i2', 'my_obj.property'),   ('i3','c'), 
    ('i4', None), ('i5', None), ('i6', None),
    ('i7', None), ('i8', None)
]

class myClass:
    def __init__(self, **kwargs):
        my_list = [(key, value) for key, value in kwargs.items() if value != None]
        return my_list
        pass

    def itera(self, lista):
        novo_dicionario = list()

        #for (i=0; i < lista.size; i++):
        for i in range(len(lista)):
            if lista[i][1] != None:
                novo_dicionario.append( {lista[i], lista[i][1] } )

            else: 
                lista[i][1].update('')
                novo_dicionario.append( {lista[i], lista[i][1] } )
            print(novo_dicionario)
          
a = myClass(item1='a', item2='b', item3='c', item4=None, item5=None, item6=None,item7=None, item8=None)

b = myClass()
b.itera(my_lista)


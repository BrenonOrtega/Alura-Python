# Recursively tranforms a dictionary in a python object
# lists not included.
from collections import namedtuple
def dictToObject(d):
    for k,v in d.items():
        if isinstance(v, dict):
            d[k] = dictToObject(v)
    return namedtuple('object', d.keys())(*d.values())


'''    
my_dict={
            'a': {
                    'aa':{ 'aaa':1, 'aab':2, 'aac':3   }, 
                    'ab':{ 'aba':1, 'abb':2, 'abc':3  },
                    'ac':{ 'aca':1, 'acb':2, 'acc':3  }
                },
            'b':
                {   'ba':{ 'baa':1, 'bab':2, 'bac':3 }, 
                    'bb':{ 'aba':1, 'abb':2, 'abc':3 },
                    'bc':{ 'bca':1, 'bcb':2, 'bcc':3 }   
                },
            'c':[
                    {  'c0a': {'c0aa':1, 'c0ab':2, 'c0ac':3},
                        'c0b': {'c0ba':1, 'c0bb':2, 'c0bc':3},
                        'c0c': {'c0ca':1, 'c0cb':2, 'c0cc':3},
                    },
                    {   'c1a': {'c1aa':1, 'c1ab':2, 'c1ac':3},
                        'c1b': {'c1ba':1, 'c1bb':2, 'c1bc':3},
                        'c1c': {'c1ca':1, 'c1cb':2, 'c1cc':3},
                    },
                    {   'c2a': {'c2aa':1, 'c2ab':2, 'c2ac':3},
                        'c2b': {'c2ba':1, 'c2bb':2, 'c2bc':3},
                        'c2c': {'c2ca':1, 'c2cb':2, 'c2cc':3},
                    }
                ],       
        }
# namedtuple transforma um dicionário em um objeto com a classe definida
# porém não transforma listas ou objectos aninhados.
namedtuple_example = namedtuple("nome_objeto", my_dict.keys())(*my_dict.values())
print(namedtuple_example)

my_obj = dictToObject(my_dict)
def printall():
    print('my_obj.a:',my_obj.a)
    print('my_obj.b:',my_obj.b)
    print('my_obj.c[1]:',my_obj.c[1])
    print('my_obj.c[1][\'c1a\']'':', my_obj.c[1]['c1a'])
    print('my_obj.c[1][\'c1a\'][\'c1aa\']:', my_obj.c[1]['c1a']['c1aa'])

printall()
'''




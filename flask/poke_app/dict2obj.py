from collections import namedtuple

my_dict={
        'a':
            {
                'aa':{
                        'aaa':1, 
                        'aab':2, 
                        'aac':3
                    }, 
                'ab':{
                        'aba':1, 
                        'abb':2, 
                        'abc':3
                    },
                'ac':{
                        'aca':1,
                        'acb':2,
                        'acc':3
                    }
            },
        'b':
            {
                'ba':{
                        'baa':1, 
                        'bab':2, 
                        'bac':3
                    }, 
                'bb':{
                        'aba':1, 
                        'abb':2, 
                        'abc':3
                    },
                'bc':{
                        'bca':1,
                        'bcb':2,
                        'bcc':3
                    }
            },
        }

my_obj = namedtuple("teste", my_dict.keys())(*my_dict.values())

print(my_dict)
print(my_obj)

#Another solution:
def dictToObject(d):
    for k,v in d.items():
        if isinstance(v, dict):
            d[k] = dictToObject(v)
            print(d[k])
    return namedtuple('object', d.keys())(*d.values())


a = dictToObject(my_dict)
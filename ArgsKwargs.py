# *args, arguments

def add(*args):
    print(args)

add(7,8,5,6,7,89)

a = [5,6,7,8,9]
b = [1,2,*a,3,4]
print(b)


def sum2(*args):
    total = 0
    for n in args:
        total+=n 
    print(f"Сумма: {total}")

sum2(4,5,5,6,7,8,9,0,5,6,7,90)


# **kwargs KEYWORD ARGUMENTS - DICT {KEY:VALUE} 
def show(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")

show(name='Mao', age=17, birth='12.12.2000', city="Bishkek")


def pets(owner, **kwargs):
    print(f"Хозяин: {owner}")
    for k,v in kwargs.items():
        print(k,v)

pets('Zahid', dog='Bobik', cat='bruda', eats=['fish', 'meat', 'water'])

# Комбинация
#I)оператор **kwargs нельзя писать до *args, если сделаете то будет ошибка
#II) мы конечно же можем писать не только args и kwargs, но и совсем другими словами, но общепринятые правила говорят чтобы писали именно так *args и **kwargs
def demo(*args, **kwargs): 
    print('args =',args)
    print('kwargs=',kwargs)

demo(43, 3,4,5,6,7,56,7,8,9, age=45, hobbi='гимнастика', phone='redmi')


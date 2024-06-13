import random
from decimal import Decimal
from fractions import Fraction


class Worker:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    random_value = random.random()
    random_value_1 = random.randrange(10000)
    random_choice_1 = random.choice(
        ['Life of Brian', 'Holy Grail', 'Meaning of Life'])

    suits = ['hearts', 'clubs', 'diamonds', 'spades']
    random.shuffle(suits)
    print(suits)

    # Other numeric types
    # 1. Decimal Points
    false_result = 0.1 + 0.1 + 0.1 - 0.3
    right_result = Decimal('0.1') + Decimal('0.1') + \
        Decimal('0.1') - Decimal('0.3')

    print(false_result, ',', right_result)

    # 2. Fraction Types
    y = Fraction(3, 9)
    x = Fraction(1, 10)
    print(x, y, x*y)

    m = Fraction(.25)
    n = Fraction(.75)

    print(m, m+n)
    # Fraction conversion and mixed types
    f = 2.5
    z = Fraction(*f.as_integer_ratio())
    print(z)
    print(float(z))
    print(*(1.23).as_integer_ratio())

    # 3. Sets
    """
        -Unordered
        -Never Sequences
    """
    x = set('abcdefghijklmnopqrstuvwxyz')
    y = set('mnheyuo')
    z = x.intersection(y)
    z.add('MABY')
    # z.remove('b')

    for item in z:
        print(item*3)

    print(x-y)
    print(x | y)
    print(x & y)
    print(x ^ y)

    print("e" in x)
    print(z.union([1, 3, 6, "g"]))

    set_of_numbers = {1, 2, 3, 4, 5, 6}
    superset = set_of_numbers > {3, 4}  # superset

    print(superset)
    print({1, 5, 3, 6} | set_of_numbers)  # Union
    {1, 2, 3}.union({3, 4})
    {1, 2, 3}.union(set([3, 4]))

    print({1, 5, 3, 6} & set_of_numbers)  # intersection
    print({1, 2, 3}.intersection((1, 3, 5)))
    print((1, 2, 3) in set_of_numbers)  # Membership

    set_of_numbers.add("Ba")

    # Set Comprehension
    """ 
        -coded in curly braces run to make a set instead of a list. 
        Set comprehensions run a loop and collect the result of an expression on each iteration; a loop variable gives
        access to the current iteration value for use in the collection expression.
    """
    comprehension_1 = {x ** 2 for x in [1, 2, 3, 4, 5, 6, 7, 10]}
    print(comprehension_1)

    set_of_collected_exp = {c * 4 for c in 'spam'}
    print(set_of_collected_exp)

    # sets can be used to filter duplicates
    L = [1, 2, 1, 3, 2, 4, 5]
    set_l = set(L)
    L = list(set_l)
    print(L)

    # Arragement may differ
    m = list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa']))
    print(m)
    # Can be used to isolate list and string differences
    list_diff = set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6])
    string_diff = set('abcdefg') - set('abdghij')
    set_list_diff = set('spam') - set(['h', 'a', 'm'])

    L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
    print(L1 == L2)  # false- order matters
    print(set(L1) == set(L2))
    print(sorted(L1) == sorted(L2))
    print('spam' == 'asmp', set('spam') == set(
        'asmp'), sorted('spam') == sorted('asmp'))

    engineers = {'bob', 'sue', 'ann', 'vic'}
    managers = {'tom', 'sue'}
    print('bob' in engineers)
    print(engineers | managers)
    print(engineers - managers)
    print({'bob', 'sue'} < engineers)  # Are both engineers?(subset)
    print(managers ^ engineers)  # In one but not the other
    # All people is a superset of managers
    print((managers | engineers) > managers)
    print((managers | engineers) - (managers ^ engineers))  # Intersection

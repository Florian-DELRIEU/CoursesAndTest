import MyPack.Utilities as util
import numpy as np
"""
-- High order function: HOfunc(func,arg). Une fonction et l'argument de cette fonction

-- map(func,list): applique la fonction :func: a tout les éléments de :list:
-- filter(filter,list): filtre tout les éléments de :list: 

-- generator: yield retourne une variable à chaque itération (Mettre en liste ou autre pour utiliser un générateur)
    print(  i for i in nums  )          # WRONG
    print(  list(i for i in nums)  )    # GOOD list(generator)
    print(  [i for i in nums
             if i%2==0       ])
"""

case = "itertools"
util.AskUser("Wich case would you run ? ",case)

def apply_twice( func, arg):  #high order function
    """
    High order functions
    """
    return func( func(arg) )
def add_five(x):
    return x+5
def countdown(a): # generator
    while a > 0:
        yield a  # return a value from generator
        a -= 1
def odd_number(limit):
    i = 0
    while i < limit:
        if i % 2 == 0:  yield i
        i += 1
arr = np.arange(0,21,1)
nums = list(arr[:10])
words = ["a","b","c","+++"]

if case == 1:
    print(apply_twice(add_five,5))  # add_five( add_five (x) )
    print(apply_twice( lambda x: x**2 , 5) )

if case == 2:
    'Lambdas functions'
    print( (lambda x: x**2) (-2) )  # Correct syntaxe       ( 4 )
    print(  lambda x: x**2  ,-2  )  # Incorrect syntaxe     ( <function <lambda> at 0x067E4F58> -2 )
    print("-----------------")
    square = lambda x: x*x
    print(square(4))

if case == "map/filters":
    result = map(add_five,nums)         # Incorrect !
    print(result)
    result = list(map(add_five,nums))   # Correct !
    print(result)
    print( list(map(add_five,nums)) )
    print("-----------------")
    print( list(filter(lambda x: x%2==0,nums)))  # n'affiche que les nombre pairs

if case == "generators":
    print(countdown(10))
    print(countdown,10)
    for i in countdown(10):
        print(i)
    print("-----------------")
    print(list(countdown(10)))
    print(list(odd_number(10)))
    print("-----------------")
    print(  list(i for i in nums)  )
    print(  [i for i in nums        # for each int()
                if i%2==0       ])

if case == "decorators":
    def decor(func):
        def wrap():
            print("=============")
            func()
            print("=============")

        return wrap
    def print_text():
        print("Hello world")

    decor(print_text)()

    print("-----------------")

    @decor  # modifie la fonction directement en dessous avec decor()
    def print_text():
        print("Hello world")

    def print_text2():
        print("Hello world")

    print_text()
    print_text2()

if case == "recursion":
    def factorial(x):
        if x==1:    return 1  # "base case" (the case that not calls the function) factorial(1) = 1
        else:       return x*factorial(x-1)
    print(factorial(5))
    print("-----------------")
    def factorial2(x): # no "base case" so the function return an error when factorial(x-1=0)
        return x*factorial2(x-1)
#    print(factorial2(5))

    def is_even(x):
        if x == 0:  return True
        else:       return is_odd(x-1)
    def is_odd(x):
        return not is_even(x)
    print(is_odd(17))

    def fib(x):
        if x==0 or x==1:    return 1
        else:               return fib(x-1) + fib(x-2)
    print(fib(4))

if case == "sets":
    a = {1,2,4,1,6,5,3,4}
    b = {1,2,7,9,8,5,3,6}
    print(a) # duplicate are not showed and show in order
    print(a | b) # show (a AND b)
    print(a & b) # show in(a and b)
    print(a - b) # in a but not in b
    print(b - a) # in b but not in a
    print(a ^ b) # in a OR in b only

if case == "itertools":
    from itertools import count, cycle
    for i in count(1):
        if i >= 5: break
        else:       print(i)
    i = 0
    for el in cycle(words):
        print(el)
        i += 1
        if i == 10: break
    print("-----------------")

    from itertools import accumulate, takewhile, chain
    nums2 = list(accumulate(range(8))) # somme cumulé de longueur 8
    print(nums2)
    test_list = list(np.arange(8))
    for i,el in enumerate(test_list): # == list(accumulate(range(8)))
        if i != 0: el += test_list[i-1]
        test_list[i] = el
    print(test_list)
    print(list( takewhile( lambda x: x<=6 , nums) ))
    print(list(chain(arr[:10],arr[10::-1]))) # = list(list(arr[:10]) + list(arr[10::-1])
    print("-----------------")

    from itertools import product, permutations
    a = words[:-1]
    b = range(2)
    print(list(  product(a,b )  )) # permute elements of the list with
    print(list(  permutations(a)  ))  # permute elements of the list
    print("-----------------")

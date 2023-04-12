import numpy as np

case = 7
##########################################################################
if case ==1:
    A = np.array([1,2,3,4])
    a = np.array(45)
    B = np.array([
        [1,2,3],
        [4,5,6]
    ])
    C = np.array([  # array ordre 3 (i,j,k)
        [ #k = 0
            [1,2,3], #i=1
            [3,4,5]  #i=2
        ],[# k = 1
            [10,11,12], #i=1
            [13,14,15]  #i=2
        ]
    ])

    print("B.shape: ", B.shape)
    print("B.ndim: ", B.ndim)
    print("len(B): ", len(B))
    print("B[ligne , colonne]")
    print(B[1,2])
    print("C[tableau(k),ligne,colonne]")
    print(C[1,:,:])
##########################################################################
if case ==2:
    """
    arr[0, 1, 2] prints the value 6.

    And this is why:
    
    The first number represents the first dimension, which contains two arrays:
    [[1, 2, 3], [4, 5, 6]]
    and:
    [[7, 8, 9], [10, 11, 12]]
    Since we selected 0, we are left with the first array:
    [[1, 2, 3], [4, 5, 6]]
    
    The second number represents the second dimension, which also contains two arrays:
    [1, 2, 3]
    and:
    [4, 5, 6]
    Since we selected 1, we are left with the second array:
    [4, 5, 6]
    
    The third number represents the third dimension, which contains three values:
    4
    5
    6
    Since we selected 2, we end up with the third value:
    6
    """ #Exemple explain
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print("arr[0]: ",arr[0])
    print("arr[0] == arr[0,:]: ",arr[0] == arr[0,:])
    print("arr[:,0]: ",arr[:,0])
    print('2nd element on 1st dim: ', arr[0, 1])

    arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print("arr2[0, 1, 2]: ",arr2[0, 1, 2])
##########################################################################
if case ==3:
    """
    Slicing in python means taking elements from one given index to another given index.
    - We pass slice instead of index like this: [start:end].
    - We can also define the step, like this: [start:end:step].
    If we don't pass start its considered 0
    If we don't pass end its considered length of array in that dimension
    If we don't pass step its considered 1
    """
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    B = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print(arr[1:5])
    print(arr[4:])

    arr2 = [arr] # = list [ array, 2 ]
    arr2 = np.array([arr]) # = array [ array, 2 ]
    arr2 = np.array(arr[:]) # arr2 == arr
    arr2 = np.array([
        arr[:],
        10 + arr[:]
    ]) # array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("arr[-3:-1]: ",arr[-3:-1])
    print("arr[::2]: ",arr[::2])
##########################################################################
if case == 4:
    arr = np.array([1, 2, 3, 4, 5])

    x1 = arr.copy()
    x2 = arr.view()
    x3 = arr # = arr.view()
    arr[0] = 42
    print(arr)
    print(x1)
    print(x2)
    print(x3)
##########################################################################
if case ==5:
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    newarr = arr.reshape(4, 3)  # newarr.shape(4*3) = arr.shape(12*1)
    newarr2 = arr.reshape(2, 2, 3)  # newarr.shape(2*2*3) = arr.shape(12*1)
    newarr3 = arr.reshape(2, 2, -1)  # newarr.shape(2*2* x) = arr.shape(12*1) calcul de x tout seul
    print(newarr3)

    print("newarr3.reshape(-1): ", newarr3.reshape(-1))
##########################################################################
if case == 6:
    arr = np.array([3, 2, 0, 1])
    string_arr = np.array(['banana', 'cherry', 'apple'])
    print(np.sort(arr))
    print(np.sort(string_arr))

    arr = np.array([[3, 2, 4], [5, 0, 1]])
    print(np.sort(arr))
##########################################################################
if case == 7:
    arr = np.array([41, 42, 43, 44])
    x = [True, False, True, False]
    newarr = arr[x]
    print(newarr)

    filter_arr = arr > 42 # array([False, False,  True,  True])
    newarr = arr[filter_arr]
    print(filter_arr)
    print(newarr)
# From https://anandology.com/python-practice-book/

def exp(x, n):
    """Computes x raised to the power of n.

    >>> exp(2, 3)
    8
    >>> exp(3, 2)
    9
    """

    if n == 0:
        return 1
    else:
        return x * exp(x, n - 1)

def f_exp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return f_exp(x * x, n / 2)
    else:
        return x * f_exp(x, n - 1)

def product(a, b):
    product = 0
    for i in range(b):
        product += a
    return product

def f_prod(a, b):
    if b == 1:
        return a
    else:
        return a + f_prod(a, b - 1)

def flatten_list(a, result=None):
    """Flattens a nested list.

    >>> flatten_list([[1, 2, [3, 4]], [5, 6], 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    if result is None:
        result = []

    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)

    return result

def flatten_dict(a, result=None):
    # ????
    """Flattens a nested dict.

    flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    """
    if result is None:
        result = {}

    for x in a:
        print("x: {}".format(x))
        if isinstance(a[x], dict):
            print("this is a dict: {}".format(x))
            newkeys = []
            for j in a[x]:
                newkeys.append(".".join([x, j]))

                #print("jkey: {}".format(jkey))
                #result[jkey] = a[x][j]
                #print("This {} goes here: result[{}]".format(a[x][j], jkey))
            flatten_dict(a[x], result)
        else:
            result[x] = a[x]

    return result

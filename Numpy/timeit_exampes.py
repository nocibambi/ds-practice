import timeit
print(timeit.timeit('1+3', number=500000))

print(timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = list(i for i in input_list if div_by_two(i))
''', number=50000))

print(timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = [i for i in input_list if div_by_two(i)]''', number=50000))

print(timeit.timeit('''input_list = range(500)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

        # generator:
        xyz = list(i for i in input_list if div_by_two(i))
        ''', number=50000))

print(timeit.timeit('''input_list = range(500)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

        # generator:
        xyz = [i for i in input_list if div_by_two(i)]''', number=50000))

# "list comprehension is in theory faster since the list is in memory,
# BUT this is only true if you're not building a new list."

print(timeit.timeit('''input_list = range(500)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

        # generator:
        xyz = (i for i in input_list if div_by_two(i))
        ''', number=50000))

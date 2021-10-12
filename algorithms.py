import random
import inspect


def input_arguments_decorator(function):
    def wrapper(*args, **kwargs):

        function_signature = inspect.signature(function)
        kparams = {}

        index = 0
        for parameter in function_signature.parameters:

            default_value = function_signature.parameters[parameter].default

            if (index < len(args)):
                kparams[parameter] = args[index]
            elif kwargs.get(parameter):
                kparams[parameter] = kwargs[parameter]
            elif default_value is not inspect._empty:
                kparams[parameter] = default_value
            else:
                print('enter', parameter + ': ', end='')
                value = input()
                try:
                    kparams[parameter] = int(value)
                except ValueError:
                    kparams[parameter] = value

            index += 1

        return function(**kparams)

    return wrapper


def binary_search(list, item):
    def left_bound(list, item):

        left = -1
        right = len(list)

        while right - left > 1:
            middle = (right + left) // 2
            if list[middle] < item:
                left = middle
            else:
                right = middle

        return left

    def right_bound(list, item):

        left = -1
        right = len(list)

        while right - left > 1:
            middle = (right + left) // 2
            if list[middle] <= item:
                left = middle
            else:
                right = middle

        return right

    return left_bound(list, item), right_bound(list, item)


# def test_binary_serach():
#
#     print('test_binary_search:')
#     random_range = 0, 15
#     item = random.randint(*random_range)
#     list = random_list(*random_range)
#     list.sort()
#
#     print('список:' + str(list), 'искомый элемент:' + str(item), sep='\n')
#     print("результат:", binary_search(list, item))


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b) if a > b else gcd(a, b % a)


def invert_array(list):
    for k in range(len(list) // 2):
        list[k], list[-k - 1] = list[-k - 1], list[k]


# def test_invert_array():
#     print('test_invert_array')
#     list = random_list()
#     print(list)
#     invert_array(list)
#     print(list)


# def test_sort(function):
#     list = random_list(2, 15, 10)
#     print(list)
#     print(function(list))


def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


class List(list):

    @input_arguments_decorator
    def random(self, n, l, r, u=True):

        self.clear()

        for i in range(n):

            while True:
                r_v = random.randint(l, r)
                if not u or (not self.count(r_v)):
                    self.append(r_v)
                    break

    def sort(self, method=''):

        def buble(arr):
            for k in range(len(arr)):
                for i in range(len(arr) - k - 1):
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]

        def insert(arr):
            if len(arr) <= 1:
                return arr

            for i in range(1, len(arr)):
                k = i
                while arr[k] < arr[k - 1] and k > 0:
                    arr[k], arr[k - 1] = arr[k - 1], arr[k]
                    k -= 1

        def choise(arr):
            for k in range(len(arr)):
                min = k
                for i in range(k + 1, len(arr)):
                    if arr[min] > arr[i]:
                        min = i
                arr[k], arr[min] = arr[min], arr[k]

        def merge(arr):

            def sort(arr):

                def merge_lists(arr1, arr2):

                    result = [0] * (len(arr1) + len(arr2))

                    x = y = z = 0
                    while x < len(arr1) and y < len(arr2):
                        if arr1[x] < arr2[y]:
                            result[z] = arr1[x]
                            x += 1
                        else:
                            result[z] = arr2[y]
                            y += 1
                        z += 1

                    while x < len(arr1):
                        result[z] = arr1[x]
                        z += 1
                        x += 1

                    while y < len(arr2):
                        result[z] = arr2[y]
                        z += 1
                        y += 1

                    return result

                if len(arr) <= 1:
                    return arr

                mid = len(arr) // 2
                left = sort(arr[:mid])
                right = sort(arr[mid:])

                return merge_lists(left, right)

            sorted_arr = sort(self)

            for i in range(len(arr)):
                arr[i] = sorted_arr[i]

        if method == '':
            super().sort()
        else:
            sort_func = locals().get(method)
            sort_func(self)


l = List()
l.random(10, 0, 9)
print(l)
l.sort('merge')
print(l)

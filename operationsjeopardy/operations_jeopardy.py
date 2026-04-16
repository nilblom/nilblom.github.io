import math
import copy
import itertools
from math import factorial

numbers = ['2', '4', '6', '8']
ops = ['+', '-', '*', '/']
ops_unary = ['sqrt', '3rt', '!', 'dfactorial', '']

def find_expression_left(s, i):  # i marks the behind of ')'
    level = 1
    while i >= 0:
        if s[i] == ')':
            level += 1
        if s[i] == '(':
            level -= 1
            if level == 0:
                return i
        i -= 1
    return -1

def find_expression_right(s, i):  # i marks the front of '('
    level = 1
    while i < len(s):
        if s[i] == '(':
            level += 1
        if s[i] == ')':
            level -= 1
            if level == 0:
                return i
        i += 1
    return -1

def group_expressions(s):
    s1 = copy.copy(s)
    i = 0
    while i < len(s1):
        if s1[i] in ['*', '-', '/']:
            k = i

            j = find_expression_left(s1, i-2)
            if j > -1 and find_expression_right(s1, i) == i+2:
                pass
            elif s1[i-1] == ')':
                s1.insert(find_expression_left(s1, i-2), '(')
            else:
                s1.insert(i-1, '(')
            i += 1

            j = find_expression_right(s1, i)
            if j > -1 and find_expression_right(s1, i) == k+2:
                pass
            elif s1[i+1] == '(':
                s1.insert(find_expression_right(s1, i+2), ')')
            else:
                s1.insert(i+2, ')')

        i += 1

    return s1

s = ['8', '*', '4']
s1 = group_expressions(s)
assert s1 == ['(', '8', '*', '4', ')']

s = ['8', '*', '4', '*', '3']
s1 = group_expressions(s)
assert s1 == ['(', '(', '8', '*', '4', ')', '*', '3', ')']

s = ['(', '8', '*', '4', ')', '*', '3']
s1 = group_expressions(s)
assert s1 == ['(', '(', '8', '*', '4', ')', '*', '3', ')']

s = ['(', '8', '*', '4', ')', '*', '(', '3', '+', '2', ')']
s1 = group_expressions(s)
assert s1 == ['(', '(', '8', '*', '4', ')', '*', '(', '3', '+', '2', ')', ')']

s = ['(', '2', '/', '2', '+', '6', ')', '+', '8']
s1 = group_expressions(s)
assert s1 == ['(', '(', '2', '/', '2', ')', '+', '6', ')', '+', '8']

def dfactorial(n):
    if n == 0:
        return 1
    product = 1
    for i in range(n, 0, -2):   
        product *= i
    return product

assert dfactorial(3) == 3
assert dfactorial(4) == 8
assert dfactorial(1) == 1
assert dfactorial(5) == 15

def insert_parentheses(s):
    results = [s]
    i = 0
    while i < len(s)-2:
        s1 = copy.copy(s)
        s1.insert(i, '(')
        s1.insert(i+4, ')')
        results.append(s1)
        i += 2
    return results

s = ['2', '+', '4', '*', '6', '+', '8']
S = insert_parentheses(s)
assert S == [['2', '+', '4', '*', '6', '+', '8'],
             ['(', '2', '+', '4', ')', '*', '6', '+', '8'],
             ['2', '+', '(', '4', '*', '6', ')', '+', '8'],
             ['2', '+', '4', '*', '(', '6', '+', '8', ')']]

def apply_operators(p):
    i = 0
    while i < len(p):
        if p[i] == 'sqrt':
            p[i] = p[i+1] + "**(1/2)"
            p.pop(i+1)
        elif p[i] == '3rt':
            p[i] = p[i+1] + "**(1/3)"
            p.pop(i+1)
        elif p[i] == '!':
            p[i] = "factorial(" + p[i+1] + ")"
            p.pop(i+1)
        elif p[i] == 'dfactorial':
            p[i] = "dfactorial(" + p[i+1] + ")"
            p.pop(i+1)
        else:
            i += 1

def remove_empty_string(p):
    while '' in p:
        p.remove('')

def expression_to_list(s):
    s1 = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            end = find_expression_right(s, i+1)
            sublist = s[i+1:end]
            items = expression_to_list(sublist)
            s1.append(items)
            i = end+1
        else:
            s1.append(s[i])
            i += 1
    return s1

def compare(a, b):
    if type(a) == list and type(b) == list:
        if len(a) > len(b):
            return 1
    elif type(a) == list:
        return 1
    elif type(b) == list:
        return 0
    else:
        return a > b
        
def swap(s, i, j):
    copy = s[j]
    s[j] = s[i]
    s[i] = copy

def find_max(s):
    max = 0
    i = 0
    while i < len(s):
        if compare(s[i], s[max]) == 1:
            max = i
        i += 1
    return max

def list_sort(s):
    i = 0
    while i < len(s):
        if i+1 < len(s) and s[i+1] in ['-', '/']:
            i += 3
            continue
        max = find_max(s[i:])
        swap(s, i, i+max)
        if type(s[i]) == list:
            list_sort(s[i])
        i += 1

s = ['6', '-', '8']
list_sort(s)
assert s == ['6', '-', '8']

a = ['6', '+', '(', '8', '*', '2', ')', '+', '4']
b = ['4', '+', '(', '8', '*', '2', ')', '+', '6']
a1 = expression_to_list(a)
b1 = expression_to_list(b)
list_sort(a1)
list_sort(b1)
assert a1 == b1

a = ['(', '8', '*', '2', ')', '+', '4', '+', '6']
b = ['4', '+', '6', '+', '(', '8', '*', '2', ')']
a1 = expression_to_list(a)
b1 = expression_to_list(b)
list_sort(a1)
list_sort(b1)
assert a1 == b1

a = ['4', '+', '6', '+', '(', '8', '*', '2', ')']
b = ['(', '2', '*', '8', ')', '+', '4', '+', '6']
a1 = expression_to_list(a)
b1 = expression_to_list(b)
list_sort(a1)
list_sort(b1)
assert a1 == b1

def list_to_expression(e):
    s = []
    for d in e:
        if type(d) == list:
            s.append('(')
            s.extend(list_to_expression(d))
            s.append(')')
        else:
            s.append(d)
    return s

e = [['4', '*', '6'], '*', '8']
s = list_to_expression(e)
assert s == ['(', '4', '*', '6', ')', '*', '8']

def is_equal(s1, s2):
    s1 = expression_to_list(s1)
    s2 = expression_to_list(s2)
    list_sort(s1)
    list_sort(s2)
    return s1 == s2

s1 = ['(', '(', '8', '*', '6', ')', '/', '4', ')', '+', '2']
assert is_equal(s1, s1) == True

def solve():
    solutions = []
    permutations = itertools.permutations(numbers)

    for numbers_p in permutations:

        products = list(itertools.product(
            ops_unary,
            [numbers_p[0]],
            ops,
            ops_unary,
            [numbers_p[1]],
            ops,
            ops_unary,
            [numbers_p[2]],
            ops,
            ops_unary,
            [numbers_p[3]]
        ))

        for p in products:
            p = list(p)
            apply_operators(p)
            s = "".join(p)
            t = copy.copy(p)
            remove_empty_string(p)
            r = insert_parentheses(p)
            for r1 in r:
                try:
                    x = eval("".join(r1))
                except OverflowError, ZeroDivisionError:
                    continue
                if x == 26:
                    r2 = group_expressions(r1)
                    solutions.append(r2)

    print("Filtering solutions... (%d)" % len(solutions))

    i = 0
    while i < len(solutions):
        s1 = solutions[i]
        j = i+1
        while j < len(solutions):
            s2 = solutions[j]
            if i != j and is_equal(s1, s2):
                solutions.pop(j)
            else:
                j += 1
        i += 1

    print("Found", len(solutions), "solutions")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "-c":
        solve()



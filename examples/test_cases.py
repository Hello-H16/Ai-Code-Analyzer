# examples/test_cases.py

# 1. Recursion without return (common mistake)
recursion_bug = '''
def factorial(n):
    if n == 0:
        return 1
    else:
        factorial(n - 1)
'''

#  2. Proper recursion
recursion_correct = '''
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n
'''

#  3. Infinite loop (for future detection)
infinite_loop = '''
def loop_forever():
    while True:
        print("Running...")
'''

#  4. Linear search (working fine)
linear_search = '''
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
'''

#  5. Binary search (bug: wrong mid calculation)
binary_search_bug = '''
def binary_search(arr, target):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
'''

#  6. Missing return in recursive Fibonacci
fibonacci_bug = '''
def fibonacci(n):
    if n <= 1:
        return n
    fibonacci(n - 1) + fibonacci(n - 2)
'''

# Dictionary to easily select test cases
test_cases = {
    "recursion_bug": recursion_bug,
    "recursion_correct": recursion_correct,
    "infinite_loop": infinite_loop,
    "linear_search": linear_search,
    "binary_search_bug": binary_search_bug,
    "fibonacci_bug": fibonacci_bug
}

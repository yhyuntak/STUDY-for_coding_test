def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n):
    # return 을 통해서 쫙 실행되고 찹찹찹 올라가는 느낌.
    if n <= 1 :
        return 1
    # n! = n * (n-1)!

    return n*factorial_recursive(n-1)

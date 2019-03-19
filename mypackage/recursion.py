def sum_array(array):
    total=0
    for i in array:
        total+=i
    return total


    '''Return sum of all items in array'''

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):

    '''Return n!'''
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)


def reverse(word):

    '''Return word in reverse'''
    word_new=list(word)
    rev=[]

    for i in range(1,len(word_new)+1):
        rev.append(word_new[(-i)])

    reversedone="".join(rev)
    return reversedone

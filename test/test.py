from mypackage import recursion,recursion

def sum_array():
    """
    make sure my functions work
    """

    assert recursion.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'
    assert recursion.sum_array([10, 1, 12, 9, 2]) == 34, 'incorrect'
    assert recursion.sum_array([1, 2, 3, 4, 5]) == 15, 'incorrect'

def fibonacci():
    """
    make sure my functions work
    """

    assert recursion.fibonacci(1) == 1, 'incorrect'
    assert recursion.fibonacci(8) == 21, 'incorrect'

def factorial():
    """
    make sure my functions work
    """

    assert recursion.factorial(1) == 1, 'incorrect'
    assert recursion.factorial(8) == 40320, 'incorrect'

def reverse():
    """
    make sure my functions work
    """

    assert recursion.reverse('spend') == 'dneps', 'incorrect'
    assert recursion.reverse('car') == 'rac', 'incorrect'

def bubble_sort():
    """
    make sure my functions work
    """

    assert sorting.bubble_sort([97, 200, 100, 101, 211, 107]) == [97, 100, 101, 107, 200, 211], 'incorrect'
    assert sorting.bubble_sort([3,1,4,2,5]) == [1,2,3,4,5], 'incorrect'

def merge_sort():
    """
    make sure my functions work
    """

    assert sorting.merge_sort([97, 200, 100, 101, 211, 107]) == [97, 100, 101, 107, 200, 211], 'incorrectincorrect'
    assert sorting.merge_sort([3,1,4,2,5]) == [1,2,3,4,5], 'incorrect'

def quick_sort():
    """
    make sure my functions work
    """

    assert sorting.quick_sort([97, 200, 100, 101, 211, 107]) == [97, 100, 101, 107, 200, 211], 'incorrect'
    assert sorting.quick_sort([3,1,4,2,5]) == [1,2,3,4,5], 'incorrect'

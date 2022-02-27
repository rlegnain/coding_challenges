"""
Minimum Addition
=================

Find the minimum possible sum of P1 and P2 for a any positive integer number N. Where P1 and P2 are the digits in the number N.

Note: The order of occurrence of the digits in P1 and P2 may differ from the order of occurrence of the digits in N.


example:
N = 4325

results:
one possible solution is:
P1 = 25
P2 =34

the minimum sum is 59

- Note there are possiblities of P1 and P2 like (43, 25), (3, 245), (53, 25), ect but their sum is not minimum
Thus the answer is 59

"""

def solve1(N):
    """This method uses all possible numbers."""
    assert isinstance(N, int)
    assert 10 <= N <= 2e18
    
    # convert interger to sorted list of its digit
    N_as_list_ordered = sorted([x for x in str(N)])
    sumation = 2e18
    permu_list = permutations(N_as_list_ordered)
    # print(list(permu_list))
    for permu in permu_list:
        for index in range(len(permu)-1):
            P1_s = "".join(permu[:index+1])
            P2_s = "".join(permu[index+1:])
            temp = int(P1_s) + int(P2_s)
            if temp<sumation:
                P1 = int(P1_s) 
                P2 = int(P2_s)
                sumation = temp
    print("{} + {} = {}".format(P1, P2, sumation))


def solve2(N):
    """
    very fast algorithm
    """
    assert isinstance(N, int)
    assert 10 <= N <= 2e18

    # convert interger to sorted list of its digit
    N_as_list_ordered = sorted([x for x in str(N)])
    P1 = ""
    P2 = ""

    for index, element in enumerate(N_as_list_ordered):
        if index%2:
            P2 += element
        else:
            P1 += element
    
    sumation = int(P1) + int(P2)
    print("{} + {} = {}".format(P1, P2, sumation))
    
solve1(6438573437)
solve2(6438573437)

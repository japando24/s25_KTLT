#Q6 (Funtions)
from math import pow


def q6_kdq(x,n):
    s=0
    for i in range(1,n+1):
        s +=  x**(2*i)
    return s

q6_kdq(0,0)
def q6_dq(x,n):
    if n==1:
        return x**2
    return x**(2*n) + q6_dq(x,n-1)
# def q6_dq(x,n):
#     if n<1:
#         return 0
#     else:
#         return (x**(2*n)+q6_kdq(x,n-1))
#
# q6_dq(5,7)
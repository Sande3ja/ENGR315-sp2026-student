import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """ 
    pi_estimate=0
    pi_error=abs(pi_estimate-math.pi)
    a=1
    b=1/(math.sqrt(2))
    p=1
    t=1/4
    while pi_error>target_error:
       
        aa=(a+b)/2
        bb=math.sqrt(a*b)
        pp=2*p
        tt=t-p*((aa-a)**2)
        a=aa
        b=bb
        p=pp
        t=tt
        pi_estimate=(a+b)**2/(4*t)
        pi_error=abs(pi_estimate-math.pi)
    

    ### YOUR CODE HERE ###

    # change this so an actual value is returned
    return pi_estimate




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")

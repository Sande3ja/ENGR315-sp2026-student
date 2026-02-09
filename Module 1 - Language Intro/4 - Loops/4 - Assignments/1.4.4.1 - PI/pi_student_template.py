import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1  #from wikipedia
b = 1/(math.sqrt(2))  #from wikipieda
t = 1/4 #from wikipedia
p = 1 #from wikipedia

# perform 10 iterations of this loop
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    ### YOUR CODE HERE ###
    w=(a+b)/2          # w is a holder for a_[n+1]
    x= math.sqrt(a*b)  #x is a holder for b_[n+1]
    y=2*p              #y is a holder for p_[n+1]
    z= t-p*((w-a)**2)  # z is a holder for t_[n+1]

    a=w                # Once the calculations are done, update the variables for the next iteration
    b=x
    p=y
    t=z



    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = (a+b)**2/(4*t)

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))

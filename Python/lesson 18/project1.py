def myfunction(n):
    # Loop 1: for i in range(0, n+1)
    # This loop runs n+1 times. Each print operation takes constant time O(1).
    # So, the complexity of this loop is O(n).
    for i in range(0,n+1):
        print("First Loop")

    # Loop 2: while j <= n+1
    # The variable 'j' starts at 1 and doubles in each iteration (j = j*2).
    # This is characteristic of logarithmic time complexity.
    # The loop continues as long as j <= n+1.
    # Let's say it runs 'k' times. Then 2^k <= n+1.
    # So, k <= log2(n+1).
    # Therefore, the complexity of this loop is O(log n).
    j=1
    while(j<=(n+1)):
        print("Second loop ",j)
        j=j*2

    # Loop 3: for i in range(0, 100)
    # This loop runs a fixed number of times (100 times).
    # The number of iterations does not depend on the input 'n'.
    # So, the complexity of this loop is O(1) (constant time).
    for i in range(0,100):
        print("Third Loop")
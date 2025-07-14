def print_recurrence_analysis():
    """
    Prints the recurrence relations and their solutions for the given functions.
    """
    print("Recurrence Relations:\n")

    print("For myfunction1(n) (assuming typical intent for recurrence problems where n <= 1 is base case):")
    print("T_1(n) = T_1(n/2) + T_1(n/3) + O(n)")
    print("Base Case: T_1(n) = O(1) for n <= 1")
    print("Solution: T_1(n) = O(n)\n")

    print("For myfunction2(n):")
    print("T_2(n) = T_2(n-1) + O(1)")
    print("Base Case: T_2(n) = O(1) for n <= 1")
    print("Solution: T_2(n) = O(n)\n")

# Call the function to print the analysis
print_recurrence_analysis()
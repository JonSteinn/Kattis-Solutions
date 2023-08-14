from math import log2 as lg

# Calculate the maximum value of n such that N! < 2**bits
# This involves finding n such that the sum of logarithms of 1 to n (lg(1) + lg(2) + ... + lg(n)) is less than bits.
# This function prepares a dictionary to map years to corresponding bit values.
def pre_process():
    # Create a dictionary mapping years to corresponding bit values (2**(i+2))
    years_to_bits = {y: 2**(i+2) for i, y in enumerate(range(1960, 2170, 10))}
    years_to_n = {}  # Dictionary to store the calculated maximum n for each year
    s, n, year = 0, 2, 1960
    
    # Calculate the value of s (sum of logarithms of 1 to n) for each year and determine the maximum n for each year
    while year < 2170:
        s += lg(n)
        if s > years_to_bits[year]:  # If the calculated sum of logarithms surpasses the corresponding bit value
            years_to_n[year] = n - 1  # Store the maximum n for the year (previous n)
            year += 10  # Move to the next year
        n += 1  # Increment n for the next iteration
        
    return years_to_n  # Return the dictionary of years to maximum n values

def main():
    years_to_n = pre_process()  # Pre-calculate the maximum n values for each year
    while True:
        n = int(input())  # Read an input value n
        if n == 0:  # If n is 0, exit the loop
            break
        print(years_to_n[n - n % 10])  # Print the maximum n for the corresponding year (subtracting the last digit of n)

if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly

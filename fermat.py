import random

# Let n be the number of bits of the various numbers in these algorithms.

# This algorithm runs in O(n^5) time since it calls fermat and then miller_rabin.  fermat runs in O(n^4) time and
#   miller_rabin runs in O(n^5) time, so prime_test runs in O(n^4) + O(n^5) time, which can be reduced to O(n^5).
# This algorithm has O(n) bit space complexity since both fermat and miller_rabin have space complexities of O(n), so
#   the space complexity would be O(n) + O(n), which can be reduced to O(n).
def prime_test(N, k):
	return run_fermat(N,k), run_miller_rabin(N,k)

# This algorithm runs in O(n^4) time since there are n recursive calls and there are O(n^3) bit operations at each
#   recursive call.
# This algorithm has O(n) bit space complexity because z is stored at each recursive level, and z has n bits, so the
#   space complexity is O(k * n) where k is the number of recursive calls, which can be reduced to O(n).
def mod_exp(x, y, N):
    # This algorithm follows the pseudo code found on page 19 of the textbook
    if y == 0:
        return 1
    # There will be n recursive calls to mod_exp, where n is the number of bits of y (each time y is halved, its
    #   number of bits is reduced by 1.
    # z will have n bits, so the space complexity is O(n).
    z = mod_exp(x, y // 2, N)

    # There will be O(n^3) bit operations in this if-else block (division has a complexity of O(n^3), and it is the
    #   largest complexity in this if-else block).

    # Checking if y is even (checking the last bit) runs in constant time.
    if y % 2 == 0:
        # Squaring z runs in O(n^2) time (since it is the same as multiplying z by z).  Division runs in O(n^3) time.
        return (z ** 2) % N

    else:
        # Squaring z runs in O(n^2) time.  Multiplying by x runs in O(n^2) time.  Division runs in O(n^3) time.
        return (x * (z ** 2)) % N

# This algorithm runs in O(n^3) time because the largest operation is division, which runs in O(n^3) time.
# This algorithm has O(1) bit space complexity because 2^k would require k (constant) bits.
def fprobability(k):
    # The probability that the fermat primality test makes an error is less than or equal to 1 / (2^k).
    # As such, the probability that the fermat primality test is correct is 1 - P(error) = 1 - (1 / (2^k)).

    # There will be O(n^3) bit operations (division has a complexity of O(n^3), and it is the
    #   largest complexity in this calculation).

    # Subtraction runs in O(n) time.  Division runs in O(n^3) time.  2^k is 2 multiplied by itself k times, so its
    #   time complexity would be O(n^2) (multiplication).
    # 1 requires 1 bit of space and 2^k would require about k bits of space (bit shifting k times), so its space
    #   complexity would be O(1) (constant).
    return 1 - (1 / (2 ** k))


# This algorithm runs in O(n^3) time because the largest operation is division, which runs in O(n^3) time.
# This algorithm has O(1) bit space complexity because 4^k can be re-written as 2^(2k), which would require 2k
#   (constant) bits.
def mprobability(k):
    # The miller-rabin test works for at least 3/4 of the values of a, or 1 - 1/4.
    # There are k values of a.
    # As such, the probability that the miller-rabin test is correct is 1 - 1/(4^k)

    # There will be O(n^3) bit operations (division has a complexity of O(n^3), and it is the
    #   largest complexity in this calculation).

    # Subtraction runs in O(n) time.  Division runs in O(n^3) time.  4^k is 4 multiplied by itself k times, so its time
    #   complexity would be O(n^2) (multiplication).
    # 1 requires 1 bit of space and 4^k can be re-written as 2^(2k), which would require about 2k bits of space (bit
    #   shifting 2k times), so its space complexity would be O(1) (constant).
    return 1 - (1 / (4 ** k))

# This algorithm runs in O(n^4) time because it calls mod_exp k times, and mod_exp runs in O(n^4) time, so the
#   complexity this algorithm is O(k * n^4), which can be reduced to O(n^4).
# This algorithm has O(n) bit space complexity because it calls mod_exp k times, and mod_exp has a space complexity of
#   O(n), so the space complexity is O(k * n), which can be reduced to O(n).
def run_fermat(N,k):
    # This algorithm follows the pseudo code found on page 27 of the textbook.
    for i in range(1, k):
        a = random.randint(1, N - 1)

        # mod_exp runs in O(n^4) time (see the comments for mod_exp).
        if mod_exp(a, N - 1, N) != 1:
            return "composite"

    return "prime"

# This algorithm runs in O(n^5) time because it calls mod_exp k times for the initial check, and it calls mod_exp k * n
#   times for the sequence of square roots (the exponent is halved at each pass in the while loop, so its number of bits
#   decreases by 1 at each pass), so the complexity of this algorithm is O(k * n * n^4), which can be reduced to O(n^5).
# This algorithm has a O(n) bit space complexity because it calls mod_exp come constant c amount of times (k * m times,
#   where m is the number of bits in y), and mod_exp has a space complexity of O(n), so the overall space complexity is
#   O(c * n), which can be reduced to O(n).
def run_miller_rabin(N,k):
    # We want to test k different values of a (like the fermat test).
    for i in range(1, k):
        # Get a random value of a such that 1 <= a < N.
        a = random.randint(1, N - 1)

        # We must first check if a^(N - 1) is congruent to 1 mod N.

        # mod_exp runs in O(n^4) time (see the comments for mod_exp).
        if mod_exp(a, N - 1, N) == 1:
            # If the initial check passed, we proceed to check the sequence of square roots.

            # Subtraction runs in O(n) time.
            exponent = N - 1

            z = 1

            # Keep checking the sequence of square roots until the exponent is no longer even or z != 1.

            # Worst case, this while loop is executed n times where n is the number of bits of the exponent (it is
            #   halved at each pass through the loop, so its number of bits is reduced by 1 at each pass).
            while exponent % 2 == 0 and z == 1:
                # Divide the exponent by 2 (same as taking the square root).

                # Division runs in O(n^3) time.
                exponent = exponent / 2

                # Calculate the modulo exponent.

                # mod_exp runs in O(n^4) time (see the comments for mod_exp).
                z = mod_exp(a, exponent, N)

            # Once the exponent is no longer even (we can't take the square root) or z != 1, make the final check of
            # the algorithm.
            # If this case is true, N failed the test, so N is composite

            # Division runs in O(n^3) time.
            if z % N != N - 1 and z % N != 1:
                return "composite"


        # If a^(N - 1) is not congruent to 1 mod N, N failed the test, so N is composite
        else:
            return "composite"

    return "prime"

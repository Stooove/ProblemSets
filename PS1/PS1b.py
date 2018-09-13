# Problem Set 1b
# Name: Steve
# Collaborators: None
# Time: 30 min
# Write a program that computes the sum of the logarithms of all the primes from 2 to some number n,
# and print out the sum of the logs of the primes, the number n, and the ratio of these two quantities.
# Test this for different values of n.

'''
log(x) means ln(x), not log10(x)
log(2) + log(3) = log(2*3) = log(6)

want: (sum of all log(prime) less than n)/n

examples:
input = 3:
log(2) = .69
    log(2) = .69
        log(2)/3 = .23

input = 5:
log(3) = 1.0986
    (log(2) + log(3)) = 1.79
        log(6)/5 = .358

input = 7:
log(5) = 1.609
    log(2*3*5) = 3.4012
        log(30)/7 = .4859

input 11:
log(7) = 1.9459
    log(30*7) = 5.3471
        log(210)/11 = .4861

input 13:
log(11) = 2.3979
    log(210*11) = 7.75
        log(2310)/13 = .5958

input 1000:
log(991) =
    log(991*X)/997 = .9521971056670983

approaches 1
'''

from math import *


def main():
    some_n = input_gather() #some_n chosen as this was the name given
    prime_sum, prime_below_some_n = prime_control(some_n)
    print('sum of log(prime), between 2 and up to but not including {} is: {}'.format(some_n, prime_sum))
    print('your entered n value is: {}'.format(some_n))
    print('the ratio of the sum of log(prime) over n is: {}'.format(prime_sum/prime_below_some_n))


def input_gather():
    number_n = input('What positive integer greater than 1 would you like to go through? ')
    int_check = input_check(number_n) #verify user input a number
    while int_check == False:
        number_n = input('What POSITIVE INTEGER GREATER THAN 1 would you like to go through? ')
        int_check = input_check(number_n)
    return int(number_n)


def input_check(integer):
    integer_check = False
    try:
        integer = int(integer)
        if integer > 1:
            integer_check = True
    finally:
        if integer_check == True:
            return True
        else:
            return False


def prime_control(some_n):
    '''controls the following functions: find primes until entered number (some_n), sums the logs of primes below some_n.
    for 0-13, should find log(2*3*5*7*11)
    '''
    prime_sum = 0  # initialize total
    proposed_prime = 0  # first number to evaluate as prime
    prime_below_some_n = 0  # initialize previous prime tracker
    while proposed_prime < some_n:
        proposed_prime, is_prime = find_next_prime(proposed_prime, some_n)  # returns true if proposed_prime is prime.
        if is_prime == True:
            prime_sum = log_prime_sum_calc(prime_sum, prime_below_some_n)  # add the log of the prime_below_some_n to the total
            prime_below_some_n = proposed_prime
    return prime_sum, prime_below_some_n


def find_next_prime(proposed_prime, some_n):
    is_prime = False  # intialize first, in case some proposed_prime >= some_n
    while proposed_prime < some_n:  # go forward until new prime is found or limit reached
        proposed_prime += 1
        is_prime = primetest(proposed_prime)  # test if proposed_prime is prime
        if is_prime == True:
            return proposed_prime, is_prime
        else:
            pass
    return proposed_prime, is_prime


def primetest(n):
    n_divis_int = 3  # starting at 3, as anything dividing by 1 doesn't matter, and 2 should be False.
    if n <= 1:  # 1 is not prime, nor are negative numbers
        return False
    elif n <= 3:  # 2 and 3 are prime
        return True
    elif n % 2 == 0:  # even numbers are not prime
        return False
    elif n == 5 or n == 7:  # 5 and 7 are primes < 9
        return True
    else:
        while n_divis_int <= n**(.5):  # primeality indicates only need to go through sqrt of number, as all factors repeat after that.
            if n % n_divis_int == 0:
                return False
            else:
                n_divis_int += 2  # even numbers aren't prime
        return True


def log_prime_sum_calc(prime_sum, prime):
    if not prime == 0:  # ensure log(0) can't be a value
        prime_sum += log(prime)
    return prime_sum


if __name__ == '__main__':
    main()


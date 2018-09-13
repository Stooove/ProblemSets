# Problem Set 1a
# Name: Steve
# Collaborators: None
# Time: 30 min
#
def main():
    prime = prime_proposal()
    print(prime)

def prime_proposal():
    prime_count = 0
    proposed_prime = 0
    while prime_count < 1000:
        proposed_prime += 1
        isprime = primetest(proposed_prime)
        if isprime == True:
            prime_count +=1
        else:
            pass
    prime = proposed_prime
    return prime

def primetest(n):
    n_divis_int = 3 #starting at 3, as anything dividing by 1 doesn't matter, and 2 should be False.
    if n <= 1: #1 is not prime, nor are negative numbers
        return False
    elif n <= 3: #2 and 3 are prime
        return True
    elif n % 2 == 0: #even numbers are not prime
        return False
    elif n == 5 or n == 7: #5 and 7 are primes < 9
        return True
    else:
        while n_divis_int <= n**(.5): #primeality indicates only need to go through sqrt of number, as all factors repeat after that.
            if n%n_divis_int == 0:
                return False
            else:
                n_divis_int += 2 #don't care about dividing by even numbers
        return True


if __name__ == '__main__':
    main()
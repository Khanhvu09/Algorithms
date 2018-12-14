# ========Algorithm========

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143

largest_prime = [1]
number = 600851475143
# find prime numbers of 600851475143
# list all the prime numbers for that number
# print the highest value prime number 
# while largest_prime[-1] < number:
for i in range(1, 600000000):
    if i % 2 == 0:
        largest_prime.append(i)
print largest_prime
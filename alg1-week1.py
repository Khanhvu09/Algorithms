# =========Algorithm 1=========
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# sum = 0
# for i in range(0, 1001):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print sum


fibSeq = [0, 1]
i = 1
sum = 0
x = fibSeq
while fibSeq[-1] < 4000000:
    fibSeq.append(fibSeq[i] + fibSeq[i - 1])
    i += 1
del fibSeq[-1]
print fibSeq
for i in fibSeq[1:len(fibSeq)]:
    if i % 2 == 0:
        sum += i 
print sum 
    

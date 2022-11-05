# Prime number
# No idea if it is what it is made or not, in any case you type "algorithm of prime number" and you find good codes (so yeah)

num = 200000000401
  
# If given number is greater than 1
divisibleBy = 1
if num > 1:
  
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        divisibleBy = i
        print("Testing with", i)
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number, this number is divisible by", divisibleBy)
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")


# MAYBE I STOLE THIS CODE IDK !!!!!!!
## Computing Prime Numbers
def prime_number():
    value = int(input("Which prime number do you want to see? "))
    prime_list = []
    count = 0
    integer = 0
    factor = 0

    while (count < value):
        if (integer > 1):
            if (integer == 2) or (integer % 2 != 0):
                prime_list.append(integer)
                for i in prime_list:
                    if (integer % i == 0):
                        factor += 1
                        if (factor > 1):
                            prime_list.pop()
                            count -= 1
                            break
                factor = 0
                count += 1
        integer += 1

    return "The value you seek is", prime_list[(value - 1)]


print(prime_number())

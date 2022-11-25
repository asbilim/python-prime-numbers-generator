def prime_number(limit):

    prime_numbers = [1,2]
    count = 3
    test = 2
    prime = False
    if limit <= 2:
        print(1)
        print(2)
    else:
        while count < limit:
            while test < count:
                if count % test == 0:
                    if count in prime_numbers:
                        prime = False #not prime
                    count += 1
                    test=2
                else:
                    prime = True #prime
                    test+=1

            if prime:
                print(count)
            count+=1
            test=2
            prime = False #putting back the default value of prime

prime_number(15000)
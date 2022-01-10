def is_prime(number: int) -> bool: 
    list = [x for x in range(2,number) if number % x == 0];
    return len(list) == 0;

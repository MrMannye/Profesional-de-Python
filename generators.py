import time 

def fibo_gen(maximo: int):
    n1, n2, counter, aux = 0, 1, 0, 0;
    while True:
        if aux <= maximo:
            if counter == 0:
                counter += 1; 
                yield n1; 
            elif counter == 1: 
                counter += 1;
                yield n2; 
            else: 
                aux = n1 + n2; 
                n1, n2 = n2, aux;
                counter += 1; 
                yield aux;
        else: 
            break;

if __name__ == '__main__':
    fibonacci = fibo_gen(8);
    for element in fibonacci: 
        print(element);
        time.sleep(1);
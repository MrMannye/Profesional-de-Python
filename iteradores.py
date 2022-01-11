
# * Como recorre un arreglo Python cuando lo hacemos por un for asi es como se ve por detras 
def iterador(): 
    my_list = [1,2,3,4,5];
    my_iter = iter(my_list);

    while True:
        try:
            element = next(my_iter);
            print(element);
        except StopIteration: 
            break;


# ! Azucar sintactico de la funcion que esta arriba
def iterador_for():
    my_list = [1,2,3,4,5];
    for element in my_list: 
        print(element);


def run():
    iterador();
    iterador_for();

if __name__ == '__main__':
    run();
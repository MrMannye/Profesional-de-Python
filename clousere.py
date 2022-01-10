def main():
    a = 1;
    
    def nested():
        print(a);
    
    # * Retornamos la funcion nested que imprimiendo la variable de scope superior
    return nested

def make_multiplayer(x):
    def multiplier(n):
        return x*n;
    return multiplier;


if __name__ == '__main__':
    # TODO: A una variable (my_func) le asignamos la funcion main que retorna una funcion que a su vez esta
    # TODO: guardando el valor de la varible a para poder imprimirla (closures)
    my_func = main();
    my_func();

    # * --------------------------

    times10 = make_multiplayer(10);
    times4 = make_multiplayer(4);

    print(times10(3))
    print(times10(2))
    print(times10(times4(2)));

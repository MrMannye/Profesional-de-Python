from datetime import date, datetime
from typing import final

def execution_time(func):
    def wrapper(*args, **kwargs): 
        initial_time = datetime.now();
        func(*args, **kwargs)
        final_time = datetime.now();
        print((final_time - initial_time).total_seconds());
    return wrapper;

@execution_time
def random_func(): 
    for _ in range(1, 100000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b;

# * KeyWord Argument
@execution_time
def saludo(nombre='Cesar'):
    print(f'Hola {nombre}')

random_func();
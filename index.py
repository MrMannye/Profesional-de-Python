from palindrome import is_palindrome


from palindrome import is_palindrome;
from primeNumber import is_prime;

menu = '''
    PROYECTO PROFESIONAL DE PYTHON
    1. Palabra Palindroma (Tipado Estatico)
    2. Numero Primo (Tipado Estatico)

'''


def run():
    print(menu);
    option = input("INGRESE OPCION: ");
    if(option == '1'):
        word = input('INGRESE SU PALABRA: ');
        palindromo = is_palindrome(word);
        print(palindromo);
    else: 
        number = int(input('INGRESE SU NUMERO: '));
        primo = is_prime(number);
        print(primo);

if __name__ == '__main__':
    run();

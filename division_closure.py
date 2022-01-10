def make_division_of(n: int):
    def divition(x: int) -> str:
        print(x/n);
    return divition;

def run(): 
    divide_by_3 = make_division_of(3);
    divide_by_3(18); # * The expected output is 6

    divide_by_5 = make_division_of(5);
    divide_by_5(100); # * The expected output is 20
    
    divide_by_18 = make_division_of(18);
    divide_by_18(54); # * The expected output is 3

if __name__ == '__main__':
    run();
    
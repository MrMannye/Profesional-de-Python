def make_repeater_of(n: int):
    def repeater(string: str) -> str:
        assert type(string) == str, "Solo puedes utilizar cadenas";
        print(string * n);
    return repeater;


def run(): 
    repeat_5 = make_repeater_of(5);
    repeat_5("Hola Mundo ");

    repeat_10 = make_repeater_of(10);
    repeat_10("Miguel ");


if __name__ == '__main__':
    run();
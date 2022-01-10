def is_palindrome(string: str) -> bool:
    #Ana
    string = string.replace(" ", "").lower();
    return string == string[::-1];

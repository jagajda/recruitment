def check_if_palindrome(x):
    x = x.lower()
    x = x.replace(' ', '')
    rev = ''.join(reversed(x))
    return x == rev

def test_positive():
    mock = "A toyota"
    assert check_if_palindrome(mock) == True

def test_negative():
    mock = "Not a palindrome"
    assert check_if_palindrome(mock) == False

def main():
    print(check_if_palindrome("A b  B a"))
    print(check_if_palindrome("kur Czak"))

if __name__ == '__main__':
   main() 

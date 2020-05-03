def diff_digits(x):
    digits=[i for i in str(x)]
    return len(set(digits))

def test_digits():
    mock = 177
    assert diff_digits(mock) == 2

def test_one_digit():
    assert diff_digits(1) == 1

def test_same_digits():
    assert diff_digits(3333) == 1

if __name__ == '__main__':
    print(diff_digits(177))

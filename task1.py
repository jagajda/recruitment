def revert(a):
    return a[::-1]

#creating simple unittest
def test_revert():
    test_str = "I see sea shells in sea"
    assert revert(test_str) == "".join(reversed(test_str))

def test_empty():
    assert revert('') == ''

def test_one_letter():
    mock = 'a'
    assert revert(mock) == mock

if __name__== '__main__':
    print (revert("I see sea shells in sea"))

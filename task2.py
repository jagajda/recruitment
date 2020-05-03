import string

def translate(x):
    lookup = {}
    alphabet = list(string.ascii_lowercase)
    x = x.lower()
    x_list = list(x)
    i = 0
    digit = 2
    while(i < int(len(alphabet)/3)):
        k = 0
        for j in range(1,4):
            lookup.update({alphabet[i*3 + k]:j*str(digit)})
            k += 1
        digit += 1
        i += 1
    lookup.update({'p': '7'})
    lookup.update({'q': '77'})
    lookup.update({'r': '777'})
    lookup.update({'s': '7777'})
    lookup.update({'t': '8'})
    lookup.update({'u': '88'})
    lookup.update({'v': '888'})
    lookup.update({'w': '9'})
    lookup.update({'x': '99'})
    lookup.update({'y': '999'})
    lookup.update({'z': '9999'})
    for i in range(len(x_list)):
        if x_list[i] == ' ':
            x_list[i] = '#'
        else:
            x_list[i] = lookup[x_list[i]]

    return ''.join(x_list)

def test_translate():
    test_str = "Eve has a cat"
    mock = "3388833#4427777#2#22228"
    assert translate(test_str) == mock

def test_empty():
    assert translate('') == ''

def test_one_letter():
    assert translate('c') == '222'

def main():
    print(translate("Eve has a cat"))

if __name__ == '__main__':
    main()

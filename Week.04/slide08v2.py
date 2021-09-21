# function to add/join 3 values together
def plus3(val1, val2, val3):
    print('In plus3: ', end='')
    print('val1={},'.format(val1), end='')
    print('val2={}, val3={}'.format(val2, val3))
    result = val1 + val2 + val3
    return result

# main script
def main():
    total = plus3(12, 3, 5)
    print('In main: total is', total)
    word = plus3('a', 'b', 'c')
    print('In main: concatenated string is', word)

if __name__ == "__main__":
    main()

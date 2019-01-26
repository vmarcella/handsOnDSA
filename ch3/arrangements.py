def bitStr(string, length):
    '''
        Find all the possible arrangements given a string of characters that
        can be used and length of the desired output string

        Arguments:
            :string: characters available for use
            :length: desired output
    '''
    if length == 1:
        return string
    else:
        return [digit + bits for digit in bitStr(string, 1) for bits in bitStr(string, length - 1)]

print(bitStr('abc', 4))

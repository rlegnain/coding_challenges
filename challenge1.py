"""
Run Length Encoding
=======================

Write a code to conver a string of repeting letters to a string of number of character
example:
aaaabbccca -> 4a2b3c1a
"""

def run_length_encoding1(string):
    """proposal 1"""
    #initialize params
    count = 0
    count_letter = None
    encode_string = ""

    # algorithm
    for index, letter in enumerate(string):    
        if count_letter == letter:
            count += 1
        else:
            encode_string += str(count) + count_letter
            count_letter = letter
            count = 1

        if index == len(string)-1:
            encode_string += str(count) + count_letter

    return encode_string



def run_length_encoding2(string):
    """propsal 2"""
    #initialize params
    encode_string = ""
    endcode_array = []
    count_letter = None

    # algorithm
    for letter in string:
        if count_letter == letter:
            # update counter
            endcode_array[-2] = str(int(endcode_array[-2]) + 1)
        else:
            count_letter = letter
            endcode_array.extend([str(1), letter])

    return "".join(endcode_array)

if __name__ == "__main__":
  string = input("Enter a string: ")
  rtn1 = run_length_encoding1(string=string)
  rtn2 = run_length_encoding2(string=string)

'''
*                                                                                      *
*  Letter Capitalize                                                                   *
*  Using the JavaScript language, have the function LetterCapitalize(str) take the     *
*  str parameter being passed and capitalize the first letter of each word. Words      *
*  will be separated by only one space.                                                *
*                                                                                      *
*  SOLUTION                                                                            *
*  I am going to convert the string to an array based on the space character that      *
*  separates each word. Then I am going to loop through each word in the array and     *
*  capitalize the first letter of the word. I am going to convert array back to a      *
*  string to return as the answer.
*                                                                                      *
*  Steps for solution                                                                  *
*    1) Convert string to arry of words by splitting on space.                         *
*    2) Loop thru each word in the array and convert first letter to uppercase         *
*       using the charAt(0) value and then appending the remainder of the word         *
*       using the slice() function                                                     *
*    3) Convert array to string with join() function.    
'''


def letter_capitalize(str_param):
    str_to_list = (str_param.split(" "))
    for word in str_to_list:
        for char in word:
            pass

    return str_param


print(letter_capitalize("this is a test"))


name = 'humra'
print('My name is {1} {0}'.format(name, 'ahsan'))
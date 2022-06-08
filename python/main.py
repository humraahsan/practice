# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def print_dict(my_dict):
    """
    Print dict key and values line by line, examples:
        Arizona; 10
        California; 12
        Alabama; 20
        arkansas; 3
    """
    for key, xyz in my_dict.items():
        print(key, ';', xyz)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Humra')
    score_dict = {
        "Arizona": 10,
        "California": 12,
        "Alabama": 20,
        "arkansas": 3
    }
    print_dict(score_dict)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

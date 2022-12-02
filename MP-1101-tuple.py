"""
function generate_tuple
    generate 5 random integer
    append each into the list
    return list converted into tuple

function negelct second
    keep element such that its index divided by 2 is not equal to 0
    return value at odd element
"""

from random import randint

def generate_tuple(length):
    """
    :param length: int (length of tuple)
    :return: tuple of random element of the specified length
    """
    base_lst = []
    for element_order in range(length):
        base_lst.append(randint(0, 20))
    return tuple(base_lst)

def neglect_even_element(base_tuple):
    """
    :param base_tuple: tuple (tuple to be processed)
    :return: tuple with second element removed
    """
    return tuple(base_tuple[i] for i in range(len(base_tuple)) if i % 2 == 0)
def main():
    base_tuple = generate_tuple(int(input("Specify the tuple length: ")))
    new_tuple = neglect_even_element(base_tuple=base_tuple)
    print(f"Base tuple: {base_tuple} \nProcessed tuple: {new_tuple}")

if __name__ == "__main__":
    main()

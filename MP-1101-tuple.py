def make_tuple(space_seperated):
    return tuple(space_seperated.split(" "))

def neglect_two(base_tuple):
    return tuple(base_tuple[i] for i in range(len(base_tuple)) if i != 1)

def main():
    base_tuple = make_tuple(input("Enter elements seperated by space: "))
    new_tuple = neglect_two(base_tuple=base_tuple)
    print(f"Base tuple: {base_tuple} \nProcessed tuple: {new_tuple}")

if __name__ == "__main__":
    main()

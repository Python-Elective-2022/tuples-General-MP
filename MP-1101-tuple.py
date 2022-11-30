def neglect_two(base_tuple):
    return tuple(base_tuple[i] for i in range(len(base_tuple)) if i != 1)

def main():
    base_tuple = ("a", 1, "b", 2)
    new_tuple = neglect_two(base_tuple=base_tuple)
    print(f"Base tuple: {base_tuple} \nProcessed tuple: {new_tuple}")

if __name__ == "__main__":
    main()
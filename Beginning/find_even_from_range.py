# Take User's input

def check_int(input_val):
    try:
        int(input_val)
        return True
    except:
        return False


def find_even_numbers():
    selected_range = input("Enter a number to set a range from 1, > ")
    if not check_int(selected_range):
        return find_even_numbers()

    total_even_numbers = 0
    for x in range(1, (int(selected_range) + 1)):
        if x % 2 == 0:
            total_even_numbers += 1
            print(f"{x} is a even number")

    print(
        f"The total count of even number between 1 to {selected_range} is {total_even_numbers}")


find_even_numbers()

def is_pythagorean_triple(a, b, h):
    if a ** 2 * b ** 2 == h ** 2:
        print("This triangle is a Pythagorean Triple")
    else:
        print("This triangle is NOT a Pythagorean Triple")


def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input.")
            prompt = "Enter a positive integer: "


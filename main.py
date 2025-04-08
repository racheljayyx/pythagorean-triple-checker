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

    return num


def main():
    print("This is Pythagorean Triple Checker")
    side_1 = get_positive_integer("Enter side #1: ")
    side_2 = get_positive_integer("Enter side #2: ")
    side_3 = get_positive_integer("Enter side #3: ")

    triangle_sides = [side_1, side_2, side_3]
    triangle_sides.sort()

    is_pythagorean_triple(triangle_sides[0], triangle_sides[1], triangle_sides[2])


if __name__ == "__main__":
    main()

from prac_6.guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        time = input("Year: ")
        value = input("Cost:$ ")
        guitars.append(Guitar(name, time, value))
        print("{} ({}) :$ {:,.2f} added.".format(name, time, float(value)))
        space = input("")
        name = input("Name: ")
    print("\n... snip ...\nThese are my guitars:")
    for i, guitar in enumerate(guitars):
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, float(guitar.cost),
                                                                  " (vintage)" if 2021-int(guitar.year) > 50 else ""))


main()
class Person:
    def __init__(self):
        self.__name = None
        self.__age = None
        self.__address = None

    def get_name(self):
        # self.__name = input("enter name: ")
        print(self.__name)
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
    #   self.__age = int(input("enter age: "))
        print(self.__age)
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_address(self):
    #   // self.__address = input("enter address: ")
        print(self.__age)
        return self.__address

    def set_address(self, address):
        self.__address = address


def main():
    person = Person()
    person.set_name("Arshad")
    person.set_age(21)
    person.set_address("123 johar town")

    print("Name: ", person.get_name())
    print("Age: ", person.get_age())
    print("Address: ", person.get_address())


if __name__ == "__main__":
    main()
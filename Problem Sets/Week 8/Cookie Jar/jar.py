class Jar:
    # initializes cookie jar with a given capacity
    # capacity represents maximum number of cookies that can fit in the cookie jar
    # if capacity is not a non-negative int: raises a ValueError
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    # returns a str with n 🍪, where n is the number of cookies in the cookie jar
    # e.g. 3 cookies in the cookie jar return "🍪🍪🍪"
    def __str__(self):
        return self.size * "🍪"

    # adds n cookies to the cookie jar
    # if adding would exceed cookie jar’s capacity: raises a ValueError
    def deposit(self, n=0):
        self.size = self.size + n

    # removes n cookies from the cookie jar
    # if withdrawing would exceed cookie jar’s size: raises a ValueError
    def withdraw(self, n=0):
        self.size = self.size - n

    # returns the cookie jar’s capacity
    # maximum number of cookies that can be deposited
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    # returns number of cookies actually in the cookie jar
    # as large as the number of cookies that have been deposited/withdrawn
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError
        if size > self.capacity:
            raise ValueError
        self._size = size


def main():
    jar = Jar()
    jar.deposit()
    jar.withdraw()
    print(jar)


if __name__ == "__main__":
    main()

class HomeView:

    @classmethod
    def home(cls):
        print("Welcome\n")
        print("1. List Players")
        print("2. New Player\n")
        print("Q. Exit")

        return input("Choice: ")

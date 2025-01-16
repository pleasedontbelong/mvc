class HomeView:
    @classmethod
    def home(cls):
        print("Welcome\n")
        print("1. Players Menu")
        print("2. Tournament Menu\n")
        print("Q. Exit")

        return input("Choice: ")

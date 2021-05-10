class PlayerView:

    @classmethod
    def display_list(cls, players):
        print("\tID\tName\tAge")
        for player in players:
            print(f"\t{player.id}\t{player.name}\t{player.age}")

        print("1. View Player")
        print("2. New Player")
        print("3. Delete Player")
        print("4. Update Player")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        player_id = None

        if choice in ("1", "3", "4"):
            player_id = int(input("Enter Player Id:"))

        return choice, player_id

    @classmethod
    def detail_player(cls, player):
        print(f"Id: {player.id}")
        print(f"Name: {player.name}")
        print(f"Age: {player.age}")
        print(f"Email: {player.email}")

        print("Q. Exit")
        print("H. Homepage")
        return input("Choice:")

    @classmethod
    def create_player(cls):
        return {
            "id": input("Enter an ID: "),
            "name": input("Enter a name: "),
            "age": input("Enter an age: "),
            "email": input("Enter an email: ")
        }

    @classmethod
    def update_player(cls, player):
        return {
            "name": input(f"Enter a name [{player.name}]: "),
            "age": input(f"Enter an age [{player.age}]: "),
            "email": input(f"Enter an email [{player.email}]: ")
        }
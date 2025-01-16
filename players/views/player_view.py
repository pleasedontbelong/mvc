class PlayerView:
    @classmethod
    def display_list(cls, players):
        print("\tID\tName\tAge")
        for player in players:
            print(f"\t{player.id}\t{player.name}\t{player.age}")

        print("1. View Player")
        print("2. New Player")
        print("3. Delete Player")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice: ")
        player_id = None
        player = None

        if choice in ("1", "3"):
            player_id = input("Enter Player Id:")

            player = next((p for p in players if p.id == player_id), None)
            while not player and player_id is not None:
                print("Player not found")
                player_id = int(input("Enter Player Id: "))
                player = next((p for p in players if p.id == player_id), None)

        return choice, player

    @classmethod
    def detail_player(cls, player):
        print(f"Id: {player.id}")
        print(f"Name: {player.name}")
        print(f"Age: {player.age}")
        print(f"Email: {player.email}")
        input("Press Enter to continue")

    @classmethod
    def create_player(cls):
        return {
            "id": input("Enter an ID: "),
            "name": input("Enter a name: "),
            "age": input("Enter an age: "),
            "email": input("Enter an email: "),
        }

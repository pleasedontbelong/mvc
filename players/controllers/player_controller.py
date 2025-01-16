from players.controllers.home_controller import HomePageController
from players.models.player import Player
from players.screen import clear_screen
from players.views.player_view import PlayerView


class PlayerController:
    @classmethod
    @clear_screen
    def list(cls, store, route_params=None):
        choice, player = PlayerView.display_list(store["players"])

        if choice == "1":
            cls.view(store, player)
        elif choice == "2":
            cls.create(store)
        elif choice == "3":
            cls.delete(store, player)
        elif choice.lower() == "q":
            return
        elif choice.lower() == "h":
            HomePageController.main_menu(store)
        else:
            raise Exception("invalid choice")

    @classmethod
    @clear_screen
    def create(cls, store):
        # call the view that will return us a dict with the new player info
        data = PlayerView.create_player()

        # You could specify each argument like:
        # player = Player(id=data["id"], name=data["name"], age=data["age"])
        # but it's easier to use `**` to pass the arguments
        player = Player(**data)

        # we add the player to the store
        store["players"].append(player)

        cls.list(store)

    @classmethod
    @clear_screen
    def delete(cls, store, player):
        # remove the player from the store
        store["players"].remove(player)
        cls.list(store)

    @classmethod
    @clear_screen
    def view(cls, store, player: Player):
        # we pass the player to the view that will display the player info
        PlayerView.detail_player(player)
        cls.list(store)

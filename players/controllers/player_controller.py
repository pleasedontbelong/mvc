from players.models.player import Player, PlayerManager
from players.views.player_view import PlayerView


class PlayerController:

    @classmethod
    def list(cls, store, route_params=None):
        choice, player_id = PlayerView.display_list(store["players"])

        if choice == "1":
            return "view_player", player_id
        elif choice == "2":
            return "new_player", None
        elif choice == "3":
            return "delete_player", player_id
        elif choice == "4":
            return "update_player", player_id
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            raise Exception("invalid choice")

    @classmethod
    def create(cls, store, route_params=None):
        # call the view that will return us a dict with the new player info
        data = PlayerView.create_player()

        # You could specify each argument like:
        # player = Player(id=data["id"], name=data["name"], age=data["age"])
        # but it's easier to use `**` to pass the arguments
        player = Player(**data)

        if not player.is_valid():
            return "errors", "Les informations sont incorrectes"

        # we add the player to the store
        store["players"].append(player)

        return "list_player", None

    @classmethod
    def delete(cls, store, route_params):
        # remove the player from the store
        store["players"] = [
            p for p in store["players"] if p.id != route_params
        ]
        return "list_player", None

    @classmethod
    def view(cls, store, player_id):
        """
        Display one single player, the player_id correspond to the player ID
        we want to display
        """
        # search the player on the store
        manager = PlayerManager(store)
        player = manager.get_player(player_id)

        # we pass the player to the view that will display the player info and
        # the next options
        choice = PlayerView.detail_player(player)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None

    @classmethod
    def update(cls, store, player_id):
        manager = PlayerManager(store)
        player = manager.get_player(player_id)

        data = PlayerView.update(player)

        player.update(**data)

        return "list_player", None
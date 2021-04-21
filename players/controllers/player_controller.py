from players.models.player import Player
from players.views.player_view import PlayerView


class PlayerList:
    def dispatch(self, store, route_params=None):
        choice, player_id = PlayerView.display_list(store["players"])

        if choice == "1":
            return "player_detail", player_id
        elif choice == "2":
            return "player_create", None
        elif choice == "3":
            return "player_delete", player_id
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            raise Exception("invalid choice")


class PlayerCreate:
    def dispatch(self, store, route_params=None):
        # call the view that will return us a dict with the new player info
        data = PlayerView.create_player()

        # You could specify each argument like:
        # player = Player(id=data["id"], name=data["name"], age=data["age"])
        # but it's easier to use `**` to pass the arguments
        player = Player(**data)

        # we add the player to the store
        store["players"].append(player)

        return "player_list", None


class PlayerDelete:
    def dispatch(self, store, route_params):
        # remove the player from the store
        store["players"] = [p for p in store["players"] if p.id != route_params]
        return "player_list", None


class PlayerDetail:
    def dispatch(self, store, route_params):
        """
        Display one single player, the route_params correspond to the player ID
        we want to display
        """
        # search the player on the store
        player = next(p for p in store["players"] if p.id == route_params)

        # we pass the player to the view that will display the player info and
        # the next options
        choice = PlayerView.detail_player(player)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None

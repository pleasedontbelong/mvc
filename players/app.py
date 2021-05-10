from players.controllers.home_controller import HomePageController
from players.models.player import Player
from players.controllers.player_controller import PlayerController
import subprocess as sp


class Store:

    def __init__(self) -> None:
        self.store = {"players": []}
        self.load_players()

    def load_players(self):
        # lire le players.json et save les instances dans self.store
        pass

    def get_player(self, player_id):
        return next(p for p in self.store["players"] if p.id == player_id)

    def update_player(self, player, data):
        player.name = data["name"]
        player.age = data["age"]
        player.email = data["email"]
        # maj le fichier player.json avec tiny db
        #...


class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "list_player": PlayerController.list,
        "new_player": PlayerController.create,
        "update_player": PlayerController.update,
        "view_player": PlayerController.view,
        "delete_player": PlayerController.delete,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = Store()

    def run(self):
        while not self.exit:
            # Clear the shell output
            sp.call('clear', shell=True)

            # Get the controller method that should handle our current route
            controller_method = self.routes[self.route]

            # Call the controller method, we pass the store and the route's
            # parameters.
            # Every controller should return two things:
            # - the next route to display
            # - the parameters needed for the next route
            next_route, next_params = controller_method(
                self.store, self.route_params
            )

            # set the next route and input
            self.route = next_route
            self.route_params = next_params

            # if the controller returned "quit" then we end the loop
            if next_route == "quit":
                self.exit = True

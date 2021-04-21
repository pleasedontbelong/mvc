from players.models.player import Player
import subprocess as sp


class Application:
    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.controllers = {}
        self.route_params = None
        self.store = {
            "players": [
                Player(1, "Pablo", 36, "pablo@test.com"),
                Player(2, "Michel", 40, "michel@test.com"),
            ]
        }

    def register(self, controller, name):
        self.controllers[name] = controller

    def run(self):
        while not self.exit:
            # Clear the shell output
            sp.call("clear", shell=True)

            # Get the controller method that should handle our current route
            controller_method = self.controllers[self.route]().dispatch

            # Call the controller method, we pass the store and the route's
            # parameters.
            # Every controller should return two things:
            # - the next route to display
            # - the parameters needed for the next route
            next_route, next_params = controller_method(self.store, self.route_params)

            # set the next route and input
            self.route = next_route
            self.route_params = next_params

            # if the controller returned "quit" then we end the loop
            if next_route == "quit":
                self.exit = True

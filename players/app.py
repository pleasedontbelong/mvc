from players.controllers.home_controller import HomePageController
from players.models.player import Player
from players.screen import clear_screen


class Application:
    @clear_screen
    def run(self):
        store = {
            "players": [
                Player("123", "Pablo", 36, "pablo@test.com"),
                Player("456", "Michel", 40, "michel@test.com"),
                Player("789", "Juan", 25, "juan@test.com"),
                Player("101", "Pedro", 30, "pedro@test.com"),
                Player("102", "Carlos", 32, "carlos@test.com"),
                Player("103", "Luis", 33, "luis@test.com"),
                Player("104", "Maria", 34, "maria@test.com"),
                Player("105", "Ana", 35, "ana@test.com"),
                Player("106", "Jose", 36, "jose@test.com"),
                Player("107", "Luisa", 37, "luisa@test.com"),
            ]
        }
        HomePageController.main_menu(store)

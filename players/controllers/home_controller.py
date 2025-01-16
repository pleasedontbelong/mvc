from players.screen import clear_screen
from players.views.home_view import HomeView


class HomePageController:
    @classmethod
    @clear_screen
    def main_menu(cls, store=None, input=None):
        from players.controllers.player_controller import PlayerController

        choice = HomeView.home()
        if choice.lower() == "q":
            return
        elif choice == "1":
            PlayerController.list(store)
        elif choice == "2":
            raise Exception("WIP Not implemented yet")

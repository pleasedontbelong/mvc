from players.views.home_view import HomeView


class HomePage:
    def dispatch(self, store=None, input=None):
        choice = HomeView.home()
        if choice.lower() == "q":
            next = "quit"
        elif choice == "1":
            next = "player_list"
        elif choice == "2":
            next = "player_create"
        return next, None

from players.controllers.player_controller import (
    PlayerCreate,
    PlayerDelete,
    PlayerDetail,
    PlayerList,
)
from players.controllers.home_controller import HomePage
from players.app import Application


if __name__ == "__main__":
    app = Application()

    # the following could be done using a decorator on controllers
    app.register(HomePage, name="homepage")
    app.register(PlayerList, name="player_list")
    app.register(PlayerCreate, name="player_create")
    app.register(PlayerDelete, name="player_delete")
    app.register(PlayerDetail, name="player_detail")

    # start the app
    app.run()

class Player:
    def __init__(self, id, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.id = id

    def __repr__(self):
        return f"Player #{self.id} {self.name}"

    def update(self, id, name, age, email):
        self.id = id
        self.age = age
        self.name = name
        self.email = email

    def is_valid(self):
        return True


class PlayerManager:

    def __init__(self, store):
        self.store = store

    def get_player(self, player_id):
        return next(p for p in self.store["players"] if p.id == player_id)

    def get_all(self):
        return self.store["players"]
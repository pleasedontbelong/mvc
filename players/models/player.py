class Player:
    def __init__(self, id, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.id = id

    @classmethod
    def validate(self, player_dict):
        errors = []
        if not player_dict["age"].isnumeric():
            errors.append("age should be numeric")
        return errors

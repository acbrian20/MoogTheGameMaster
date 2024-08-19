import json

class CharacterProfile:
    def __init__(self, name, age, height, weight, hair, eyes, race, background, customFields):
        self.name = name
        self.age = age
        self.race = race
        self.background = background
        self.height = height
        self.weight = weight
        self.hair = hair
        self.eyes = eyes
        self.customFields = customFields

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "hair": self.hair,
            "eyes": self.eyes,
            "race": self.race,
            "background": self.background,
            "custom_fields": self.customFields
        })

class ProfileManager:
    def __init__(self):
        self.player_character = None
        self.side_character = None

    def set_player_character(self, character):
        self.player_character = character

    def set_side_character(self, character):
        self.side_character = character

    def get_profiles_json(self):
        return {
            "player_character": self.player_character.to_json() if self.player_character else None,
            "side_character": self.side_character.to_json() if self.side_character else None
        }

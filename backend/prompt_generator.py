class PromptGenerator:
    def __init__(self, static_prompt):
        self.static_prompt = static_prompt

    def generate_full_prompt(self, profiles_json):
        full_prompt = self.static_prompt + "\n\n"
        full_prompt += f"Player Character: {profiles_json['player_character']}\n"
        full_prompt += f"Side Character: {profiles_json['side_character']}\n"
        return full_prompt

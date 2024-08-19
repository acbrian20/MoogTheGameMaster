import tkinter as tk
from tkinter import ttk
from backend.character_profile import CharacterProfile, ProfileManager
from backend.prompt_generator import PromptGenerator
from backend.api_interface import APIInterface

class MainWindow:
    def __init__(self, config):
        self.root = tk.Tk()
        self.root.title(config['ui']['window_title'])
        self.root.geometry(f"{config['ui']['window_size'][0]}x{config['ui']['window_size'][1]}")

        self.profile_manager = ProfileManager()
        self.prompt_generator = PromptGenerator(config['prompt']['static_content'])
        self.api_interface = APIInterface(
            config['api']['base_url'],
            config['api']['api_key'],
            config['api']['model']
        )

        self.create_widgets()

    def create_widgets(self):
        # Create input fields for character profiles
        # Add a button to generate and start the campaign
        # Create a text area to display the campaign output
        pass

    def generate_campaign(self):
        # Get character profiles from input fields
        # Generate full prompt
        # Send prompt to API
        # Display response in the text area
        pass

    def run(self):
        self.root.mainloop()

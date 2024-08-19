import yaml
from ui.main_window import MainWindow

def load_config():
    with open('config.yaml', 'r') as config_file:
        return yaml.safe_load(config_file)

if __name__ == "__main__":
    config = load_config()
    app = MainWindow(config)
    app.run()

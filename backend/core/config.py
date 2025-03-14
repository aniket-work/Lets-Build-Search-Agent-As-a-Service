import json
import yaml
import os

# Load Config JSON
def load_json_config():
    config_path = os.path.join(os.path.dirname(__file__), "../../config/config.json")
    with open(config_path, "r") as file:
        return json.load(file)

# Load YAML Settings
def load_yaml_settings():
    settings_path = os.path.join(os.path.dirname(__file__), "../../config/settings.yaml")
    with open(settings_path, "r") as file:
        return yaml.safe_load(file)

CONFIG = load_json_config()
SETTINGS = load_yaml_settings()

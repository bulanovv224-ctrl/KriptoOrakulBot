import yaml

def load_config(path="config/config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    config = load_config()
    print("KriptoOrakulBot запущен.")
    print(f"Debug mode: {config['settings']['debug']}")

import shutil
from pathlib import Path

PLUGIN_DIR = Path(os.environ.get('XDG_CONFIG_HOME', Path.home() / '.config')) / 'ranger' / 'plugins'


def main():
    dest = PLUGIN_DIR / 'ranger_devicons'
    source = Path(__file__).resolve().parent

    PLUGIN_DIR.mkdir(parents=True, exist_ok=True)

    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(source, dest)
    print(f"Installed ranger_devicons to {dest}")


if __name__ == '__main__':
    main()

import sys
from levelup.ui import GameApp


def main() -> None:
    app = GameApp()
    try:
        app.start()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()

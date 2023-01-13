from higherlowergame.cli import CLI
from higherlowergame.game import Game
from higherlowergame.game_data import PROFILE_DATA, Profile


def main() -> None:
    cli = CLI()

    if len(PROFILE_DATA) < 2:
        cli.display_not_enough_profiles_error()
        return

    game = Game([Profile(**profile) for profile in PROFILE_DATA], cli)
    try:
        game.play()
    except KeyboardInterrupt:
        cli.display_interrupt()


if __name__ == '__main__':
    main()

from higher_lower_game.cli import CLI
from higher_lower_game.game import Game
from higher_lower_game.game_data import PROFILE_DATA, Profile


def main() -> None:
    cli = CLI()

    if len(PROFILE_DATA) < 2:
        cli.display_not_enough_profiles_error()
        return

    game = Game([Profile(**profile) for profile in PROFILE_DATA], cli)
    game.play()


if __name__ == '__main__':
    main()

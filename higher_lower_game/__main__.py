import copy
import random
from typing import Any

from higher_lower_game import game_data
from higher_lower_game.cli import CLI


def random_profile(profile_list: list[dict[str, Any]]) -> dict[str, Any]:
    """Return a random profile removed from the profile list."""
    profile = random.choice(profile_list)
    profile_list.remove(profile)

    return profile


def get_higher_profile(**profiles: dict[str, Any]) -> dict[str, Any]:
    """Return the most followed profile."""
    return max(
        profiles.values(), key=lambda profile: profile['follower_count']
    )


def main() -> None:
    cli = CLI()

    profiles_data = copy.deepcopy(game_data.DATA)

    cli.clear_console()
    cli.display_logo()

    if len(profiles_data) < 2:
        cli.display_not_enough_profiles_error()
        return

    profiles = {
        'A': random_profile(profiles_data),
        'B': random_profile(profiles_data),
    }

    score = 0
    while True:
        cli.display_profile_comparison(profiles)

        choice = cli.ask_user_choice()

        cli.clear_console()
        cli.display_logo()

        higher_profile = get_higher_profile(**profiles)

        if profiles[choice] != higher_profile:
            cli.display_player_error(score)
            break

        score += 1

        if len(profiles_data):
            cli.display_player_hit(score)
        else:
            cli.display_game_complete(score)
            break

        profiles.update(
            {'A': higher_profile, 'B': random_profile(profiles_data)}
        )


if __name__ == '__main__':
    main()

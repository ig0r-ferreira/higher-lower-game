import random

from higher_lower_game.cli import CLI
from higher_lower_game.game_data import Profile


def get_higher_profile(*profiles: Profile) -> Profile:
    """Return the most followed profile."""
    return max(profiles, key=lambda profile: profile.follower_count)


class Game:
    """Class that represents the game."""

    def __init__(self, profile_list: list[Profile], cli: CLI) -> None:
        self._cli = cli
        self._score = 0
        self._all_profiles = profile_list
        self._profile_a = self._take_random_profile()
        self._profile_b = self._take_random_profile()

    def _take_random_profile(self) -> Profile:
        """Return a random profile removed from the profile list."""
        profile = random.choice(self._all_profiles)
        self._all_profiles.remove(profile)
        return profile

    def _increase_score(self) -> None:
        """Increase the score."""
        self._score += 1

    def _has_profiles_available(self) -> bool:
        """Return if there are profiles available for comparison."""
        return bool(len(self._all_profiles))

    def play(self) -> None:
        """Start the game."""
        self._cli.clear_console()
        self._cli.display_logo()

        while True:
            self._cli.display_profile_comparison(
                self._profile_a, self._profile_b
            )
            choice = self._cli.ask_user_choice()

            self._cli.clear_console()
            self._cli.display_logo()

            higher_profile = get_higher_profile(
                self._profile_a, self._profile_b
            )

            profiles = {'A': self._profile_a, 'B': self._profile_b}

            if profiles[choice] != higher_profile:
                self._cli.display_player_error(self._score)
                break

            self._increase_score()

            if self._has_profiles_available():
                self._cli.display_player_hit(self._score)
            else:
                self._cli.display_game_complete(self._score)
                break

            self._profile_a = higher_profile
            self._profile_b = self._take_random_profile()

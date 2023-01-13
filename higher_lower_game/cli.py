from rich.align import Align
from rich.console import Console, RenderableType
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

from higher_lower_game import art
from higher_lower_game.game_data import Profile


def _format_profile_display(profile: Profile, style: str = '') -> Text:
    """Return a text formatted with profile data."""
    return Text(
        f'{profile.name}, a {profile.description}, from {profile.country}',
        style=style,
        justify='center',
    )


def _center_element(element: RenderableType, orient: str = 'both') -> Align:
    """
    Return a center-aligned element.

    Args:
        element (RenderableType): The renderable element that will be centered.
        orient (str, optional): Orientation optional. One of "both", "vertical"
        or "horizontal". Default is "both".
    Returns:
        Align: A center-aligned element.
    """
    match orient:
        case 'both':
            return Align(element, align='center', vertical='middle')
        case 'horizontal':
            return Align(element, align='center')
        case 'vertical':
            return Align(element, vertical='middle')
        case _:
            raise ValueError("Invalid option for 'orient' param.")


def _generate_profile_panel(
    id: str, profile: Profile, border_style: str = 'none'
) -> Panel:
    """Return a panel whose profile data is centered."""
    return Panel(
        _center_element(_format_profile_display(profile)),
        title=f'Profile {id}',
        border_style=border_style,
    )


class CLI:
    """A class used to represent a CLI."""

    def __init__(self) -> None:
        self.console = Console()
        self.width = 100

    def clear_console(self) -> None:
        """Clear console."""
        self.console.clear()

    def display_logo(self) -> None:
        """Display LOGO."""
        self.console.print(
            _center_element(Text(art.LOGO, style='#FF8A00')), width=self.width
        )

    def display_not_enough_profiles_error(self) -> None:
        """Display not enough profiles error."""
        self.console.print(
            'Error: Not enough profiles.\n',
            style='bright_red',
            width=self.width,
        )

    def display_profile_comparison(
        self, profile_a: Profile, profile_b: Profile
    ) -> None:
        """Display profile comparison."""
        layout = Layout()
        layout.split_row(
            _generate_profile_panel('A', profile_a, '#0072F9'),
            _center_element(Text(art.VS, style='#FFD700')),
            _generate_profile_panel('B', profile_b, '#FF2000'),
        )

        self.console.print(layout, height=10, width=self.width)

    def display_player_hit(self, score: int) -> None:
        """Show the player that he got it right."""
        self.console.print(
            f"You're right. Current score: {score}.\n",
            style='bright_green',
            width=self.width,
            justify='center',
        )

    def display_player_error(self, score: int) -> None:
        """Show the player that he made a mistake."""
        self.console.print(
            f"Sorry, that's wrong. Final score: {score}.\n",
            style='bright_red',
            width=self.width,
            justify='center',
        )

    def ask_user_choice(self) -> str:
        """Ask the user which option he wants from the available ones."""
        guess = Prompt.ask(
            '\nWho has more followers? [#FF8A00][A/B][/]',
            choices=['a', 'A', 'b', 'B'],
            show_choices=False,
        ).upper()
        return guess

    def display_game_complete(self, score: int) -> None:
        """Show the player that he has completed the game."""
        self.console.print(
            'Congratulations, you got them all right. '
            f'Final score: {score}.\n',
            style='bright_green',
            width=self.width,
            justify='center',
        )

    def display_interrupt(self) -> None:
        self.console.print('\n^C', end='')

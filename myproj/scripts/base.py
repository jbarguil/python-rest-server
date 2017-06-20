"""Base script.
"""

import config


_COLOR_RESET = '\033[0m'


def print_env_alert():
    """Displays a colorful alert to the user if they're running in PROD.
    """
    dbg = config.config.DEBUG

    msg = '{}{} Running in {} {}! {}'.format(
        '' if dbg else '\033[101;93;1m WARNING! ',  # Red "WARNING!" if prod.
        _COLOR_RESET,
        '\033[42;1m' if dbg else '\033[101;1m',     # Red if prod else green.
        config.deploy,
        _COLOR_RESET,
    )

    print(msg)


def prompt_to_continue():
    """Displays a colorful alert to the user if they're running in PROD.

    Prompts for them to press <enter> to continue.
    """
    print_env_alert()
    raw_input(
        ' Press {}enter{} to continue or {}ctrl+C{} to abort: '.format(
            '\033[32m',     # Green.
            _COLOR_RESET,
            '\033[91m',     # Red.
            _COLOR_RESET))


def prompt_then_execute(func):
    """Displays a colorful alert to the user if they're running in PROD.

    Prompts for them to press <enter> to continue, then executes func.
    """
    try:
        prompt_to_continue()

        # Executes the function received as an argument.
        func()

        print(' Done.')
    except KeyboardInterrupt:
        print('\n\n Aborting...')

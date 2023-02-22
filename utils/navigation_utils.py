from utils.store_constants import COMMANDS


def print_all_commands():
    """
    Get all console store commands
    :return: dictionary
    """
    for cmd in list(COMMANDS.keys()):
        print(f"\t - {cmd}: {COMMANDS[cmd]}")


import os
import re

import inquirer
from rich import print

from decorators import *

git_commands = {
    "commit": [
        {
            "alias": "🔧 fix",
            "description": "A bug fix",
            "command": ["git add .", "git commit -m \"🔧 fix: <description> ~ <file> \"", "git push"],
        },
        {
            "alias": "✨ add",
            "description": "Added a new feature",
            "command": ["git add .", "git commit -m \"✨ add: <description> ~ <file> \"", "git push"],
        },
        {
            "alias": "♻️ refactor",
            "description": "Refactored code",
            "command": ["git add .", "git commit -m \"♻️ refactor  <description> ~ <file> \"", "git push"],
        },
        {
            "alias": "🔨 chore",
            "description": "A code change that neither fixes a bug nor adds a feature",
            "command": ["git add .", "git commit -m \"🔨 chore: <description> ~ <file> \"", "git push"],
        },
        {
            "alias": "🚀 perf",
            "description": "Perfomance improvement",
            "command": ["git add .", "git commit -m \"🚀 perf: <description> ~ <file> \"", "git push"],
        },
        {
            "alias": "📝 docs",
            "description": "Documentation changes",
            "command": ["git add .", "git commit -m \"📝 docs: <description> ~ <file> \"", "git push"],
        }
    ]
}


@clear_screen
@press_to_continue
def use_git_commands():
    git_commands_view = []
    for idx, group in enumerate(git_commands):
        print(f"[bold]{group}[/]")

        choices = []

        for command in git_commands[group]:
            choice = (
                f"{command['alias']} - {command['description']}", command["command"])
            choices.append(choice)

        git_commands_view.append(
            inquirer.List(
                "command",
                message="A",
                carousel=True,
                choices=choices
            )
        )

    answers = inquirer.prompt(git_commands_view)
    command = parse_command(answers["command"])

    print("-" * 50)

    os.system(command)


def parse_command(commands):
    command = " && ".join(commands)

    matches = re.findall(r"<(.*?)>", command)
    for match in set(matches):
        user_input = input(f"{match}: ")
        command = command.replace(f"<{match}>", user_input)

    print(command)

    return command


def create_new_git_command():
    print("create_new_git_command")


def delete_command():
    print("delete_command")


if __name__ == "__main__":
    home_view = [inquirer.List("action", message="What do you want to do?",  carousel=True,
                               choices=[
                                   ('Use git commands', use_git_commands),
                                   ('Create new git commnad',
                                       create_new_git_command),
                                   ('Delete command', delete_command),
                                   ('Exit', exit)
                               ])]

    while True:
        answers = inquirer.prompt(home_view)
        answers["action"]()

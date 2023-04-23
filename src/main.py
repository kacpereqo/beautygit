import msvcrt as m
import os

import inquirer
from rich import print

git_commands = {
    "commit": [
        {
            "alias": "🔧 fix",
            "description": "A bug fix",
            "command": ["git add .", "git commit -m \"🔧 fix: <description>\"", "git push"],
        },
        {
            "alias": "✨ add",
            "description": "Added a new feature",
            "command": ["git add .", "git commit -m \"✨ add: <description>\"", "git push"],
        },
        {
            "alias": "♻️ refactor",
            "description": "Refactored code",
            "command": ["git add .", "git commit -m \"♻️ refactor: <description>\"", "git push"],
        },
        {
            "alias": "🔨 chore",
            "description": "A code change that neither fixes a bug nor adds a feature",
            "command": ["git add .", "git commit -m \"🔨 chore: <description>\"", "git push"],
        },
        {
            "alias": "🚀 perf",
            "description": "Perfomance improvement",
            "command": ["git add .", "git commit -m \"🚀 perf: <description>\"", "git push"],
        },
        {
            "alias": "📝 docs",
            "description": "Documentation changes",
            "command": ["git add .", "git commit -m \"📝 docs: <description>\"", "git push"],
        }
    ]
}


def use_git_commands():
    git_commands_view = []
    for idx, group in enumerate(git_commands):
        print(f"[bold]{group}[/]")
        git_commands_view.append(
            inquirer.List(
                "command",
                message="A",
                carousel=True,
                choices=[
                    (f"{command['alias']} - {command['description']}", command["command"]) for command in git_commands[group]]
            )
        )

    answers = inquirer.prompt(git_commands_view)
    os.system(" && ".join(answers["command"]))
    print("\nPress any key to continue...")
    m.getch()


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

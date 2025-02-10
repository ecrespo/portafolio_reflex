import reflex as rx
from reflex_github_badge.github_badge import github_badge


def GithubCard(username:str) -> rx.Component:
    return github_badge(
        username=username,
        description="Hello world 👋",

    )
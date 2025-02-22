from typing import List, Dict

import reflex as rx




def BarProgress(value=100, color_scheme="tomato") -> rx.Component:
    return rx.progress(value=value,size="1",radius=None,color_scheme=color_scheme)


def skill_bar_progress(value: int = 100,color: str = "pink", text: str = "Prueba") -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(text),
            BarProgress(value=value,color_scheme=color),
        ),
        width="100%"
    )

items: List[Dict] = [
{
            "value": 50,
            "color": "pink",
            "text": "Python"
        },
        {
            "value": 10,
            "color": "brown",
            "text": "Golang"
        }
]

def vertical_skills_bars(items) -> rx.Component:
    return rx.vstack(
        rx.foreach(items,skill_bar_progress),
        width="50%"
    )

def horizontal_skills_bars(items) -> rx.Component:
    return rx.hstack(
        rx.foreach(items,vertical_skills_bars),
        width="100%"
    )


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Pruebas"),
            rx.card(
                rx.vstack(
                rx.center(rx.heading("Skills"),width="100%"),
                horizontal_skills_bars(vitems),
                width = "100%"
            ),
            width = "100%",
        ),
    width="100%"
    )

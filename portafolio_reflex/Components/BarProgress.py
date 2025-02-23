from typing import List, Dict

import reflex as rx



def BarProgress(value=100, color_scheme="tomato") -> rx.Component:
    return rx.progress(value=value,size="1",radius=None,color_scheme=color_scheme)


def skill_bar_progress(item: Dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(item.get("text")),
            BarProgress(value=item.get("value"),color_scheme=item.get("color")),
        ),
        width="100%"
    )


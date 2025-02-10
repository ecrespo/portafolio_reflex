import reflex as rx

class Timeline(rx.Component):
    """Timeline Component"""

    library = "@antd/Timeline"

    tag = "Timeline"

    is_default = True
    mode: rx.Var[str]
    
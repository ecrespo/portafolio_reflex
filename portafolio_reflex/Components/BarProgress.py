import reflex as rx




def BarProgress(value=100, color_scheme="tomato") -> rx.Component:
    return rx.progress(value=value,size="1",radius=None,color_scheme=color_scheme)

"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from portafolio_reflex.Components.BarProgress import BarProgress
from portafolio_reflex.Components.GithubComponent import GithubCard
from portafolio_reflex.Components.SplineComponent import spline
from portafolio_reflex.Components.LinkedinComponent import Linkedin
from portafolio_reflex.Components.BarProgress import BarProgress
import RIL as icons
from reflex_qrcode import QRCode
from reflex_motion import motion
from reflex_calendar import calendar
from rxconfig import config


class State(rx.State):
    """The app state."""
    ...

dots:dict = {
    "@keyframes dots": {
        "0%": {
            "background_position": "0 0 ",
        },
        "100%": {
            "background_position": "40px 40px",
        }
    },
    "animation": "dots 4s linear infinite alternate-reverse both"
}

wave:dict = {
    "@keyframes wave": {
        "0%": {
            "transform": "rotate(45deg)",
        },
        "100%": {
            "transform": "rotate(-15deg)",
        }
    },
    "animation": "wave 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite alternate-reverse both"
}

css:dict = {
    "app": {
        "_dark":{
            "bg": "#15171b"
        },
    },
    "header": {
        "width": "100%",
        "height": "50px",
        "padding": [
            "0rem 1rem",
            "0rem 1rem",
            "0rem 1rem",
            "0rem 8rem",
            "0rem 8rem",
        ],
        "transition": "all 550ms ease"
    },
    "main": {
        "property": {
            "width": "100%",
            "height": "84vh",
            "padding": "15rem 0rem",
            "align_items": "center",
            "justify_content": "start",


        }
    }
}


class Header:
    def __init__(self):
        self.header: rx.Hstack() = rx.hstack(style=css.get("header"))
        self.email: rx.Hstack() = rx.hstack(
            rx.box(
                rx.icon(tag="mail",
                        _dark={"color": "rgba(255,255,255,0.5)"})
            ),
            rx.box(
                rx.text("ecrespo@gmail.com",_dark={"color": "rgba(255,255,255,0.5)"})
            ),
            align_items="center",
            justify_content="center"
        )
        #self.float_button:FloatButton = FloatButton()
        self.theme:rx.Component() = rx.color_mode.button(_light={"color": "black"},_dark={"color":"white"})

    def compile_component(self)-> list:
        return [self.email,rx.spacer(),self.theme]

    def build(self):
        self.header.children = self.compile_component()
        return self.header


# main content area
class Main:
    def __init__(self):
        self.box:rx.Box = rx.box(width="100%")
        self.name:rx.Hstack = rx.hstack(
            rx.heading(
                "Hi - I'm Seraph",
                font_size=["2rem","2.85rem","4rem","5rem","5rem"],
                font_weight="900",
                _dark={
                    "background":"linear-gradient(to right, #e1e1e1, #757575)",
                    "background_clip":"text"
                }
            ),
            rx.heading("👋", size="8",style=wave),
            spacing="2"
        )
        self.badge_stack_max: rx.Hstack = rx.hstack(spacing="1")
        self.badge_stack_min: rx.Vstack = rx.vstack(spacing="1")
        titles:list = ["Software Engineer", "Data Engineer", "AI Engineer"]
        self.badge_stack_max.children = [self.create_badges(title) for title in titles]
        self.badge_stack_min.children = [self.create_badges(title) for title in titles]
        #self.crumbs: rx.Breadcrumb = rx.breadcrum()
        data: list = [
            ["/github.png","Github","#"],
            ["/linkedin.png", "Linkedin", "#"],
            ["/mastodon.png", "Mastodon", "#"],
        ]
        #self.crumbs.children = [self.create_breadcrum_items(path, title, url) for path,item,url in data]



    # def create_breadcrum_items(self,path: str, title: str, url: str|None):
    #     return rx.breadcrum_item(
    #         rx.hstack(
    #             rx.image(src=path, html_width="24px", html_height="24px", _dark={"filter": "brightness(0) invert(1)"}),
    #             rx.breadcrum_link(title, href=url, _dark={"color":"rgba(255,255,255,0.7)"})
    #         ),
    #     )

    def create_badges(self, title: str):
        return rx.badge(
            title,
            variant="solid",
            padding=[
                "0.15rem 0.35rem",
                "0.15rem 0.35rem",
                "0.15rem 1rem",
                "0.15rem 1rem",
                "0.15rem 1rem"
            ]
        )

    def compile_desktop_component(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                self.badge_stack_max,
                # self.crumbs,
                # spline(
                #     scene="https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"
                # ),
                #Linkedin(fullname="ernestocrespo"),
                #GithubCard("ecrespo"),
                rx.hstack(
                    icons.fontawesome.solid("house"),
                    icons.simple("python"),
                    icons.material("Search"),
                    icons.octicons("check-circle-fill"),
                    icons.phosphor("acorn"),
                    icons.bootstrap("airplane"),
                ),
                # QRCode(
                #     title="Title",
                #     value="Value"
                # ),
                # motion(
                #     rx.button(
                #         "Bounce me!",
                #     ),
                #     while_hover={"scale": 1.2},
                #     while_tap={"scale": 0.9},
                #     transition={"type": "spring", "stiffness": 400, "damping": 17},
                # ),
                # calendar(),
                #rx.hstack(BarProgress(75),BarProgress(20)),
                style=css.get('main').get("property")
            )
        )
#"dayana-ovalle-a32508151"
    def compile_mobile_component(self):
        return rx.mobile_only(
            rx.vstack(
                self.name,
                self.badge_stack_min,
                #self.crumbs,
                # spline(
                #     scene="https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"
                # ),
                Linkedin(fullname="ernestocrespo"),
                GithubCard("ecrespo"),
                style=css.get('main').get("property")
            )
        )

    def build(self):
        self.box.children = [self.compile_desktop_component(),] #self.compile_mobile_component()]
        return self.box


class Footer:
    ...


#@rx.page(route="/")
def landing() -> rx.Component:
    header:object = Header().build()
    main:object = Main().build()
    return rx.vstack(
        header,
        main,
        # background
        _light={
            "background":"radial-gradient(circle,rgba(0,0,0,0.35) 1px, transparent 1px)",
            "background_size" : "25px 25px",
        },
        background="radial-gradient(circle,rgba(255,255,255,0.09) 1px, transparent 1px)",
        background_size="25px 25px",
        style=dots,
    )

@rx.page(route="/")
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Pruebas"),
            rx.card(
                rx.vstack(
                rx.center(rx.heading("Skills"),width="100%"),
                rx.hstack(
                    rx.vstack(
                        rx.card(
                            rx.vstack(
                                rx.text("Python"),
                                BarProgress(20, "pink"),
                            ),
                            width="100%"
                        ),
                        rx.card(
                            rx.vstack(
                                rx.text("Linux"),
                                BarProgress(90, "blue"),
                            ),
                            width="100%"
                        ),
                        rx.card(
                            rx.vstack(
                                rx.text("Pandas"),
                                BarProgress(95, "orange"),
                            ),
                            width="100%"
                        ),
                        width="50%"
                    ),
                    rx.vstack(
                        rx.card(
                            rx.vstack(
                                rx.text("Goland"),
                                BarProgress(25, "yellow"),
                            ),
                            width="100%"
                        ),
                        rx.card(
                            rx.vstack(
                                rx.text("FastAPI"),
                                BarProgress(90, "green"),
                            ),
                            width="100%"
                        ),
                        rx.card(
                            rx.vstack(
                                rx.text("Rust"),
                                BarProgress(15, "brown"),
                            ),
                            width="100%"
                        ),
                        width="50%"
                        ),
                        width="100%"
                    ),
                    width="100%"
                ),
                width = "100%"
            ),
            width = "100%",
        ),
    width="100%"
    )

app = rx.App(style=css.get("app"))

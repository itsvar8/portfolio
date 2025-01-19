import reflex as rx
from rxconfig import config  # noqa
from . import pages  # noqa
from . import ui

# with open(os.path.join(os.getcwd(), "assets", "intro.txt"), encoding="utf-8") as f:
#     _intro = f.read()

_intro = """Over the past three years, I’ve dedicated myself to mastering 3D modeling and 3D printing, building on my previous experience in photography and graphic design as a digital printing specialist.
Recently, I’ve focused on expanding my knowledge further by learning Python, which I’ve been studying intensively for the last eight months.
Here, you'll find examples that showcase my journey in 3D design, printing, and coding, highlighting my commitment to growth in cutting-edge technologies."""


class State(rx.State):
    intro: list[str] = _intro.split("\n")  # noqa


def content(mobile_tablet=False):
    return rx.vstack(
        rx.heading("Welcome to my portfolio!", size="9" if not mobile_tablet else "8"),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        rx.vstack(
            rx.foreach(State.intro, lambda s: rx.text(s, size="5" if not mobile_tablet else "4")),
            spacing="0",
        ),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        ui.welcome_card("3D Modeling", "/lamp_transparent.png", "/modeling"),
        ui.welcome_card("Python", "/python_logo.png", "/python", True),
        ui.welcome_card("Projects", "/light_bulb.png", "/projects"),
        ui.welcome_card("About me", "/profile_image_circle_800px.png", "/about", True),
        ui.welcome_card("Contacts", "/gmail.webp", "/contacts"),
        spacing="5" if not mobile_tablet else "3",
        align="stretch",
        margin_left="16em" if not mobile_tablet else "auto",
        padding_x="18vw" if not mobile_tablet else "6vw",
        padding_y="8vh" if not mobile_tablet else "2vh",
    )


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode.button(position="top-right"),
        ui.sidebar(),
        rx.desktop_only(
            content(),
            ui.footer(),
        ),
        rx.mobile_and_tablet(
            content(mobile_tablet=True),
            ui.footer(mobile_tablet=True),
        ),
    )


app = rx.App(
    theme=rx.theme(
        radius="large",
        # appearance="dark",
        accent_color="cyan",
    ),
)
app.add_page(index, title=f"Var's Portfolio | Welcome")

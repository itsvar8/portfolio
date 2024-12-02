import os
import reflex as rx
from portfolio_reflex import ui

with open(
    os.path.join(os.getcwd(), "assets", "about_me.txt"),
    encoding="utf-8",
) as f:
    about = f.read()

icons = dict()
for root, dirs, files in os.walk(os.path.join("assets", "software_icons"), topdown=False):
    for icon in sorted(files, reverse=True):
        icons[icon.split(".")[0].capitalize()] = os.path.join(root.replace("assets", ""), icon)


class State(rx.State):
    about: list[str] = about.split("\n")  # noqa
    sw_icons: dict[str, str] = icons  # noqa


def image_with_caption(image):
    return rx.fragment(
        rx.desktop_only(
            rx.vstack(
                rx.image(image[1]),
                rx.text(f"{image[0]}", size="4"),
                align="center",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.image(image[1]),
                rx.text(f"{image[0]}", size="2"),
                align="center",
            )
        ),
    )


def content(mobile_tablet=False):
    return rx.vstack(
        rx.heading("About me", size="9" if not mobile_tablet else "8"),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        rx.card(
            rx.hstack(
                rx.vstack(
                    rx.heading("Hello!", size="8"),
                    rx.divider(color_scheme="cyan"),
                    rx.vstack(
                        rx.foreach(State.about, lambda s: rx.text(s, size="5" if not mobile_tablet else "4")),
                        spacing="0",
                    ),
                    width="65%",
                ),
                rx.image(src="/profile_image_circle_800px.png", width="30%"),
                wrap="wrap",
                justify="center",
            ),
            padding="1em",
        ),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        rx.heading("Software I already use:", size="8" if not mobile_tablet else "7", padding_bottom="2vh"),
        rx.grid(
            rx.foreach(State.sw_icons, image_with_caption),
            columns="4",
            wrap="wrap",
            spacing="5",
            justify="center",
        ),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        ui.bottom_buttons(),
        spacing="5" if not mobile_tablet else "3",
        margin_left="16em" if not mobile_tablet else "auto",
        padding_x="18vw" if not mobile_tablet else "6vw",
        padding_y="8vh" if not mobile_tablet else "2vh",
    )


@rx.page(title=f"Var's Portfolio | About me")
def about() -> rx.Component:
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

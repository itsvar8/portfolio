import os
import time
import reflex as rx
from portfolio_reflex import ui

_renders = list()
for root, dirs, files in os.walk(os.path.join("assets", "renders"), topdown=False):
    for icon in sorted(files, reverse=False):
        _renders.append(os.path.join(root.replace("assets", ""), icon))


class ModelingState(rx.State):
    renders: list[str] = _renders  # noqa


def content(mobile_tablet=False):
    return rx.fragment(
        rx.vstack(
            rx.heading("3D Modeling", size="9" if not mobile_tablet else "8"),
            rx.divider(color_scheme="cyan", margin_y="2vh"),
            spacing="5" if not mobile_tablet else "3",
            margin_left="16em" if not mobile_tablet else "auto",
            padding_x="18vw" if not mobile_tablet else "6vw",
            padding_top="8vh" if not mobile_tablet else "2vh",
        ),
        rx.vstack(
            rx.grid(
                rx.foreach(ModelingState.renders, lambda img: ui.dialog_image(img, "1")),
                columns="4" if not mobile_tablet else "2",
                spacing="5" if not mobile_tablet else "2",
            ),
            align="center",
            spacing="5" if not mobile_tablet else "3",
            margin_left="16em" if not mobile_tablet else "auto",
            padding="2vw",
        ),
        rx.vstack(
            rx.divider(color_scheme="cyan", margin_y="2vh"),
            rx.image("/5_4_macropad.gif", width="100%", border_radius="1rem"),
            align="center",
            spacing="5" if not mobile_tablet else "3",
            margin_left="16em" if not mobile_tablet else "auto",
            padding_x="18vw" if not mobile_tablet else "6vw",
            padding_y="2vw",
        ),
        rx.vstack(
            rx.divider(color_scheme="cyan", margin_y="2vh"),
            ui.bottom_buttons(),
            spacing="5" if not mobile_tablet else "3",
            margin_left="16em" if not mobile_tablet else "auto",
            padding_x="18vw" if not mobile_tablet else "6vw",
            padding_bottom="8vh" if not mobile_tablet else "2vh",
        ),
    )


@rx.page(title=f"Var's Portfolio | 3D Modeling")
def modeling() -> rx.Component:
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

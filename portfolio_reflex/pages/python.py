import reflex as rx
from portfolio_reflex import ui


class State(rx.State):
    pass


def content(mobile_tablet=False):
    return rx.vstack(
        rx.heading("Python", size="9" if not mobile_tablet else "8"),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        rx.heading("This webapp...", size="7" if not mobile_tablet else "6"),
        rx.text(
            "...is completely written in Python using the open-source framework ",
            rx.link("Reflex", href="https://reflex.dev", is_external=True),
            ".",
            size="5" if not mobile_tablet else "4",
        ),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        ui.bottom_buttons(),
        spacing="5" if not mobile_tablet else "3",
        margin_left="16em" if not mobile_tablet else "auto",
        padding_x="18vw" if not mobile_tablet else "6vw",
        padding_top="8vh" if not mobile_tablet else "2vh",
        padding_bottom="2vh",
        height="80vh" if not mobile_tablet else "70vh",
    )


@rx.page(title=f"Var's Portfolio | Python")
def python() -> rx.Component:
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

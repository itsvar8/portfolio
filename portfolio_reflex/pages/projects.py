import reflex as rx
from portfolio_reflex import ui


def content(mobile_tablet=False):
    return rx.vstack(
        rx.heading("Projects", size="9" if not mobile_tablet else "8"),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        ui.welcome_card("Cornepad", "/cornepad/cornepad_square.png", "/projects/cornepad"),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        ui.bottom_buttons(),
        spacing="5" if not mobile_tablet else "3",
        margin_left="16em" if not mobile_tablet else "auto",
        padding_x="18vw" if not mobile_tablet else "6vw",
        padding_y="8vh" if not mobile_tablet else "2vh",
        height="80vh" if not mobile_tablet else "75vh",
    )


@rx.page(title=f"Var's Portfolio | Projects")
def projects() -> rx.Component:
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

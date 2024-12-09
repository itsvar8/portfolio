import reflex as rx
from portfolio import ui


def content(mobile_tablet=False):
    return rx.vstack(
        rx.heading("Contacts", size="9" if not mobile_tablet else "8"),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        rx.flex(
            rx.hstack(
                rx.image(src="/gmail.webp", width="4em"),
                rx.heading("itsvar8@gmail.com"),
                align="center",
                wrap="wrap",
                on_click=rx.redirect("mailto:itsvar8@gmail.com"),
                _hover={
                    "cursor": "pointer",
                },
            ),
            justify="center",
            width="100%",
        ),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        ui.bottom_buttons(),
        spacing="5" if not mobile_tablet else "3",
        margin_left="16em" if not mobile_tablet else "auto",
        padding_x="18vw" if not mobile_tablet else "6vw",
        padding_y="8vh" if not mobile_tablet else "2vh",
        height="80vh" if not mobile_tablet else "70vh",
    )


@rx.page(title=f"Var's Portfolio | Contacts")
def contacts() -> rx.Component:
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

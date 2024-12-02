import reflex as rx
from sqlalchemy import True_


def card(text, image, redirect, inverted, mobile_tablet=False):
    flippable = [
        rx.image(src=image, width="35%", border_radius="1rem"),
        rx.vstack(
            rx.heading(text, size="8" if not mobile_tablet else "7"),
            rx.divider(color_scheme="cyan"),
            align="end" if not inverted else "start",
            width="60%",
        ),
    ]
    return rx.card(
        rx.hstack(
            flippable if not inverted else flippable[::-1],
            wrap="wrap",
            justify="center",
        ),
        on_click=rx.redirect(redirect),
        _hover={
            "cursor": "pointer",
            "background-image": f"linear-gradient({rx.color('slate', 1)}, {rx.color('accent', 4)})",
        },
        padding="1em",
        bg=rx.color("slate", 1),
    )


def welcome_card(text, image, redirect, inverted=False):
    return rx.fragment(
        rx.desktop_only(card(text, image, redirect, inverted)),
        rx.mobile_and_tablet(card(text, image, redirect, inverted, mobile_tablet=True)),
        width="100%",
    )

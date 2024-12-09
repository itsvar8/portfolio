import reflex as rx


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer(mobile_tablet=False) -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.text(
                "© 2024 Andrea Varotto, All rights reserved. ",
                "No part of this website may be reproduced or distributed without prior written permission from the copyright owner",
                size="2",
            ),
            rx.divider(color_scheme="cyan"),
            rx.hstack(
                rx.link(rx.text("Privacy and Cookies Policy", size="3"), href="/privacy-cookies", width="100%"),
                # socials(),
                justify_items="between",
                width="100%",
            ),
            align="center",
            spacing="5",
            width="100%",
            height="100%",
        ),
        align_items="end",
        margin_left="16em" if not mobile_tablet else "auto",
        padding_x="18vw" if not mobile_tablet else "6vw",
        padding_y="2vh",
    )

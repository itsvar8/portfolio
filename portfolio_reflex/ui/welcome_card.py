import reflex as rx


def card(
    text: str,
    image: str,
    redirect: str,
    inverted: bool,
    external: bool,
    description: None | str,
    mobile_tablet: bool = False,
):
    vstack_elements = [
        rx.heading(text, size="8" if not mobile_tablet else "7"),
        rx.divider(color_scheme="cyan"),
    ]
    if description:
        vstack_elements.append(
            rx.text(description, size="5" if not mobile_tablet else "4", align="right" if not inverted else "left")
        )
    return rx.card(
        rx.hstack(
            rx.image(src=image, width="35%", border_radius="1rem"),
            rx.vstack(
                vstack_elements,
                align="end" if not inverted else "start",
                width="60%",
            ),
            direction="row" if not inverted else "row-reverse",
            wrap="wrap",
            justify="center",
        ),
        on_click=rx.redirect(redirect, external=external),
        _hover={
            "cursor": "pointer",
            "background-image": f"linear-gradient({rx.color('slate', 1)}, {rx.color('accent', 4)})",
        },
        padding="1em",
        bg=rx.color("slate", 1),
    )


def welcome_card(
    text: str,
    image: str,
    redirect: str,
    inverted: bool = False,
    external: bool = False,
    description: None | str = None,
):
    return rx.fragment(
        rx.desktop_only(card(text, image, redirect, inverted, external, description)),
        rx.mobile_and_tablet(card(text, image, redirect, inverted, external, description, mobile_tablet=True)),
    )

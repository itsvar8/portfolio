import reflex as rx


def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon) if not icon.endswith("png") else rx.image(src=icon, width="1.5em"),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            _hover={
                "bg": rx.color("accent", 4),
                "color": rx.color("accent", 11),
                "transform": "scale(1.05)",
            },
            border_radius="0.5em",
            transform="scale(1)",
            transition="transform 0.3s ease",
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Welcome", "hand", "/"),
        sidebar_item("3D Modeling", "box", "/modeling"),
        sidebar_item("Python", "bot", "/python"),
        sidebar_item("Projects", "lightbulb", "/projects"),
        sidebar_item("About me", "user-round", "/about"),
        sidebar_item("Contacts", "mail", "/contacts"),
        spacing="1",
        width="100%",
    )


def heading():
    return rx.hstack(
        rx.image(
            src="/icon.png",
            width="2em",
            height="auto",
            border_radius="25%",
        ),
        rx.heading("varotto.work", size="5", weight="bold"),
        align="center",
        justify="start",
        padding_x="0.5rem",
        width="100%",
        on_click=rx.redirect("/"),
        _hover={
            "cursor": "pointer",
        },
    )


def sidebar() -> rx.Component:
    return rx.fragment(
        rx.desktop_only(
            rx.vstack(
                heading(),
                sidebar_items(),
                spacing="5",
                position="fixed",
                z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                # bg=rx.color("accent", 2),
                bg=rx.color("slate", 2),
                align="start",
                height="100%",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(rx.icon("align-justify", size=30)),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(rx.icon("x", size=30)),
                                width="100%",
                            ),
                            heading(),
                            sidebar_items(),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        # bg=rx.color("accent", 2),
                        bg=rx.color("slate", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )

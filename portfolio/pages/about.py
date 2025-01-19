import reflex as rx
from portfolio import ui

# with open(
#         os.path.join(os.getcwd(), "assets", "about_me.txt"),
#         encoding="utf-8",
# ) as f:
#     _about = f.read()

_about = """I'm Andrea Varotto, I live in northeast Italy, and I'll be soon father for the second time.
I've been passionate about PCs since I was a kid and always need to be learning something new in tech to feel at my best.
I plan to dive into Rust next, and I'm also considering taking Japanese lessons.
One language for machines and one for humans, I guess!"""

_icons = {
    "Solidworks": "software_icons\\01_3D\\solidworks.png",
    "Onshape": "software_icons\\01_3D\\onshape.png",
    "Fusion": "software_icons\\01_3D\\fusion.png",
    "Blender": "software_icons\\01_3D\\blender.png",
    "Prusaslicer": "software_icons\\02_slicers\\prusaslicer.png",
    "Cura": "software_icons\\02_slicers\\cura.png",
    "Chitubox": "software_icons\\02_slicers\\chitubox.png",
    "Photoshop": "software_icons\\03_2D\\photoshop.png",
    "Lightroom": "software_icons\\03_2D\\lightroom.png",
    "Illustrator": "software_icons\\03_2D\\illustrator.png",
    "Resolve": "software_icons\\resolve.png",
    "Kicad": "software_icons\\kicad.png",
}

_certificates = {
    "What Is Data Science": "certificates\\01 What is Data Science.jpg",
    "Tools For Data Science": "certificates\\02 Tools for Data Science.jpg",
    "Data Science Methodology": "certificates\\03 Data Science Methodology.jpg",
}


class State(rx.State):
    about: list[str] = _about.split("\n")  # noqa
    sw_icons: dict[str, str] = _icons  # noqa
    certificates: dict[str, str] = _certificates  # noqa


def image_with_caption(image):
    return rx.fragment(
        rx.desktop_only(
            rx.vstack(
                rx.image(f"/{image[1]}"),
                rx.text(f"{image[0]}", size="4"),
                align="center",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.image(f"/{image[1]}"),
                rx.text(f"{image[0]}", size="2"),
                align="center",
            )
        ),
    )


def certificate_with_caption(image):
    return rx.fragment(
        rx.desktop_only(
            rx.vstack(
                ui.dialog_image(f"{image[1]}"),
                rx.text(f"{image[0]}", size="4"),
                align="center",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                ui.dialog_image(f"{image[1]}"),
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
        rx.heading("My certificates and CV:", size="8" if not mobile_tablet else "7", padding_bottom="2vh"),
        rx.grid(
            rx.foreach(State.certificates, certificate_with_caption),
            columns="2",
            wrap="wrap",
            spacing="5",
            justify="center",
        ),
        rx.hstack(
            rx.button(
                rx.icon("notebook-text"),
                "Open CV",
                on_click=rx.redirect(
                    "https://europa.eu/europass/eportfolio/api/eprofile/shared-profile/andrea-varotto/1f56ec1a-c473-40b2-a331-f06a211bbb62?view=html",
                    external=True,
                ),
                _hover={
                    "cursor": "pointer",
                },
            ),
            align_self="stretch",
            justify_content="flex-end",
            padding_y="1rem",
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

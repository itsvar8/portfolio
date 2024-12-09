import reflex as rx
from portfolio import ui


_renders = [
    {'img': 'renders\\00_Varotto_lamp_square.png', 'thumb': 'renders\\thumbs\\00_Varotto_lamp_square.png'},
    {'img': 'renders\\02_5_4_macropad.jpg', 'thumb': 'renders\\thumbs\\02_5_4_macropad.jpg'},
    {'img': 'renders\\05_0_MeshVariant.png', 'thumb': 'renders\\thumbs\\05_0_MeshVariant.png'},
    {'img': 'renders\\05_case.PNG', 'thumb': 'renders\\thumbs\\05_case.PNG'},
    {'img': 'renders\\Cornepad-02.png', 'thumb': 'renders\\thumbs\\Cornepad-02.png'},
    {'img': 'renders\\Cornepad-03.png', 'thumb': 'renders\\thumbs\\Cornepad-03.png'},
    {'img': 'renders\\Fan impeller blender comp.png',
     'thumb': 'renders\\thumbs\\Fan impeller blender comp.png'},
    {'img': 'renders\\OpenAirCase5mm-00-FRONT.png', 'thumb': 'renders\\thumbs\\OpenAirCase5mm-00-FRONT.png'},
    {'img': 'renders\\OpenAirCase5mm-01-BACK.png', 'thumb': 'renders\\thumbs\\OpenAirCase5mm-01-BACK.png'},
    {'img': 'renders\\Spiral cup.png', 'thumb': 'renders\\thumbs\\Spiral cup.png'},
    {'img': 'renders\\Thermostat cover.png', 'thumb': 'renders\\thumbs\\Thermostat cover.png'},
    {'img': 'renders\\zz_Crankshaft.png', 'thumb': 'renders\\thumbs\\zz_Crankshaft.png'}
]


class ModelingState(rx.State):
    renders: list[dict[str, str]] = _renders  # noqa


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
                rx.foreach(ModelingState.renders, lambda img: ui.dialog_image(img, "1", True)),
                columns="4" if not mobile_tablet else "2",
                spacing="4" if not mobile_tablet else "2",
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

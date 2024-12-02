import reflex as rx
from reflex.components.radix.themes.components.aspect_ratio import aspect_ratio


class State(rx.State):
    display: str = "none"
    image: str = ""

    @rx.event
    def show(self, image):
        self.display = "block"
        self.image = image

    @rx.event
    def hide(self):
        self.display = "none"


def pop_image(img, _aspect_ratio="auto"):
    return rx.fragment(
        rx.card(
            rx.vstack(
                rx.image(
                    State.image,
                    border_radius="1rem",
                    max_width="92vw",
                    max_height="92vh",
                ),
                rx.button("Close", size="3", on_click=State.hide),
                width="100%",
                height="100%",
                align="center",
                justify="center",
            ),
            position="fixed",
            display=State.display,
            width="100%",
            height="100%",
            top="0",
            left="0",
            right="0",
            bottom="0",
            z_index="100",
        ),
        rx.flex(
            rx.image(
                img,
                border_radius="1rem",
                max_height="100%",
            ),
            align="center",
            justify="center",
            on_click=lambda: State.show(img),
            # margin_y="-8%",
            _hover={
                "cursor": "pointer",
            },
            aspect_ratio=_aspect_ratio,
        ),
    )

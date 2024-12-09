import reflex as rx
from portfolio import ui


def content(mobile_tablet=False):
    return rx.vstack(
        rx.heading("Cornepad", size="9" if not mobile_tablet else "8"),
        #
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        #
        rx.text(
            "Cornepad is a single piece 36 keys ",
            rx.link("Corne", href="https://github.com/foostan/crkbd", is_external=True),
            " layout keyboard with a center 4*4 numpad, 2 rotary encoders and RGB. ",
            "The rotation of the three clusters of keys is -7.5 | 0 | +7.5 degrees.",
            size="5" if not mobile_tablet else "4",
        ),
        rx.image("/cornepad/cornepad-2000px.jpg", border_radius="1rem"),
        #
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        #
        rx.heading("What you need", size="7" if not mobile_tablet else "6"),
        rx.list.unordered(
            rx.list.item(
                rx.text("USB-C Raspberry Pi Pico compatible controller ", size="5" if not mobile_tablet else "4"),
                rx.link(
                    "(tested with this)",
                    href="https://52pi.com/collections/rpi-pico/products/rp2040-plus-4mb-8mb-compatible-with-raspberry-pi-pico-microcontroller-development-board?variant=42744296472728",
                    is_external=True,
                    size="5" if not mobile_tablet else "4",
                ),
            ),
            rx.list.item(rx.text("Diodes 1N4148 – 54 pcs", size="5" if not mobile_tablet else "4")),
            rx.list.item(
                rx.link(
                    "RGB Leds ",
                    href="https://www.amazon.com/BTF-LIGHTING-WS2812B-Heatsink-10mm3mm-WS2811/dp/B01DC0J0WS/ref=sr_1_16?crid=3VQEMBJ9TR7LW&keywords=WS2812B&sprefix=ws2812b%2Caps%2C214&sr=8-16&th=1",
                    is_external=True,
                    size="5" if not mobile_tablet else "4",
                ),
                rx.text("– 34 pcs", size="5" if not mobile_tablet else "4"),
            ),
            rx.list.item(rx.text("Switches – 52 pcs", size="5" if not mobile_tablet else "4")),
            rx.list.item(rx.text("Rotary encoders EC11 - 2 pcs", size="5" if not mobile_tablet else "4")),
            rx.list.item(rx.text("M3 threaded inserts – 8 pcs", size="5" if not mobile_tablet else "4")),
            rx.list.item(rx.text("M3 x 8mm button head screws – 8 pcs", size="5" if not mobile_tablet else "4")),
            rx.list.item(
                rx.text(
                    "M2 x 3mm button head screws (you can cut longer ones easily) – 2 pcs",
                    size="5" if not mobile_tablet else "4",
                )
            ),
            rx.list.item(
                rx.text("Solid core wire for rows and columns (around 20awg)", size="5" if not mobile_tablet else "4")
            ),
            rx.list.item(
                rx.text(
                    'Softer wire for the connection between the controller and rows/columns (search "ribbon cable")',
                    size="5" if not mobile_tablet else "4",
                )
            ),
            rx.list.item(rx.text("Optional Dupont connectors", size="5" if not mobile_tablet else "4")),
        ),
        rx.image("/cornepad/Cornepad-01b.png", border_radius="1rem"),
        #
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        #
        rx.heading("Wiring", size="7" if not mobile_tablet else "6"),
        rx.text("Click on the image to expand", size="5" if not mobile_tablet else "4"),
        rx.box(ui.dialog_image("cornepad/Cornepad-Wiring-RP2040.png")),
        rx.spacer(),
        rx.box(ui.dialog_image("cornepad/Cornepad-Wiring-LEDS.png")),
        #
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        #
        rx.heading("Firmware", size="7" if not mobile_tablet else "6"),
        rx.text(
            "It runs on ",
            rx.link("VIAL-QMK", href="https://get.vial.today/", is_external=True),
            ", here are the links of the source code and a pre compiled file.",
            size="5" if not mobile_tablet else "4",
        ),
        rx.hstack(
            rx.button(
                rx.icon("github"),
                "Source",
                on_click=rx.redirect(
                    "https://github.com/itsvar8/vial-qmk/tree/cornepad/keyboards/handwired/cornepad", external=True
                ),
                _hover={
                    "cursor": "pointer",
                },
            ),
            rx.button(
                rx.icon("file-down"),
                "Precompiled",
                on_click=rx.download("/cornepad/fw_cornepad.zip"),
                _hover={
                    "cursor": "pointer",
                },
            ),
            align_self="stretch",
            justify_content="flex-end",
            padding_y="1rem",
        ),
        rx.image("/cornepad/Cornepad-02b.png", border_radius="1rem"),
        #
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        #
        rx.heading("3D Files", size="7" if not mobile_tablet else "6"),
        rx.text(
            "Supports are not needed, for the stripe on the case i used the color change function",
            " of the slicer at the beginning and end of the USB-C port hole.",
            size="5" if not mobile_tablet else "4",
        ),
        rx.hstack(
            rx.button(
                rx.icon("download"),
                ".stl",
                on_click=rx.download("/cornepad/Cornepad-STL.zip"),
                _hover={
                    "cursor": "pointer",
                },
            ),
            align_self="stretch",
            justify_content="flex-end",
            padding_y="1rem",
        ),
        rx.image("/renders/Cornepad-03.png", border_radius="1rem"),
        #
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        #
        rx.heading("Have fun!", size="7" if not mobile_tablet else "6"),
        rx.text(
            "If you are in the mood for a donation it’ll help a lot!",
            size="5" if not mobile_tablet else "4",
        ),
        rx.hstack(
            rx.button(
                rx.icon("credit-card"),
                "Paypal",
                on_click=rx.redirect("https://www.paypal.com/paypalme/itsvar8", external=True),
                _hover={
                    "cursor": "pointer",
                },
            ),
            align_self="stretch",
            justify_content="flex-end",
            padding_y="1rem",
        ),
        #
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        #
        ui.bottom_buttons(),
        spacing="5" if not mobile_tablet else "3",
        margin_left="16em" if not mobile_tablet else "auto",
        padding_x="18vw" if not mobile_tablet else "6vw",
        padding_y="8vh" if not mobile_tablet else "2vh",
    )


@rx.page(title=f"Var's Portfolio | Cornepad", route="/projects/cornepad")
def cornepad() -> rx.Component:
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

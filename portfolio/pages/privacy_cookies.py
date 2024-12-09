import reflex as rx
from portfolio import ui


def content(mobile_tablet=False):
    return rx.vstack(
        rx.heading("Privacy - Cookies", size="9" if not mobile_tablet else "8"),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        rx.heading("Privacy policy", size="7" if not mobile_tablet else "6"),
        rx.text(
            "The privacy policy is simple: no personal data shared with us will be given to any third party, under any circumstances. "
            "Your data will also never be used by us for any purpose without specific permission, because i don't have them.",
            "The app engages in no ad targeting, data mining, or other activities that may compromise your privacy, ",
            "and we do not affiliate ourselves with any third parties that do so.",
            size="5" if not mobile_tablet else "4",
        ),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        rx.heading("Cookies policy", size="7" if not mobile_tablet else "6"),
        rx.heading("What Are Cookies?", size="5" if not mobile_tablet else "4"),
        rx.text(
            "Cookies are small data files that are placed on your computer or mobile device when you visit a website. "
            "Cookies are widely used by website owners to make their websites work, as well as to provide reporting information.",
            size="5" if not mobile_tablet else "4",
        ),
        rx.heading("Our Use of Cookies", size="5" if not mobile_tablet else "4"),
        rx.text(
            "This webapp does not use cookies. We have designed our website to provide information and services without the need for cookies. This means:",
            size="5" if not mobile_tablet else "4",
        ),
        rx.list.unordered(
            rx.list.item(
                rx.text(
                    "No Persistent Cookies: We do not store any persistent cookies on your device.",
                    size="5" if not mobile_tablet else "4",
                )
            ),
            rx.list.item(
                rx.text(
                    "No Session Cookies: We do not use temporary cookies that expire after a browsing session.",
                    size="5" if not mobile_tablet else "4",
                )
            ),
            rx.list.item(
                rx.text(
                    "No Third-Party Cookies: We do not allow third-party services to store cookies on your device through our website.",
                    size="5" if not mobile_tablet else "4",
                )
            ),
        ),
        rx.divider(color_scheme="cyan", margin_y="2vh"),
        ui.bottom_buttons(),
        spacing="5" if not mobile_tablet else "3",
        margin_left="16em" if not mobile_tablet else "auto",
        padding_x="18vw" if not mobile_tablet else "6vw",
        padding_y="8vh" if not mobile_tablet else "2vh",
    )


@rx.page(title=f"Var's Portfolio | Privacy - Cookies")
def privacy_cookies() -> rx.Component:
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

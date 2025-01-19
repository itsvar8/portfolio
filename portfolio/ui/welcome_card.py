import asyncio
import reflex as rx


class WelcomeCardState(rx.State):
    loading: bool = True
    _n_tasks: int = 0

    @rx.event
    def _loaded(self):
        self.loading = False

    @rx.event(background=True)
    async def loaded(self):
        async with self:
            if self._n_tasks > 0:
                return
            self._n_tasks += 1
            await asyncio.sleep(0.5)
            self._loaded()


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
            rx.skeleton(
                rx.image(src=image, width="35%", border_radius="1rem"),
                loading=rx.cond(WelcomeCardState.loading, True, False),
            ),
            rx.vstack(
                vstack_elements,
                align="end" if not inverted else "start",
                width="60%",
            ),
            direction="row" if not inverted else "row-reverse",
            wrap="wrap",
            justify="center",
        ),
        on_click=rx.redirect(redirect, is_external=external),
        _hover={
            "cursor": "pointer",
            "background-image": f"linear-gradient({rx.color('slate', 1)}, {rx.color('accent', 4)})",
            "transform": "scale(1.05)",
        },
        padding="1em",
        bg=rx.color("slate", 1),
        on_mount=WelcomeCardState.loaded,
        transform="scale(1)",
        transition="transform 0.3s ease",
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

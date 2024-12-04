import asyncio
import time
import reflex as rx


class DialogImageState(rx.State):
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


def dialog_image(img, _aspect_ratio="auto"):
    return rx.dialog.root(
        rx.skeleton(
            rx.dialog.trigger(
                rx.flex(
                    rx.image(img, border_radius="1rem", max_height="100%"),
                    align="center",
                    justify="center",
                    _hover={
                        "cursor": "pointer",
                        "transform": "scale(1.05)",
                    },
                    aspect_ratio=_aspect_ratio,
                    max_width="100%",
                    transform="scale(1)",
                    transition="transform 0.3s ease",
                ),
            ),
            loading=rx.cond(DialogImageState.loading, True, False),
        ),
        rx.dialog.content(
            rx.vstack(
                # rx.dialog.title("Welcome to Reflex!"),
                # rx.dialog.description(
                #     "This is a dialog component. You can render anything you want in here.",
                # ),
                rx.image(img, border_radius="1rem", max_width="94vw", max_height="84vh"),
                rx.dialog.close(rx.button("Close", size="2", outline="none")),
                spacing="5",
                width="100%",
                height="100%",
                align="center",
                justify="center",
            ),
            max_width="98vw",
            max_height="98vh",
            position="fixed",
            width="100%",
            height="100%",
            top="0",
            left="0",
            right="0",
            bottom="0",
            style={
                "background": "rgba(130, 200, 230, 10%)",
                "-webkit-backdrop-filter": "brightness(150%) blur(64px)",
                "backdrop-filter": "brightness(150%) blur(64px)",
            },
        ),
        on_mount=DialogImageState.loaded,
    )

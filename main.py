import flet as ft
import time


def main(page: ft.Page):
    image = ft.Image("https://picsum.photos/150/150", width=150, height=150,)

    def animate_image(self):
        print(time.time())
        switcher.content = ft.Image(
            src=f"https://picsum.photos/150/150?{time.time()}",
            width=150,
            height=150,
        )
        page.update()

    switcher = ft.AnimatedSwitcher(
        image,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=500,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    elevated_button = ft.ElevatedButton(
        "Animate Image", on_click=animate_image)
    page.add(switcher, elevated_button)


ft.app(target=main)

import flet as ft
import time


def main(page: ft.Page):
    container = ft.Container(
        width=150,
        height=150,
        bgcolor="red",
        border_radius=13,
        animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT)
    )

    def animate_container(self):
        container.width = 100 if container.width == 150 else 150
        container.height = 50 if container.height == 150 else 150
        container.bgcolor = "blue" if container.bgcolor == "red" else "red"
        container.border_radius = 30 if container.border_radius == 13 else 13
        container.update()
    elevatedBuutton = ft.ElevatedButton(
        "Animate Container!",
        on_click=animate_container
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(container, elevatedBuutton)


ft.app(target=main)

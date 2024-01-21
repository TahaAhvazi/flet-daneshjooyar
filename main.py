import flet as ft
from time import sleep


def main(page: ft.Page):
    page.title = "ProgressBar example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30.0
    page.update()

    pb = ft.ProgressBar(width=500, color="red", bgcolor="green")
    pr = ft.ProgressRing(width=20, height=20, stroke_width=2)
    text = ft.Text("Doing something!")
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(pb, text, pr)

    for i in range(0, 101):
        pb.value = i * 0.01
        pr.value = i * 0.01
        text.value = f"{i} %"
        sleep(0.1)
        page.update()


ft.app(target=main)

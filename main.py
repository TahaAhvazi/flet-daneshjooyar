import flet as ft


def main(page: ft.Page):
    page.title = "Image Slider!"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.update()

    img = ft.Image(
        src=f"https://picsum.photos/200/200",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    images = ft.Row(expand=1, wrap=False, scroll="always")
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(img, images)

    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(13.0)
            )
        )
    page.update()


ft.app(target=main)

import flet as ft


def main(page: ft.Page):
    myGridView = ft.GridView(expand=True, max_extent=120, aspect_ratio=0.5)
    page.add(myGridView)

    for i in range(5000):
        myGridView.controls.append(
            ft.Container(
                ft.Text(f"Item{i+1}", color=ft.colors.BLACK),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_300,
                border_radius=ft.border_radius.all(8)
            )

        )

    page.update()


ft.app(target=main)

import flet as ft


def main(page: ft.Page):
    container1 = ft.Container(
        width=50, height=50, bgcolor="red", animate_position=1000, top=0)
    container2 = ft.Container(
        width=50, height=50, bgcolor="blue", animate_position=500, top=60)
    container3 = ft.Container(
        width=50, height=50, bgcolor="green", animate_position=1000, top=120)

    def animateContainers(self):
        container1.top = 20
        container1.left = 30
        container2.top = 100
        container2.left = 50
        container3.top = 100
        container3.left = 120
        page.update()
    elevatedButton = ft.ElevatedButton("Animate!", on_click=animateContainers)
    myStack = ft.Stack(
        [container1, container2, container3,],
        height=250,
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(myStack, elevatedButton)


ft.app(target=main)

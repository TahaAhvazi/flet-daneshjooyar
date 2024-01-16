import flet as ft
import time


def main(page: ft.Page):
    page.title = "Daneshjooyar conter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def button_clicked(input):
        greetings.controls.append(
            ft.Text(f"Hello {first_name.value} {last_name.value}"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    first_name = ft.TextField(label="First Name", autofocus=True)
    last_name = ft.TextField(label="Last Name")
    submit_button = ft.ElevatedButton("Say Hello", on_click=button_clicked)
    greetings = ft.Column()

    page.add(
        first_name,
        last_name,
        submit_button,
        greetings,
    )


ft.app(target=main)

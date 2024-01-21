import flet as ft


class GreeterController(ft.UserControl):
    def build(Self):
        return ft.Text("Welcome!")


class LoginApproachController(ft.UserControl):
    def build(self):
        return ft.Column([
            ft.TextField(label="Username", width=300),
            ft.ElevatedButton("Login"),
        ]
        )


class CounterController(ft.UserControl):
    def add_number(self, event):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def decrement_number(self, event):
        self.counter -= 2
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0
        self.text = ft.Text(str(self.counter))
        return ft.Row([ft.ElevatedButton("REMOVE", on_click=self.decrement_number), self.text, ft.ElevatedButton("ADD", on_click=self.add_number)], vertical_alignment=ft.MainAxisAlignment.CENTER)


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        GreeterController(),
        LoginApproachController(),
        CounterController(),
    )


ft.app(target=main)

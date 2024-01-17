import flet as ft


def main(page: ft.Page):

    def checkbox_change(e):
        mytext.value = (
            f"You have done Learn flet : {myCheckBox.value}"
        )
        page.update()

    mytext = ft.Text()
    myCheckBox = ft.Checkbox(
        label="Learn flet with daneshjooyar", value=False, on_change=checkbox_change)
    page.add(mytext, myCheckBox)


ft.app(target=main)

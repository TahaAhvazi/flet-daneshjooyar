import flet as ft


def main(page: ft.Page):
    # PubSub
    page.title = "My X Chat"

    def on_message(message):
        messages.controls.append(ft.Text(message))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_message(event):
        page.pubsub.send_all(f"{user.value}: {message.value}")
        message.value = ""
        page.update()

    messages = ft.Column()
    user = ft.TextField(hint_text="Your name")
    message = ft.TextField(hint_text="Your message...", expand=True)
    sendButton = ft.ElevatedButton("SEND", on_click=send_message)

    page.add(messages, ft.Row([user, message, sendButton]))


ft.app(target=main, view=ft.AppView.WEB_BROWSER)

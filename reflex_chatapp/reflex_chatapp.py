import reflex as rx
from reflex_chatapp import style
from reflex_chatapp.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, style=style.question_style),
        rx.box(answer, style=style.answer_style),
        margin_y="1rem",
    )


def chat() -> rx.Component:
    return rx.box(
        # we must use rx foreach because state values aren't known at compile time
        rx.foreach(State.chat_history, lambda messages: qa(messages[0], messages[1]))
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Type your question here...",
            style=style.input_style,
            on_blur=State.set_question,
        ),
        rx.button("Ask", style=style.button_style, on_click=State.answer),
    )


def index() -> rx.Component:
    return rx.container(chat(), action_bar())


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()

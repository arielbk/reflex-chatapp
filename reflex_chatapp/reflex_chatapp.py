import reflex as rx
from reflex import el
from reflex_chatapp.state import State


global_style = {
    ".scrollbar-w-2::-webkit-scrollbar": {"width": "0.25rem", "height": "0.25rem"},
    ".scrollbar-track-blue-lighter::-webkit-scrollbar-track": {
        "--bg-opacity": "1",
        "background-color": "#f7fafc",
        "background-color": "rgba(247, 250, 252, var(--bg-opacity))",
    },
    ".scrollbar-thumb-blue::-webkit-scrollbar-thumb": {
        "--bg-opacity": "1",
        "background-color": "#edf2f7",
        "background-color": "rgba(237, 242, 247, var(--bg-opacity))",
    },
    ".scrollbar-thumb-rounded::-webkit-scrollbar-thumb": {"border-radius": "0.25rem"},
}


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        el.div(
            el.div(
                question,
                class_name="max-w-24 my-2 px-4 py-2 rounded-lg inline-block rounded-br-none bg-blue-500 text-white",
            ),
            class_name="flex justify-end",
        ),
        el.div(
            el.div(
                answer,
                class_name="max-w-lg my-2 px-6 py-4 rounded-lg inline-block rounded-bl-none bg-gray-200 text-gray-600",
            ),
            class_name="flex justify-start",
        ),
    )


def chat() -> rx.Component:
    return rx.box(
        # we must use rx foreach because state values aren't known at compile time
        rx.foreach(State.chat_history, lambda messages: qa(messages[0], messages[1])),
        class_name="flex flex-col space-y-2 p-3 pb-24 overflow-y-auto scrollbar-thumb-blue scrollbar-thumb-rounded scrollbar-track-blue-lighter scrollbar-w-2 scrolling-touch",
    )


def action_bar() -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Type your question here...",
            on_change=State.set_question,
            value=State.question,
            class_name="w-full focus:outline-none focus:placeholder-gray-200 text-gray-600 placeholder-gray-500 bg-gray-200 rounded-md px-4 py-3",
        ),
        el.button(
            "Send",
            class_name="inline-flex items-center justify-center rounded-lg px-4 transition duration-500 ease-in-out text-white bg-blue-500 hover:bg-blue-400 focus:outline-none",
            type="submit",
        ),
        class_name="flex flex-row gap-2 fixed bottom-0 left-0 w-full bg-white border-t-2 border-gray-200 px-4 py-4",
        on_submit=State.answer,
    )


def index() -> rx.Component:
    return el.div(
        chat(),
        action_bar(),
        class_name="p:2 sm:p-6 justify-between mx-0 w-full flex flex-col h-screen",
    )


# Add state and page to the app.
app = rx.App(state=State, style=global_style)
app.add_page(index)
app.compile()

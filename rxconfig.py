import reflex as rx


class ReflexchatappConfig(rx.Config):
    pass


config = ReflexchatappConfig(
    app_name="reflex_chatapp",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    tailwind={},
)

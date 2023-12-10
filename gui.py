from textual.app import App
from textual.widgets import Button, Header, Input, Log
from rich.style import Style
from textual.message import Message
from rich.box import DOUBLE


class MyApp(App):
  def compose(self):
    yield Header()
    yield Input(
        placeholder="Enter a number...",
        validators=[],
    )
    yield Log()

  def on_input_changed(self):
    log = self.query_one(Log)
    log.write_line("test")

MyApp().run()
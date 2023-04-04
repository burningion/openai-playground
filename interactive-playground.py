from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Input, Footer, Static, TextLog

class GPTPrompt(Static):
    """A widget to prompt for ChatGPT"""

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter your prompt")
        yield Button("Enter", id="enter", variant="success")

class GPTApp(App):
    """A Textual app to use GPT-4 from the command line"""
    CSS_PATH="interactive.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets"""
        yield Header()
        yield Footer()
        yield Container(GPTPrompt())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    
if __name__ == "__main__":
    app = GPTApp()
    app.run()
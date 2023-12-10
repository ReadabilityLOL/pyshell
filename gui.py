from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.prompt import Prompt

console = Console()

# Function to display terminal output
def display_output(output):
    output_panel = Panel(output, title="Output")
    layout.update(output_panel)

# Initial output for demonstration purposes
initial_output = "Welcome to the terminal GUI!"

# Create panels for input and initial output
input_panel = Panel.fit(Prompt("Enter command: "), title="Input")
output_panel = Panel(initial_output, title="Output")

# Create a layout
layout = Layout()
layout.split(
    Layout(name="header", size=1),
    Layout(name="main", ratio=2),
    Layout(name="footer", size=1),
)
layout["header"].update(Panel("Top Right Panel", title="Top Right"))

# Add panels to the layout
layout["main"].split_row(input_panel, output_panel)
layout["footer"].update(Panel("Bottom Bar"))

# Render the layout
console.print(layout)

# Simulate updating the output when a command is entered
new_output = "This is the new terminal output!"
display_output(new_output)

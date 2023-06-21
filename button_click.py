from reactpy import component, html, run

@component
def printButton(text, state):
    def handle_event(event):
        print(text, state)
    
    return html.button({"on_click": handle_event}, text)

@component
def App():
    return html.div(
        printButton("Play", "Playing"),
        printButton("Pause", "Paused"),
    )

run(App)
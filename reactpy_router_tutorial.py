from reactpy import component, html, run
from reactpy_router import route, simple, link, use_location

@component
def root():
    return simple.router(
        route("/", html.h1("Home")),
        route("/about", html.h1("About"))
    )

run(root)
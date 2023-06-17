from reactpy import component, html, run


@component
def App():
    return html.section(
        html.h1(
        {
            "style": {
                "margin_top": "0px",
                "color": "red",
            }
        },
        "Hello, world!"
        )
    )

run(App)




























# (
#             {
#                 "style": {
#                     "width": "50%",
#                     "margin_left": "25%",
#                 },
#             },
#             html.h1(
#                 {
#                     "style": {
#                         "margin_top": "0px",
#                     },
#                 },
#                 "My Todo List",
#             ),
#             html.ul(
#                 html.li("Build a cool new app"),
#                 html.li("Share it with the world!"),
#             ),
#         )
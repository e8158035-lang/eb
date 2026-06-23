import flet as ft
import math

def main(page: ft.Page):
    page.title = "آلة حاسبة احترافية"
    page.theme_mode = "dark"
    page.window_width = 350
    page.window_height = 600

    expression = ""
    display = ft.Text(value="0", size=30)

    def update(value):
        display.value = value
        page.update()

    def normalize(expr: str) -> str:
        while expr and expr[-1] in "+-*/.":
            expr = expr[:-1]
        return expr

    def safe_eval(expr: str) -> float:
        expr = normalize(expr)
        if not expr:
            return 0.0
        return eval(expr)

    def add_constant(value: str):
        nonlocal expression
        if expression and expression[-1] not in "+-*/":
            expression += "*"
        expression += value
        update(expression)

    def click(e):
        nonlocal expression
        value = e.control.data

        try:
            if value == "C":
                expression = ""
                update("0")

            elif value == "=":
                expression = str(safe_eval(expression))
                update(expression)

            elif value == "√":
                expression = str(math.sqrt(safe_eval(expression)))
                update(expression)

            elif value == "x²":
                expression = str(safe_eval(expression) ** 2)
                update(expression)

            elif value == "sin":
                expression = str(math.sin(math.radians(safe_eval(expression))))
                update(expression)

            elif value == "cos":
                expression = str(math.cos(math.radians(safe_eval(expression))))
                update(expression)

            elif value == "tan":
                expression = str(math.tan(math.radians(safe_eval(expression))))
                update(expression)

            elif value == "log":
                expression = str(math.log10(safe_eval(expression)))
                update(expression)

            elif value == "ln":
                expression = str(math.log(safe_eval(expression)))
                update(expression)

            elif value == "π":
                add_constant(str(math.pi))

            elif value == "e":
                add_constant(str(math.e))

            else:
                expression += value
                update(expression)

        except Exception:
            update("خطأ")
            expression = ""

    def btn(text):
        return ft.ElevatedButton(
            content=ft.Text(text),
            data=text,
            width=70,
            height=60,
            on_click=click
        )

    layout = [
        ["C", "√", "x²", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "=", ""],
        ["sin", "cos", "tan", ""],
        ["log", "ln", "π", "e"]
    ]

    rows = []
    for row in layout:
        r = []
        for item in row:
            if item != "":
                r.append(btn(item))
        rows.append(ft.Row(r, alignment=ft.MainAxisAlignment.CENTER))

    page.add(
        ft.Column(
            [
                ft.Container(
                    display,
                    alignment=ft.Alignment.CENTER_RIGHT,
                    padding=20
                ),
                *rows
            ]
        )
    )

ft.app(target=main)

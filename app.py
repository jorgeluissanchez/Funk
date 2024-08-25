import flet as ft
import sympy as sp
from sympy import *

f = None
n = None
a = None
x = sp.Symbol('x')
h= None
xi= None

class LineChart(ft.LineChart):
    def __init__(self, width=310, height=150, datos_1=[], datos_2=[]):
        super().__init__()
        
        all_points = datos_1 + datos_2
        self.min_x = min(point[0] for point in all_points)
        self.max_x = max(point[0] for point in all_points)
        self.min_y = min(point[1] for point in all_points)
        self.max_y = max(point[1] for point in all_points)
        
        self.width=width
        self.height=height
        
        self.data_series = [
            ft.LineChartData(
                data_points=[ft.LineChartDataPoint(x, y) for x, y in datos_1],
                stroke_width=4,
                color="#DAD4BA",
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[ft.LineChartDataPoint(x, y) for x, y in datos_2],
                color="#B4D0C0",
                below_line_bgcolor=ft.colors.with_opacity(0, ft.colors.PINK),
                stroke_width=4,
                curved=True,
                stroke_cap_round=True,
            ),
        ]
   
class Card(ft.Container):
    def __init__(self, titulo, descripcion, error=None, colorError="#DAD4BA"):
        super().__init__()
        self.error_content = []
        if error:
            self.error_content = [
                ft.Container(
                    content=ft.Text(
                        value=error,
                        size=13,
                        font_family="robotoMedium",
                        color=ft.colors.BLACK
                    ),
                    width=50,
                    height=50,
                    border_radius=50,
                    bgcolor=colorError,
                    alignment=ft.alignment.center,
                ),
            ]
        self.expand = True
        self.content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column([
                        *self.error_content,
                        ft.Text(
                            value=titulo,
                            size=13,
                            width=50,
                            text_align=ft.TextAlign.CENTER,
                            font_family="robotoMedium"
                        ),
                        ft.Text(
                            value=descripcion,
                            size=13,
                            width=50,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.colors.BLACK,
                            font_family="robotoLight",
                        ),
                    ]),
                    padding=10,
                    bgcolor="#FDFDFD",
                    border_radius=10,
                    expand=True,
                    alignment=ft.alignment.center,
                )
            ],
            expand=True,
        )
 
class InfoCard(ft.Container):
    def __init__(self, title, description, event, height=145):
        super().__init__()
        self.content = ft.Column([
            ft.Text(
                value=title,
                size=20,
                color=ft.colors.BLACK,
                font_family="robotoMedium",
            ),
            ft.Text(
                value=description,
                size=13,
                color=ft.colors.BLACK,
                font_family="robotoLight",
            ),
        ])
        self.padding = 15
        self.bgcolor = '#FDFDFD'
        self.border_radius = 10
        self.elevation = 3
        self.on_click = event
        
class Button(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1, bgcolor=ft.colors.WHITE, color=ft.colors.BLACK):
        super().__init__()
        
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text
        self.bgcolor = bgcolor
        self.color = color

class Input(ft.Container):
    def __init__(self, variable, prev, next):
        super().__init__()
        self.prev= prev
        self.next = next
        self.variable = variable
        self.result = []
        self.resDisplay = ft.Text(value="0", size=15, font_family="robotoMedium", color=ft.colors.BLACK)
        self.buttons = [
            ["1", "2", "3", "+"], ["4", "5", "6", "-"], 
            ["7", "8", "9", "*"], ["0", "(", ")", "/"], 
            ["sen", "cos", "x", "del"]
        ] if variable == "f" else [
            ["1", "2", "3"], ["4", "5", "6"], 
            ["7", "8", "9"], ["0", ".", "del"]
        ]
        self.width = 310
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[
                    ft.Container(
                    content=self.resDisplay,
                    border_radius=10,
                    padding=10,
                    expand=True,
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                )]),
                *[ft.Row(controls=[Button(text=button, button_clicked=self.button_clicked) for button in row]) for row in self.buttons],
                ft.Row(controls=[
                    Button(text="Anterior", button_clicked=self.prev),
                    Button(text="Siguiente", button_clicked=self.next, bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)
                ]),
            ]
        )

    def button_clicked(self, e):
        data = e.control.data
        if data == "del":
            self.result.pop()
        else:
            self.result.append(data)
        self.resDisplay.value = "".join(self.result)
        
        global n,a,x,f,h,xi
        
        if self.variable == "n":
            n = int("".join(self.result))
        elif self.variable == "a":
            a = int("".join(self.result))
        elif self.variable == "x":
            x = int("".join(self.result))
        elif self.variable == "h":
            h = int("".join(self.result))
        elif self.variable == "xi":
            xi = int("".join(self.result))
        elif self.variable == "f":
            try:
                f = sp.sympify("".join(self.result))
            except:
                f = None
            
        self.update()

def main(page: ft.Page):
    #page.window.title_bar_hidden = True
    #page.window.frameless = True
    page.fonts = {
        "robotoRegular": "./fonts/Roboto-Regular.ttf",
        "robotoBold": "./fonts/Roboto-Bold.ttf",
        "robotoLight": "./fonts/Roboto-Light.ttf",
        "robotoMedium": "./fonts/Roboto-Medium.ttf",
    }
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    page.window.left = 20
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.window.top = 20
    page.window.height = 812
    page.window.width = 375
    page.on_resize =None
    datos_1 = [(1, 1), (3, 1.5), (5, 1.4), (7, 3.4), (10, 2), (12, 2.2), (13, 1.8)]
    datos_2 = [(1, 1), (3, 2.8), (7, 1.2), (10, 2.8), (12, 2.6), (13, 3.9)]
    
    # INICIO DE LA APLICACIÓN
    TailorCard = InfoCard("Series de Taylor", "Son representaciones de una función como una suma infinita de términos calculados a partir de las derivadas de la función en un punto específico.", lambda _: page.go("/series-taylor/insert-f"))
    DerivateCard = InfoCard("Derivación Numérica", "Método utilizado para aproximar la derivada de una función en un punto específico cuando no se dispone de una expresión analítica de la derivada.", lambda _: page.go("/derivada-numerica/insert-f"))
    # INPTUS DE LA APLICACIÓN DE SERIES DE TAYLOR
    FunctionTailor = Input("f", prev=lambda _: page.go("/"), next=lambda _: page.go("/series-taylor/insert-n"))
    NumberNTailor = Input("n", prev=lambda _: page.go("/series-taylor/insert-f"), next=lambda _: page.go("/series-taylor/insert-a"))
    NumberATailor = Input("a", prev=lambda _: page.go("/series-taylor/insert-n"), next=lambda _: page.go("/series-taylor"))    
    # RESULTADOS DE LA APLICACIÓN DE SERIES DE TAYLOR
    LineChartTailor = LineChart(datos_1=datos_1, datos_2=datos_2)
    TheoryCardTailor = Card("Teórico", "125k")
    ExperimentalCardTailor = Card("Exp.", "125k")
    ErrorCardTailor = Card("Error", "125k", "0.5%")
    # INPTUS DE LA APLICACIÓN DE DERIVADAS
    FunctionDerivate = Input("f", prev=lambda _: page.go("/"), next=lambda _: page.go("/derivada-numerica/insert-h"))
    NumberHDerivate = Input("h", prev=lambda _: page.go("/derivada-numerica/insert-f"), next=lambda _: page.go("/derivada-numerica/insert-xi"))
    NumberXIDerivate = Input("xi", prev=lambda _: page.go("/derivada-numerica/insert-h"), next=lambda _: page.go("/derivada-numerica"))
    # RESULTADOS DE LA APLICACIÓN DE DERIVADAS
    TheoryCardDerivate = Card("Teórico", "125k")
    CenterCardDerivate = Card("Centro", "125k")
    LeftCardDerivate = Card("Izq.", "125k")
    RightCardDerivate = Card("Derecha", "125k")
    ErrorLeftCardDerivate = Card("Izq.", "125k", "0.5%")
    ErrorRightCardDerivate = Card("Derecha", "125k", "0.5%", "#B4D0C0")
    ErrorCenterCardDerivate = Card("Centro", "125k", "0.5%", "#E7DB81")
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Text(value="Temas", size=35, font_family="robotoBold"),
                    ft.Column(
                        controls=[
                            TailorCard,                 
                            DerivateCard,
                        ],
                        width=310
                    ),        
                ],
                bgcolor='#F6F6EF',
                vertical_alignment= ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                padding=25,
            )
        )
        
        if page.route == "/series-taylor/insert-f":
            page.views.append(
                ft.View(
                    "/series-taylor/insert-f",
                    [   
                        ft.Text(value="Ingresar f(x)", size=35, font_family="robotoMedium"),
                        FunctionTailor
                    ], 
                    bgcolor='#F6F6EF',
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    padding=25
                )
            )
        if page.route == "/series-taylor/insert-n":
            page.views.append(
                ft.View(
                    "/series-taylor/insert-n",
                    [   
                        ft.Text(value="Ingresar n", size=35, font_family="robotoMedium"),
                        NumberNTailor
                    ], 
                    bgcolor='#F6F6EF',
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    padding=25
                )
            )
        if page.route == "/series-taylor/insert-a":
            page.views.append(
                ft.View(
                    "/series-taylor/insert-a",
                    [   
                        ft.Text(value="Ingresar a", size=35, font_family="robotoMedium"),
                        NumberATailor
                    ], 
                    bgcolor='#F6F6EF',
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    padding=25
                )
            ) 
        if page.route == "/series-taylor":
            page.views.append(
                ft.View(
                    "/series-taylor",
                    [   
                        ft.Text(value="Series de Taylor", size=35, font_family="robotoMedium"),
                        LineChartTailor,
                        ft.Text(value="Información", size=25, font_family="robotoMedium"),
                        ft.Column(
                            controls=[
                                ft.Row([
                                        TheoryCardTailor,
                                        ExperimentalCardTailor
                                    ]),
                                ft.Row([ErrorCardTailor]),
                                ft.Row([
                                        Button(text="Volver", button_clicked=lambda _: page.go("/series-taylor/insert-f"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)
                                    ]),
                                ],
                            width=310
                        ),
                    ], 
                            
                    bgcolor='#F6F6EF',
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    padding=25
                )
            )
        
        if page.route == "/derivada-numerica/insert-f":
            page.views.append(
                ft.View(
                    "/derivada-numerica/insert-f",
                    [   
                        ft.Text(value="Ingresar f(x)", size=35, font_family="robotoMedium"),
                        FunctionDerivate
                    ], 
                    bgcolor='#F6F6EF',
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    padding=25
                )
            )
        if page.route == "/derivada-numerica/insert-h":
            page.views.append(
                ft.View(
                    "/derivada-numerica/insert-h",
                    [   
                        ft.Text(value="Ingresar h", size=35, font_family="robotoMedium"),
                        NumberHDerivate
                    ], 
                    bgcolor='#F6F6EF',
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    padding=25
                )
            )
        if page.route == "/derivada-numerica/insert-xi":
            page.views.append(
                ft.View(
                    "/derivada-numerica/insert-xi",
                    [   
                        ft.Text(value="Ingresar xi", size=35, font_family="robotoMedium"),
                        NumberXIDerivate
                    ], 
                    bgcolor='#F6F6EF',
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    padding=25
                )
            ) 
        if page.route == "/derivada-numerica":
            page.views.append(
                ft.View(
                    "/derivada-numerica",
                    [   
                        ft.Text(value="Derivadas", size=35, font_family="robotoMedium"),
                        ft.Column(
                            controls=[
                                ft.Row([
                                        TheoryCardDerivate,
                                        CenterCardDerivate
                                    ]),
                                ft.Row([
                                        LeftCardDerivate,
                                        RightCardDerivate
                                        ]),
                            ],
                            width=310
                        ),
                        ft.Text(value="Errores", size=25, font_family="robotoMedium"),
                        ft.Column(
                            controls=[
                            ft.Row([
                                        ErrorLeftCardDerivate,
                                        ErrorRightCardDerivate
                                    ]),
                                ft.Row([
                                        ErrorCenterCardDerivate                            ]),
                                ft.Row(
                                    controls=[
                                        Button(text="Volver", button_clicked=lambda _: page.go("/derivada-numerica/insert-f"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)
                                    ],
                                ),
                            ],
                            width=310
                        ),
                    ], 
                    bgcolor='#F6F6EF',
                    padding=25,
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)


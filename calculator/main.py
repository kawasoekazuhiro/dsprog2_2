import flet as ft  # Fletライブラリをインポートします
import math  # 数学関数を使うためにmathライブラリをインポートします

def main(page: ft.Page):
    page.title = "科学計算モード付き電卓"  # ウィンドウのタイトルを設定します

    screen = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=300)  # 計算結果や入力を表示するフィールドを作成します

    # ボタンがクリックされたときの処理を定義します
    def button_click(e):
        if e.control.data == "=":
            try:
                expression = screen.value.replace("×", "*").replace("÷", "/")
                # 二乗の計算を実装
                expression = expression.replace("^2", "**2")
                screen.value = str(eval(expression))
            except Exception:
                screen.value = "エラー"
        elif e.control.data == "C":
            screen.value = ""
        else:
            screen.value += str(e.control.data)
        
        page.update()

    # 科学的な計算ボタンのクリック処理を定義します
    def scientific_button_click(e):
        try:
            value = float(screen.value)
            result = None
            if e.control.data == "π":
                result = math.pi
            elif e.control.data == "√":
                result = math.sqrt(value)
            elif e.control.data == "!":
                result = math.factorial(int(value))
            elif e.control.data == "exp":
                result = math.exp(value)
            elif e.control.data == "log":
                result = math.log(value)
                
            screen.value = str(result)
        except Exception:
            screen.value = "エラー"

        page.update()

    # 通常の電卓ボタンのリストを作成します
    buttons = [
        ("7", "7"), ("8", "8"), ("9", "9"), ("÷", "/"),
        ("4", "4"), ("5", "5"), ("6", "6"), ("×", "*"),
        ("1", "1"), ("2", "2"), ("3", "3"), ("-", "-"),
        ("0", "0"), (".", "."), ("=", "="), ("+", "+"),
        ("C", "C")  # Clearボタン
    ]

    # 科学的な計算に必要な追加ボタン
    scientific_buttons = [
        ("π", "π"), ("√", "√"), ("!", "!"), ("^2", "^2"), ("exp", "exp"), ("log", "log")
    ]

    # 各ボタンをFletのElevatedButtonとして作成し、クリックイベントを設定します
    button_controls = [ft.ElevatedButton(text, on_click=button_click, data=data, width=60) for text, data in buttons]
    scientific_button_controls = [ft.ElevatedButton(text, on_click=scientific_button_click, data=data, width=60) for text, data in scientific_buttons]
    
    # グリッド（行/列）レイアウトでボタンを配置します
    grid = ft.Column(controls=[
        screen,
        ft.Row(button_controls[:4], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(button_controls[4:8], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(button_controls[8:12], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(button_controls[12:16], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(button_controls[16:], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(scientific_button_controls[:3], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(scientific_button_controls[3:], alignment=ft.MainAxisAlignment.CENTER)
    ])
    
    page.add(grid)  # 作成したグリッドをページに追加します

ft.app(target=main)  # Fletアプリケーションを実行します
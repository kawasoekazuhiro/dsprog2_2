import flet as ft  # Fletライブラリをインポートします

def main(page: ft.Page):
    page.title = "電卓アプリケーション"  # ウィンドウのタイトルを設定します

    screen = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=300)  # 計算結果や入力を表示するフィールドを作成します

    # ボタンがクリックされたときの処理を定義します
    def button_click(e):
        if e.control.data == "=":
            try:
                screen.value = str(eval(screen.value.replace("×", "*").replace("÷", "/")))
            except Exception:
                screen.value = "エラー"
        elif e.control.data == "C":
            screen.value = ""
        else:
            screen.value += str(e.control.data)
        
        page.update()

    # 通常の電卓ボタンのリストを作成します
    buttons = [
        ("7", "7"), ("8", "8"), ("9", "9"), ("÷", "/"),
        ("4", "4"), ("5", "5"), ("6", "6"), ("×", "*"),
        ("1", "1"), ("2", "2"), ("3", "3"), ("-", "-"),
        ("0", "0"), (".", "."), ("=", "="), ("+", "+"),
        ("C", "C")  # Clearボタン
    ]

    # 各ボタンをFletのElevatedButtonとして作成し、クリックイベントを設定します
    button_controls = [ft.ElevatedButton(text, on_click=button_click, data=data, width=60) for text, data in buttons]
    
    # グリッド（行/列）レイアウトでボタンを配置します
    grid = ft.Column(controls=[
        screen,
        ft.Row(button_controls[:4], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(button_controls[4:8], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(button_controls[8:12], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(button_controls[12:16], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(button_controls[16:], alignment=ft.MainAxisAlignment.CENTER),
    ])
    
    page.add(grid)  # 作成したグリッドをページに追加します

ft.app(target=main)  # Fletアプリケーションを実行します
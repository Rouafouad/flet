import flet as ft

def main(page: ft.Page):
    page.title = "Roua Mobile App.test"
    page.window.width = 390
    page.window.height = 750
    page.bgcolor = ft.Colors.BLACK
    page.window.top = 30
    page.window.left = 950
    page.window.resizable = False
    page.window.title_bar_hidden = False
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    #page.scroll = "auto"
    
    # AppBar start
    page.appbar = ft.AppBar(
        bgcolor=ft.Colors.RED,
        title=ft.Text(
            "شركة الأستكشافات النفطية",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLACK 
        ),
        center_title=True,
        leading=ft.Icon(ft.Icons.HOME),
        leading_width=40,
        actions=[
            ft.IconButton(ft.Icons.NOTIFICATIONS),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="الملف الشخصي"),
                    ft.PopupMenuItem(text="الإعدادات"),
                    ft.PopupMenuItem(text="من نحن"),
                    ft.PopupMenuItem(), 
                    ft.PopupMenuItem(text="تسجيل الخروج"),
                ]
            ),
        ]
    )

    # ---- Centered Login UI ----
    logo = ft.Image(src="images/oec_ar.png", width=120)
    title = ft.Text("تسجيل الدخول", color=ft.Colors.GREY, size=25, weight=ft.FontWeight.BOLD)

    btn1 = ft.TextField(label="Email(الأيميل)", prefix_icon=ft.Icons.EMAIL, width=280, color="white",   label_style=ft.TextStyle(color=ft.Colors.GREY),)
    btn2 = ft.TextField(
        label="Password (كلمة المرور)",
        prefix_icon=ft.Icons.PASSWORD,
        password=True,
        color="white",
        can_reveal_password=True,
        width=280,
        label_style=ft.TextStyle(color=ft.Colors.GREY),
    )

    def show(e):
        v1 = btn1.value  
        v2 = btn2.value  

        if v1 == "roua" and v2 == "123456":
            dlg = ft.AlertDialog(title=ft.Text("اهلا وسهلا بك في التطبيق", size=18, color="green"))
            page.overlay.append(dlg)
            dlg.open = True
            page.update()
        else:
            dlg = ft.AlertDialog(title=ft.Text("اسم المستخدم او كلمة المرور خاطئة لطفاً حاول مرة اخرى", size=18, color="red"))

            page.overlay.append(dlg)
            dlg.open = True
            page.update()

    btn_login = ft.ElevatedButton("الدخول للحساب", width=280, on_click=show)

    page.add(
        ft.Container(
            expand=True,
            content=ft.Column(
                [logo, title, btn1, btn2, btn_login],
                alignment=ft.MainAxisAlignment.CENTER,              # vertical center
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # horizontal center
                spacing=12,
            ),
        )
    )
    
        # AppBar start
        
    page.navigation_bar = ft.CupertinoNavigationBar(
            bgcolor=ft.Colors.RED,
            inactive_color = ft.Colors.BLACK,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.CALL, label=("اتصال")),
                ft.NavigationBarDestination(icon=ft.Icons.CAMERA, label ="كاميرا"),
                ft.NavigationBarDestination(icon=ft.Icons.CONTACT_PHONE, label = "جهات الأتصال")
            ]
            
        )

    page.update()

# ✅ Choose ONE run mode:

# 1) Desktop
ft.app(target=main)

# 2) Web (on port 3331)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=3331)

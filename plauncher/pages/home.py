import customtkinter as ctk


class HomePage(ctk.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)
        
        accounts_manager = app.accounts_manager
        FONT_UI = "Inter 18pt"
        FONT_MONO = "JetBrains Mono"

        font_section = ctk.CTkFont(FONT_UI, 13, "bold")
        font_body = ctk.CTkFont(FONT_UI, 14)
        font_small = ctk.CTkFont(FONT_UI, 12)

        header = ctk.CTkFrame(self, fg_color="transparent", height=55)
        header.place(relx=0.04, rely=0.045, relwidth=0.92)

        title = ctk.CTkLabel(
            header,
            text="Добро пожаловать",
            font=ctk.CTkFont(FONT_UI, 26, "bold"),
            anchor="w",
            height=32,
        )
        title.place(relx=0, rely=0, relwidth=1)

        subtitle = ctk.CTkLabel(
            header,
            text="Готовы к следующему запуску?",
            font=ctk.CTkFont(FONT_UI, 14),
            anchor="w",
            height=22,
        )
        subtitle.place(relx=0, rely=0.58, relwidth=1)

        launch_card = ctk.CTkFrame(self, corner_radius=14)
        launch_card.place(
            relx=0.04,
            rely=0.18,
            relwidth=0.92,
            relheight=0.43,
        )

        username_label = ctk.CTkLabel(
            launch_card,
            text="Аккаунт",
            font=font_section,
            anchor="w",
            height=20,
        )
        username_label.place(relx=0.045, rely=0.10, relwidth=0.42)
        
        usernames = accounts_manager.get_usernames()
        self.username_combobox = ctk.CTkComboBox(
            launch_card,
            values=usernames,
            font=font_body,
            height=38,
        )
        self.username_combobox.place(
            relx=0.045,
            rely=0.19,
            relwidth=0.42,
        )
        self.username_combobox.set(usernames[0] if usernames else "")

        instance_label = ctk.CTkLabel(
            launch_card,
            text="Экземпляр",
            font=font_section,
            anchor="w",
            height=20,
        )
        instance_label.place(relx=0.515, rely=0.10, relwidth=0.40)

        instance_menu = ctk.CTkComboBox(
            launch_card,
            values=[
                "PLauncher Survival",
                "Vanilla 1.21.8",
                "Fabric Performance",
            ],
            font=font_body,
            height=38,
        )
        instance_menu.set("PLauncher Survival")
        instance_menu.place(
            relx=0.515,
            rely=0.19,
            relwidth=0.44,
        )

        play_button = ctk.CTkButton(
            launch_card,
            text="▶   ИГРАТЬ",
            font=ctk.CTkFont(FONT_UI, 15, "bold"),
            height=44,
            corner_radius=10,
        )
        play_button.place(relx=0.045, rely=0.45, relwidth=0.91)

        launch_progress = ctk.CTkProgressBar(launch_card, height=8)
        launch_progress.set(0)
        launch_progress.place(relx=0.045, rely=0.7, relwidth=0.91)

        launch_status = ctk.CTkLabel(
            launch_card,
            text="Готово к запуску",
            font=font_small,
            anchor="center",
            height=18,
        )
        launch_status.place(relx=0.045, rely=0.76, relwidth=0.91)

        last_launch = ctk.CTkFrame(self, corner_radius=14)
        last_launch.place(
            relx=0.04,
            rely=0.65,
            relwidth=0.44,
            relheight=0.29,
        )

        last_title = ctk.CTkLabel(
            last_launch,
            text="ПОСЛЕДНИЙ ЗАПУСК",
            font=font_section,
            anchor="w",
            height=20,
        )
        last_title.place(relx=0.08, rely=0.11, relwidth=0.84)

        last_instance = ctk.CTkLabel(
            last_launch,
            text="PLauncher Survival",
            font=font_body,
            anchor="w",
            height=22,
        )
        last_instance.place(relx=0.08, rely=0.34, relwidth=0.84)

        last_details = ctk.CTkLabel(
            last_launch,
            text="Сегодня в 19:42",
            font=font_small,
            anchor="w",
            height=20,
        )
        last_details.place(relx=0.08, rely=0.58, relwidth=0.84)

        last_java = ctk.CTkLabel(
            last_launch,
            text="Java 21.0.8  •  8192 MB",
            font=ctk.CTkFont(FONT_MONO, 12),
            anchor="w",
            height=18,
        )
        last_java.place(relx=0.08, rely=0.77, relwidth=0.84)

        news = ctk.CTkFrame(self, corner_radius=14)
        news.place(
            relx=0.52,
            rely=0.65,
            relwidth=0.44,
            relheight=0.29,
        )

        news_title = ctk.CTkLabel(
            news,
            text="НОВОСТИ",
            font=font_section,
            anchor="w",
            height=20,
        )
        news_title.place(relx=0.08, rely=0.11, relwidth=0.84)

        news_textbox = ctk.CTkTextbox(
            news,
            font=font_small,
            wrap="word",
            corner_radius=8,
            border_width=0,
            fg_color="transparent",
        )
        news_textbox.place(
            relx=0.08,
            rely=0.29,
            relwidth=0.84,
            relheight=0.62,
        )

        news_textbox.insert(
            "1.0",
            "PLauncher 1.0\n\n"
            "Новый интерфейс и улучшенная система управления экземплярами.\n\n"
            "Добавлена поддержка быстрого выбора сборок, обновлена система запуска "
            "и улучшена стабильность клиента.\n\n"
        )
        news_textbox.configure(state="disabled")
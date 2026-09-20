import customtkinter as ctk


class VersionFrame(ctk.CTkFrame):
    def __init__(self, master, on_delete, **kwargs):
        super().__init__(
            master,
            height=52,
            corner_radius=10,
            **kwargs,
        )

        self.FONT_UI = "Inter 18pt"

        self.version_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(self.FONT_UI, 14),
            anchor="w",
            height=24,
        )
        self.version_label.place(
            relx=0.04,
            rely=0.5,
            anchor="w",
            relwidth=0.78,
        )

        self.delete_button = ctk.CTkButton(
            self,
            text="×",
            font=ctk.CTkFont(self.FONT_UI, 18),
            width=36,
            height=34,
            corner_radius=8,
            command=on_delete,
        )
        self.delete_button.place(
            relx=0.93,
            rely=0.5,
            anchor="center",
        )

    def set_version(self, minecraft, loader):
        text = f"Minecraft {minecraft}"

        if loader:
            text += f" • {loader}"

        self.version_label.configure(
            text=text,
        )


class VersionsPage(ctk.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        self.FONT_UI = "Inter 18pt"
        
        self.FONT_BODY = ctk.CTkFont(self.FONT_UI, 14)

        self.loader_versions = {
        }

        self.versions = [
        ]

        self.version_widgets = []

        self.title_label = ctk.CTkLabel(
            self,
            text="Версии",
            font=ctk.CTkFont(self.FONT_UI, 24, "bold"),
            anchor="w",
            height=32,
        )
        self.title_label.place(
            relx=0.04,
            rely=0.045,
            relwidth=0.92,
        )

        self.versions_list = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            border_width=0,
        )
        self.versions_list.place(
            relx=0.04,
            rely=0.15,
            relwidth=0.92,
            relheight=0.52,
        )

        self.add_frame = ctk.CTkFrame(
            self,
            corner_radius=14,
        )
        self.add_frame.place(
            relx=0.04,
            rely=0.70,
            relwidth=0.92,
            relheight=0.25,
        )

        self.add_title = ctk.CTkLabel(
            self.add_frame,
            text="Добавить версию",
            font=ctk.CTkFont(self.FONT_UI, 13, "bold"),
            anchor="w",
            height=22,
        )
        self.add_title.place(
            relx=0.05,
            rely=0.10,
            relwidth=0.90,
        )

        self.minecraft_combo = ctk.CTkComboBox(
            self.add_frame,
            font=self.FONT_BODY,
            height=38,
        )
        self.minecraft_combo.set("")
        self.minecraft_combo.place(
            relx=0.05,
            rely=0.35,
            relwidth=0.34,
        )

        self.loader_combo = ctk.CTkComboBox(
            self.add_frame,
            values=list(self.loader_versions.keys()),
            font=self.FONT_BODY,
            height=38,
            command=self.loader_changed,
        )
        self.minecraft_combo.set("")
        self.loader_combo.place(
            relx=0.41,
            rely=0.35,
            relwidth=0.34,
        )

        self.add_button = ctk.CTkButton(
            self.add_frame,
            text="Добавить",
            font=ctk.CTkFont(self.FONT_UI, 13, "bold"),
            height=38,
            corner_radius=10,
            command=self.add_version,
        )
        self.add_button.place(
            relx=0.77,
            rely=0.35,
            relwidth=0.18,
        )

        self.progress_bar = ctk.CTkProgressBar(
            self.add_frame,
            height=8,
        )
        self.progress_bar.set(0)
        self.progress_bar.place(
            relx=0.05,
            rely=0.72,
            relwidth=0.90,
        )

        self.progress_label = ctk.CTkLabel(
            self.add_frame,
            text="Готово к установке",
            font=ctk.CTkFont(self.FONT_UI, 12),
            anchor="center",
            height=18,
        )
        self.progress_label.place(
            relx=0.05,
            rely=0.80,
            relwidth=0.90,
        )

        self.refresh_versions()

    def create_version_widget(self, index):
        widget = VersionFrame(
            self.versions_list,
            on_delete=lambda i=index: self.delete_version(i),
        )
        widget.pack(
            fill="x",
            padx=2,
            pady=4,
        )

        self.version_widgets.append(widget)

    def update_version_widget(self, index):
        widget = self.version_widgets[index]
        version = self.versions[index]

        widget.set_version(
            version["minecraft"],
            version["loader"],
        )

        widget.delete_button.configure(
            command=lambda i=index: self.delete_version(i),
        )

    def refresh_versions(self):
        while len(self.version_widgets) < len(self.versions):
            self.create_version_widget(
                len(self.version_widgets),
            )

        for index, widget in enumerate(self.version_widgets):
            if index < len(self.versions):
                widget.pack(
                    fill="x",
                    padx=2,
                    pady=4,
                )
                self.update_version_widget(index)
            else:
                widget.pack_forget()

    def loader_changed(self, loader):
        versions = self.loader_versions.get(loader, [])

        self.minecraft_combo.configure(
            values=versions,
        )

        if versions:
            current = self.minecraft_combo.get()

            if current not in versions:
                self.minecraft_combo.set(versions[0])
        else:
            self.minecraft_combo.set("")

    def add_version(self):
        minecraft_version = self.minecraft_combo.get()
        loader = self.loader_combo.get()

        self.versions.append(
            {
                "minecraft": minecraft_version,
                "loader": loader,
            }
        )

        self.refresh_versions()
        self.versions_list._parent_canvas.yview_moveto(1.0)

    def delete_version(self, index):
        if not 0 <= index < len(self.versions):
            return

        del self.versions[index]
        self.refresh_versions()
    
    def update_loaders_list(self, loaders):
        self.loader_versions = loaders
        self.loader_combo.configure(values=loaders.keys())
        first_loader = list(loaders)[0]
        self.loader_combo.set(first_loader)
        self.loader_changed(first_loader)
import os
import customtkinter as ctk


class InstanceFrame(ctk.CTkFrame):
    def __init__(
            self,
            master,
            instance,
            index,
            font_body,
            font_small,
            on_apply,
            on_delete,
            on_open_folder,
            is_new=False,
            **kwargs,
    ):
        super().__init__(
            master,
            height=130,
            corner_radius=14,
            **kwargs,
        )

        self.instance = instance
        self.index = index
        self.font_body = font_body
        self.font_small = font_small
        self.on_apply = on_apply
        self.on_delete = on_delete
        self.on_open_folder = on_open_folder
        self.is_new = is_new

        self.image_frame = ctk.CTkFrame(
            self,
            width=100,
            height=100,
            corner_radius=10,
        )
        self.image_frame.place(
            relx=0.03,
            rely=0.115,
            relwidth=0.20,
            relheight=0.77,
        )

        self.image_label = ctk.CTkLabel(
            self.image_frame,
            text="",
        )
        self.image_label.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1,
        )

        self.name_label = ctk.CTkLabel(
            self,
            text="",
            font=self.font_body,
            anchor="w",
            height=24,
        )
        self.name_label.place(
            relx=0.26,
            rely=0.16,
            relwidth=0.43,
        )

        self.info_label = ctk.CTkLabel(
            self,
            text="",
            font=self.font_small,
            anchor="w",
            height=20,
        )
        self.info_label.place(
            relx=0.26,
            rely=0.42,
            relwidth=0.43,
        )

        self.uuid_label = ctk.CTkLabel(
            self,
            text="",
            font=self.font_small,
            anchor="w",
            height=18,
        )
        self.uuid_label.place(
            relx=0.26,
            rely=0.66,
            relwidth=0.43,
        )

        self.folder_button = ctk.CTkButton(
            self,
            text="Открыть папку",
            font=self.font_small,
            height=32,
            corner_radius=8,
        )
        self.folder_button.place(
            relx=0.72,
            rely=0.22,
            relwidth=0.24,
        )

        self.delete_button = ctk.CTkButton(
            self,
            text="Удалить",
            font=self.font_small,
            height=32,
            corner_radius=8,
        )
        self.delete_button.place(
            relx=0.72,
            rely=0.58,
            relwidth=0.24,
        )

        self.name_entry = None
        self.version_box = None
        self.icon_button = None
        self.apply_button = None
        self.edit_delete_button = None

        self.update_instance(
            instance,
            index,
        )

    def update_instance(self, instance, index):
        self.instance = instance
        self.index = index

        self.name_label.configure(
            text=instance["name"],
        )

        self.info_label.configure(
            text=instance["version"],
        )

        self.uuid_label.configure(
            text=instance["uuid"],
        )

        if instance["image"] is not None:
            self.image_label.configure(
                image=instance["image"],
                text="",
            )
        else:
            self.image_label.configure(
                image="",
                text="",
            )

        self.folder_button.configure(
            command=lambda i=self.index: self.on_open_folder(i),
        )

        self.delete_button.configure(
            command=lambda i=self.index: self.on_delete(i),
        )

    def create_edit_widgets(self):
        self.image_frame.place_forget()
        self.name_label.place_forget()
        self.info_label.place_forget()
        self.uuid_label.place_forget()
        self.folder_button.place_forget()
        self.delete_button.place_forget()

        self.configure(height=155)

        if self.name_entry is None:
            self.name_entry = ctk.CTkEntry(
                self,
                font=self.font_body,
                height=32,
            )

            self.version_box = ctk.CTkComboBox(
                self,
                values=[
                    "Minecraft 1.21.8",
                    "Minecraft 1.21.7",
                    "Minecraft 1.20.1",
                ],
                font=self.font_small,
                height=32,
            )

            self.icon_button = ctk.CTkButton(
                self,
                text="Выбрать иконку",
                font=self.font_small,
                height=32,
                corner_radius=8,
            )

            self.apply_button = ctk.CTkButton(
                self,
                text="Применить",
                font=self.font_small,
                height=32,
                corner_radius=8,
            )

            self.edit_delete_button = ctk.CTkButton(
                self,
                text="Удалить",
                font=self.font_small,
                height=32,
                corner_radius=8,
            )

        self.image_frame.place(
            relx=0.03,
            rely=0.10,
            relwidth=0.20,
            relheight=0.55,
        )

        self.name_entry.place(
            relx=0.26,
            rely=0.10,
            relwidth=0.43,
        )

        self.version_box.place(
            relx=0.26,
            rely=0.36,
            relwidth=0.43,
        )

        self.uuid_label.place(
            relx=0.26,
            rely=0.67,
            relwidth=0.43,
        )

        self.icon_button.place(
            relx=0.03,
            rely=0.68,
            relwidth=0.20,
        )

        self.apply_button.place(
            relx=0.72,
            rely=0.22,
            relwidth=0.24,
        )

        self.edit_delete_button.place(
            relx=0.72,
            rely=0.52,
            relwidth=0.24,
        )

        self.image_label.configure(
            image="",
            text="",
        )

        self.name_entry.delete(0, "end")
        self.name_entry.insert(
            0,
            self.instance["name"],
        )

        self.version_box.set(
            self.instance["version"],
        )

        self.uuid_label.configure(
            text=self.instance["uuid"],
        )

        self.apply_button.configure(
            command=lambda i=self.index: self.on_apply(i),
        )

        self.edit_delete_button.configure(
            command=lambda i=self.index: self.on_delete(i),
        )

        self.name_entry.focus_set()
        self.name_entry.select_range(0, "end")

    def restore_static(self):
        if self.name_entry is not None:
            self.name_entry.place_forget()
            self.version_box.place_forget()
            self.icon_button.place_forget()
            self.apply_button.place_forget()
            self.edit_delete_button.place_forget()

        self.configure(height=130)

        self.image_frame.place(
            relx=0.03,
            rely=0.115,
            relwidth=0.20,
            relheight=0.77,
        )

        self.name_label.place(
            relx=0.26,
            rely=0.16,
            relwidth=0.43,
        )

        self.info_label.place(
            relx=0.26,
            rely=0.42,
            relwidth=0.43,
        )

        self.uuid_label.place(
            relx=0.26,
            rely=0.66,
            relwidth=0.43,
        )

        self.folder_button.place(
            relx=0.72,
            rely=0.22,
            relwidth=0.24,
        )

        self.delete_button.place(
            relx=0.72,
            rely=0.58,
            relwidth=0.24,
        )

        self.folder_button.configure(
            command=lambda i=self.index: self.on_open_folder(i),
        )

        self.delete_button.configure(
            command=lambda i=self.index: self.on_delete(i),
        )


class InstancesPage(ctk.CTkFrame):
    def __init__(self, master, minecraft_dir=None, **kwargs):
        super().__init__(master, **kwargs)

        self.FONT_UI = "Inter 18pt"

        self.FONT_TITLE = ctk.CTkFont(
            self.FONT_UI,
            24,
            "bold",
        )
        self.FONT_BODY = ctk.CTkFont(
            self.FONT_UI,
            14,
        )
        self.FONT_SMALL = ctk.CTkFont(
            self.FONT_UI,
            11,
        )
        self.FONT_BUTTON = ctk.CTkFont(
            self.FONT_UI,
            12,
            "bold",
        )

        self.minecraft_dir = (
            minecraft_dir
            if minecraft_dir is not None
            else os.path.expanduser("~/.minecraft")
        )

        self.instances_dir = os.path.join(
            self.minecraft_dir,
            "instances",
        )

        self.instances = [
            {
                "uuid": "00000000-0000-0000-0000-000000000001",
                "name": "PLauncher Survival",
                "version": "Minecraft 1.21.8",
                "image": None,
            },
            {
                "uuid": "00000000-0000-0000-0000-000000000002",
                "name": "Vanilla",
                "version": "Minecraft 1.21.8",
                "image": None,
            },
            {
                "uuid": "00000000-0000-0000-0000-000000000003",
                "name": "Performance",
                "version": "Minecraft 1.20.1",
                "image": None,
            },
        ]

        self.instance_widgets = []
        self.editing_indices = set()

        self.title_label = ctk.CTkLabel(
            self,
            text="Экземпляры",
            font=self.FONT_TITLE,
            anchor="w",
            height=32,
        )
        self.title_label.place(
            relx=0.04,
            rely=0.045,
            relwidth=0.70,
        )

        self.add_button = ctk.CTkButton(
            self,
            text="+  Добавить экземпляр",
            font=self.FONT_BUTTON,
            height=38,
            corner_radius=10,
            command=self.add_instance,
        )
        self.add_button.place(
            relx=0.72,
            rely=0.045,
            relwidth=0.24,
        )

        self.instances_list = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            border_width=0
        )
        self.instances_list.place(
            relx=0.04,
            rely=0.14,
            relwidth=0.92,
            relheight=0.82,
        )

        self.refresh_instances()

    def get_instance_path(self, instance):
        return os.path.join(
            self.instances_dir,
            instance["uuid"],
        )

    def create_instance_widget(
            self,
            instance,
            index,
            is_new=False,
    ):
        widget = InstanceFrame(
            self.instances_list,
            instance=instance,
            index=index,
            font_body=self.FONT_BODY,
            font_small=self.FONT_SMALL,
            on_apply=self.apply_instance_edit,
            on_delete=self.delete_instance,
            on_open_folder=self.open_instance_folder,
            is_new=is_new,
        )

        widget.pack(
            fill="x",
            padx=2,
            pady=5,
        )

        self.instance_widgets.append(widget)

        return widget

    def refresh_instances(self):
        while len(self.instance_widgets) < len(self.instances):
            index = len(self.instance_widgets)

            self.create_instance_widget(
                self.instances[index],
                index,
            )

        for index, widget in enumerate(self.instance_widgets):
            if widget.is_new:
                widget.pack(
                    fill="x",
                    padx=2,
                    pady=5,
                )
                continue

            if index < len(self.instances):
                widget.pack(
                    fill="x",
                    padx=2,
                    pady=5,
                )

                widget.update_instance(
                    self.instances[index],
                    index,
                )

                if index not in self.editing_indices:
                    widget.restore_static()
            else:
                widget.pack_forget()

        for index, widget in enumerate(self.instance_widgets):
            widget.index = index

    def add_instance(self):
        if any(widget.is_new for widget in self.instance_widgets):
            return

        instance = {
            "uuid": "00000000-0000-0000-0000-000000000000",
            "name": "Новый экземпляр",
            "version": "Minecraft 1.21.8",
            "image": None,
        }

        index = len(self.instance_widgets)

        widget = self.create_instance_widget(
            instance=instance,
            index=index,
            is_new=True,
        )

        self.editing_indices.add(index)
        widget.create_edit_widgets()

    def apply_instance_edit(self, index):
        if not 0 <= index < len(self.instance_widgets):
            return

        widget = self.instance_widgets[index]

        name = widget.name_entry.get().strip()
        version = widget.version_box.get().strip()

        if not name:
            name = "Новый экземпляр"

        instance = {
            "uuid": widget.instance["uuid"],
            "name": name,
            "version": version,
            "image": widget.instance["image"],
        }

        if widget.is_new:
            self.instances.append(instance)

            widget.is_new = False
            widget.instance = instance
            widget.index = len(self.instances) - 1

            self.editing_indices.discard(index)

            self.refresh_instances()
            widget.restore_static()

        else:
            self.instances[index].update(
                {
                    "name": name,
                    "version": version,
                }
            )

            widget.instance = self.instances[index]

            self.editing_indices.discard(index)

            widget.update_instance(
                self.instances[index],
                index,
            )
            widget.restore_static()

    def delete_instance(self, index):
        if not 0 <= index < len(self.instance_widgets):
            return

        widget = self.instance_widgets[index]

        if widget.is_new:
            widget.destroy()
            self.instance_widgets.pop(index)

            self.editing_indices = {
                i if i < index else i - 1
                for i in self.editing_indices
                if i != index
            }

            for new_index, item in enumerate(self.instance_widgets):
                item.index = new_index

            return

        if not 0 <= index < len(self.instances):
            return

        del self.instances[index]

        widget.destroy()
        self.instance_widgets.pop(index)

        self.editing_indices = {
            i if i < index else i - 1
            for i in self.editing_indices
            if i != index
        }

        for new_index, item in enumerate(self.instance_widgets):
            item.index = new_index

        self.refresh_instances()

    def open_instance_folder(self, index):
        if not 0 <= index < len(self.instances):
            return

        path = self.get_instance_path(
            self.instances[index],
        )

        print(f"OPEN: {path}")
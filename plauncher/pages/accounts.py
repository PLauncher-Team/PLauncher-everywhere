import customtkinter as ctk


class AccountFrame(ctk.CTkFrame):
    def __init__(
            self,
            master,
            account,
            index,
            font_body,
            font_small,
            on_select,
            on_delete,
            on_apply_edit,
            is_new=False,
            **kwargs,
    ):
        super().__init__(
            master,
            height=60,
            corner_radius=10,
            **kwargs,
        )

        self.font_body = font_body
        self.font_small = font_small
        self.on_select = on_select
        self.on_delete = on_delete
        self.on_apply_edit = on_apply_edit
        self.index = index
        self.account = account
        self.is_new = is_new

        self.name_label = ctk.CTkLabel(
            self,
            text="",
            font=self.font_body,
            anchor="w",
            height=22,
        )
        self.name_label.place(
            relx=0.05,
            rely=0.12,
            relwidth=0.57,
        )

        self.type_label = ctk.CTkLabel(
            self,
            text="",
            font=self.font_small,
            anchor="w",
            height=18,
        )
        self.type_label.place(
            relx=0.05,
            rely=0.52,
            relwidth=0.57,
        )

        self.delete_button = ctk.CTkButton(
            self,
            text="Удалить",
            font=self.font_small,
            height=30,
            corner_radius=8,
        )
        self.delete_button.place(
            relx=0.70,
            rely=0.25,
            relwidth=0.25,
        )

        self.name_entry = None
        self.type_box = None
        self.apply_button = None
        self.edit_delete_button = None

        for widget in (self, self.name_label, self.type_label):
            widget.bind(
                "<Button-1>",
                self._select,
            )

        self.update_account(account, index)

    def _select(self, event=None):
        self.on_select(self.index)

    def update_account(self, account, index):
        self.account = account
        self.index = index

        self.name_label.configure(
            text=account["name"],
        )

        self.type_label.configure(
            text=account["type"],
        )

        self.delete_button.configure(
            command=lambda i=self.index: self.on_delete(i),
        )

    def create_edit_widgets(self):
        self.name_label.place_forget()
        self.type_label.place_forget()
        self.delete_button.place_forget()

        self.configure(height=92)

        if self.name_entry is None:
            self.name_entry = ctk.CTkEntry(
                self,
                font=self.font_body,
                height=30,
            )

            self.type_box = ctk.CTkComboBox(
                self,
                values=[
                    "ely.by",
                    "offline",
                ],
                font=self.font_small,
                height=30,
            )

            self.apply_button = ctk.CTkButton(
                self,
                text="Применить",
                font=self.font_small,
                height=30,
                corner_radius=8,
            )

            self.edit_delete_button = ctk.CTkButton(
                self,
                text="Удалить",
                font=self.font_small,
                height=30,
                corner_radius=8,
            )

        self.name_entry.place(
            relx=0.05,
            rely=0.10,
            relwidth=0.56,
        )

        self.type_box.place(
            relx=0.05,
            rely=0.52,
            relwidth=0.56,
        )

        self.apply_button.place(
            relx=0.66,
            rely=0.10,
            relwidth=0.29,
        )

        self.edit_delete_button.place(
            relx=0.66,
            rely=0.52,
            relwidth=0.29,
        )

        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, self.account["name"])

        self.type_box.set(self.account["type"])

        self.apply_button.configure(
            command=lambda i=self.index: self.on_apply_edit(i),
        )

        self.edit_delete_button.configure(
            command=lambda i=self.index: self.on_delete(i),
        )

        self.name_entry.focus_set()
        self.name_entry.select_range(0, "end")

    def restore_static_widgets(self):
        if self.name_entry is not None:
            self.name_entry.place_forget()
            self.type_box.place_forget()
            self.apply_button.place_forget()
            self.edit_delete_button.place_forget()

        self.configure(height=60)

        self.name_label.place(
            relx=0.05,
            rely=0.12,
            relwidth=0.57,
        )

        self.type_label.place(
            relx=0.05,
            rely=0.52,
            relwidth=0.57,
        )

        self.delete_button.place(
            relx=0.70,
            rely=0.25,
            relwidth=0.25,
        )

        self.delete_button.configure(
            command=lambda i=self.index: self.on_delete(i),
        )


class AccountsPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.FONT_UI = "Inter 18pt"

        self.FONT_TITLE = ctk.CTkFont(
            self.FONT_UI,
            24,
            "bold",
        )
        self.FONT_SECTION = ctk.CTkFont(
            self.FONT_UI,
            13,
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

        self.accounts = [
            {
                "uuid": "550e8400-e29b-41d4-a716-446655440001",
                "name": "Sasha",
                "type": "ely.by",
            },
            {
                "uuid": "550e8400-e29b-41d4-a716-446655440002",
                "name": "Player123",
                "type": "offline",
            },
        ]

        self.account_widgets = []
        self.selected_index = 0
        self.editing_indices = set()

        self.title_label = ctk.CTkLabel(
            self,
            text="Аккаунты",
            font=self.FONT_TITLE,
            anchor="w",
            height=32,
        )
        self.title_label.place(
            relx=0.04,
            rely=0.045,
            relwidth=0.92,
        )

        self.accounts_frame = ctk.CTkFrame(
            self,
            corner_radius=14,
        )
        self.accounts_frame.place(
            relx=0.04,
            rely=0.15,
            relwidth=0.54,
            relheight=0.81,
        )

        self.accounts_title = ctk.CTkLabel(
            self.accounts_frame,
            text="Сохранённые аккаунты",
            font=self.FONT_SECTION,
            anchor="w",
            height=22,
        )
        self.accounts_title.place(
            relx=0.06,
            rely=0.06,
            relwidth=0.88,
        )

        self.accounts_list = ctk.CTkScrollableFrame(
            self.accounts_frame,
            fg_color="transparent",
            border_width=0,
        )
        self.accounts_list.place(
            relx=0.04,
            rely=0.14,
            relwidth=0.92,
            relheight=0.70,
        )

        self.add_button = ctk.CTkButton(
            self.accounts_frame,
            text="+  Добавить аккаунт",
            font=self.FONT_BUTTON,
            height=40,
            corner_radius=10,
            command=self.add_account,
        )
        self.add_button.place(
            relx=0.06,
            rely=0.85,
            relwidth=0.88,
        )

        self.skin_frame = ctk.CTkFrame(
            self,
            corner_radius=14,
        )
        self.skin_frame.place(
            relx=0.61,
            rely=0.15,
            relwidth=0.35,
            relheight=0.81,
        )

        self.skin_title = ctk.CTkLabel(
            self.skin_frame,
            text="Скин",
            font=self.FONT_SECTION,
            anchor="w",
            height=22,
        )
        self.skin_title.place(
            relx=0.10,
            rely=0.06,
            relwidth=0.80,
        )

        self.skin_placeholder = ctk.CTkLabel(
            self.skin_frame,
            text="",
        )
        self.skin_placeholder.place(
            relx=0.10,
            rely=0.16,
            relwidth=0.80,
            relheight=0.55,
        )

        self.account_name_label = ctk.CTkLabel(
            self.skin_frame,
            text="",
            font=self.FONT_BODY,
            anchor="center",
            height=22,
        )
        self.account_name_label.place(
            relx=0.10,
            rely=0.83,
            relwidth=0.80,
        )

        self.account_type_label = ctk.CTkLabel(
            self.skin_frame,
            text="",
            font=self.FONT_SMALL,
            anchor="center",
            height=18,
        )
        self.account_type_label.place(
            relx=0.10,
            rely=0.88,
            relwidth=0.80,
        )

        self.account_uuid_label = ctk.CTkLabel(
            self.skin_frame,
            text="",
            font=self.FONT_SMALL,
            anchor="center",
            height=18,
        )
        self.account_uuid_label.place(
            relx=0.08,
            rely=0.92,
            relwidth=0.84,
        )

        self.refresh_accounts()

    def create_account_widget(self, index, account=None, is_new=False):
        if account is None:
            account = self.accounts[index]

        account_widget = AccountFrame(
            self.accounts_list,
            account=account,
            index=index,
            font_body=self.FONT_BODY,
            font_small=self.FONT_SMALL,
            on_select=self.select_account,
            on_delete=self.delete_account,
            on_apply_edit=self.apply_account_edit,
            is_new=is_new,
        )

        account_widget.pack(
            fill="x",
            padx=2,
            pady=4,
        )

        self.account_widgets.append(account_widget)

    def update_account_widget(self, index):
        if index >= len(self.accounts):
            return

        account_widget = self.account_widgets[index]

        if account_widget.is_new:
            return

        account_widget.update_account(
            self.accounts[index],
            index,
        )

        if index not in self.editing_indices:
            account_widget.restore_static_widgets()

    def refresh_accounts(self):
        while len(self.account_widgets) < len(self.accounts):
            self.create_account_widget(len(self.account_widgets))

        for index, account_widget in enumerate(self.account_widgets):
            if index < len(self.accounts):
                account_widget.pack(
                    fill="x",
                    padx=2,
                    pady=4,
                )
                self.update_account_widget(index)
            else:
                account_widget.pack_forget()

        if self.accounts:
            self.selected_index = min(
                self.selected_index,
                len(self.accounts) - 1,
                )
            self.update_selection()
        else:
            self.selected_index = -1
            self.account_name_label.configure(text="")
            self.account_type_label.configure(text="")
            self.account_uuid_label.configure(text="")

    def select_account(self, index):
        if not 0 <= index < len(self.account_widgets):
            return

        if self.account_widgets[index].is_new:
            return

        if not 0 <= index < len(self.accounts):
            return

        self.selected_index = index
        self.update_selection()

    def update_selection(self):
        for index, account_widget in enumerate(self.account_widgets):
            if index >= len(self.accounts):
                continue

            account_widget.configure(
                border_width=2 if index == self.selected_index else 0,
            )

        if 0 <= self.selected_index < len(self.accounts):
            account = self.accounts[self.selected_index]

            self.account_name_label.configure(
                text=account["name"],
            )
            self.account_type_label.configure(
                text=account["type"],
            )
            self.account_uuid_label.configure(
                text=account["uuid"],
            )
        else:
            self.account_name_label.configure(text="")
            self.account_type_label.configure(text="")
            self.account_uuid_label.configure(text="")

    def add_account(self):
        if any(widget.is_new for widget in self.account_widgets):
            return

        account = {
            "uuid": "00000000-0000-0000-0000-000000000000",
            "name": "Новый аккаунт",
            "type": "offline",
        }

        index = len(self.account_widgets)

        self.create_account_widget(
            index,
            account=account,
            is_new=True,
        )

        self.editing_indices.add(index)

        self.account_widgets[index].create_edit_widgets()

    def apply_account_edit(self, index):
        if not 0 <= index < len(self.account_widgets):
            return

        account_widget = self.account_widgets[index]

        name = account_widget.name_entry.get().strip()
        account_type = account_widget.type_box.get().strip()

        if not name:
            name = "Новый аккаунт"

        account = {
            "uuid": account_widget.account["uuid"],
            "name": name,
            "type": account_type,
        }

        if account_widget.is_new:
            self.accounts.append(account)

            account_widget.is_new = False
            account_widget.account = account
            account_widget.index = len(self.accounts) - 1

            self.editing_indices.discard(index)

            self.refresh_accounts()
            self.select_account(len(self.accounts) - 1)
        else:
            self.accounts[index]["name"] = name
            self.accounts[index]["type"] = account_type

            self.editing_indices.discard(index)

            account_widget.update_account(
                self.accounts[index],
                index,
            )
            account_widget.restore_static_widgets()

            self.select_account(index)

    def delete_account(self, index):
        if not 0 <= index < len(self.account_widgets):
            return

        account_widget = self.account_widgets[index]

        if account_widget.is_new:
            account_widget.destroy()
            self.account_widgets.pop(index)

            self.editing_indices = {
                i if i < index else i - 1
                for i in self.editing_indices
                if i != index
            }

            for new_index, widget in enumerate(self.account_widgets):
                widget.index = new_index

            return

        if not 0 <= index < len(self.accounts):
            return

        del self.accounts[index]

        account_widget.destroy()
        self.account_widgets.pop(index)

        self.editing_indices = {
            i if i < index else i - 1
            for i in self.editing_indices
            if i != index
        }

        for new_index, widget in enumerate(self.account_widgets):
            widget.index = new_index

        if not self.accounts:
            self.selected_index = -1
        elif self.selected_index > index:
            self.selected_index -= 1
        elif self.selected_index == index:
            self.selected_index = min(
                index,
                len(self.accounts) - 1,
                )

        self.refresh_accounts()
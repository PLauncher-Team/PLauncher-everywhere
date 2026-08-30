import customtkinter as ctk


class JavaPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.FONT_UI = "Inter 18pt"

        self.FONT_TITLE = ctk.CTkFont(self.FONT_UI, 24, "bold")
        self.FONT_SECTION = ctk.CTkFont(self.FONT_UI, 13, "bold")
        self.FONT_BODY = ctk.CTkFont(self.FONT_UI, 14)
        self.FONT_SMALL = ctk.CTkFont(self.FONT_UI, 12)
        self.FONT_BUTTON = ctk.CTkFont(self.FONT_UI, 13, "bold")
        self.FONT_MONO = ctk.CTkFont("JetBrains Mono", 12)

        self.java_versions = [
            "Java 8",
            "Java 11",
            "Java 17",
            "Java 21",
            "Java 25",
        ]

        self.recommended_java = "Java 21"

        self.memory_min = 512
        self.memory_max = 16384
        self.memory_step = 512
        self.memory_value = 4096

        self.title_label = ctk.CTkLabel(
            self,
            text="Java",
            font=self.FONT_TITLE,
            anchor="w",
            height=32,
        )
        self.title_label.place(
            relx=0.04,
            rely=0.045,
            relwidth=0.92,
        )

        self.settings_frame = ctk.CTkFrame(
            self,
            corner_radius=14,
        )
        self.settings_frame.place(
            relx=0.04,
            rely=0.15,
            relwidth=0.92,
            relheight=0.81,
        )

        self.runtime_frame = ctk.CTkFrame(
            self.settings_frame,
            fg_color="transparent",
            border_width=0
        )
        self.runtime_frame.place(
            relx=0.05,
            rely=0.06,
            relwidth=0.90,
            relheight=0.30,
        )

        self.runtime_title = ctk.CTkLabel(
            self.runtime_frame,
            text="Среда выполнения",
            font=self.FONT_SECTION,
            anchor="w",
            height=22,
        )
        self.runtime_title.place(
            relx=0,
            rely=0,
            relwidth=1,
        )

        self.recommended_checkbox = ctk.CTkCheckBox(
            self.runtime_frame,
            text="Использовать рекомендуемую версию",
            font=ctk.CTkFont(self.FONT_UI, 12),
            command=self.toggle_java_selection,
        )
        self.recommended_checkbox.place(
            relx=0,
            rely=0.23,
        )
        self.recommended_checkbox.select()

        self.java_label = ctk.CTkLabel(
            self.runtime_frame,
            text="Версия Java",
            font=self.FONT_SMALL,
            anchor="w",
            height=20,
        )
        self.java_label.place(
            relx=0,
            rely=0.58,
            relwidth=0.20,
        )

        self.java_combo = ctk.CTkComboBox(
            self.runtime_frame,
            values=self.java_versions,
            font=self.FONT_BODY,
            height=38,
        )
        self.java_combo.set(self.recommended_java)
        self.java_combo.place(
            relx=0.22,
            rely=0.48,
            relwidth=0.58,
        )

        self.add_java_button = ctk.CTkButton(
            self.runtime_frame,
            text="+",
            font=self.FONT_BUTTON,
            width=40,
            height=38,
            corner_radius=10,
            command=self.add_java,
        )
        self.add_java_button.place(
            relx=0.83,
            rely=0.48,
            relwidth=0.17,
        )

        self.jvm_frame = ctk.CTkFrame(
            self.settings_frame,
            fg_color="transparent",
            border_width=0
        )
        self.jvm_frame.place(
            relx=0.05,
            rely=0.40,
            relwidth=0.90,
            relheight=0.25,
        )

        self.jvm_title = ctk.CTkLabel(
            self.jvm_frame,
            text="Аргументы JVM",
            font=self.FONT_SECTION,
            anchor="w",
            height=22,
        )
        self.jvm_title.place(
            relx=0,
            rely=0,
            relwidth=1,
        )

        self.jvm_description = ctk.CTkLabel(
            self.jvm_frame,
            text="Дополнительные параметры запуска Java",
            font=self.FONT_SMALL,
            anchor="w",
            height=20,
        )
        self.jvm_description.place(
            relx=0,
            rely=0.22,
            relwidth=1,
        )

        self.jvm_entry = ctk.CTkEntry(
            self.jvm_frame,
            font=self.FONT_MONO,
            placeholder_text="-XX:+UseG1GC -XX:+ParallelRefProcEnabled",
            height=42,
        )
        self.jvm_entry.place(
            relx=0,
            rely=0.50,
            relwidth=1,
        )

        self.memory_frame = ctk.CTkFrame(
            self.settings_frame,
            fg_color="transparent",
            border_width=0
        )
        self.memory_frame.place(
            relx=0.05,
            rely=0.70,
            relwidth=0.90,
            relheight=0.25,
        )

        self.memory_title = ctk.CTkLabel(
            self.memory_frame,
            text="Память",
            font=self.FONT_SECTION,
            anchor="w",
            height=22,
        )
        self.memory_title.place(
            relx=0,
            rely=0,
            relwidth=0.40,
        )

        self.memory_entry = ctk.CTkEntry(
            self.memory_frame,
            font=self.FONT_BODY,
            width=110,
            height=36,
            justify="right",
            validate="key",
            validatecommand=(
                self.register(self.validate_memory),
                "%P",
            ),
        )
        self.memory_entry.insert(0, str(self.memory_value))
        self.memory_entry.place(
            relx=0.70,
            rely=0.2,
            relwidth=0.20,
        )

        self.memory_unit = ctk.CTkLabel(
            self.memory_frame,
            text="MB",
            font=self.FONT_SMALL,
            anchor="w",
            height=20,
        )
        self.memory_unit.place(
            relx=0.91,
            rely=0.34,
            relwidth=0.09,
        )

        self.memory_slider = ctk.CTkSlider(
            self.memory_frame,
            from_=self.memory_min,
            to=self.memory_max,
            number_of_steps=(
                    (self.memory_max - self.memory_min) // self.memory_step
            ),
            command=self.memory_slider_changed,
        )
        self.memory_slider.set(self.memory_value)
        self.memory_slider.place(
            relx=0,
            rely=0.60,
            relwidth=0.90,
        )

        self.memory_min_label = ctk.CTkLabel(
            self.memory_frame,
            text="512 MB",
            font=self.FONT_SMALL,
            anchor="w",
            height=18,
        )
        self.memory_min_label.place(
            relx=0,
            rely=0.84,
            relwidth=0.25,
        )

        self.memory_max_label = ctk.CTkLabel(
            self.memory_frame,
            text="16384 MB",
            font=self.FONT_SMALL,
            anchor="e",
            height=18,
        )
        self.memory_max_label.place(
            relx=0.65,
            rely=0.84,
            relwidth=0.25,
        )

        self.memory_entry.bind(
            "<KeyRelease>",
            self.memory_entry_changed,
        )
        self.memory_entry.bind(
            "<FocusOut>",
            self.memory_entry_focus_out,
        )
        self.memory_entry.bind(
            "<Return>",
            self.memory_entry_focus_out,
        )

        self.toggle_java_selection()

    def toggle_java_selection(self):
        state = "disabled" if self.recommended_checkbox.get() else "normal"

        self.java_combo.configure(
            state=state,
        )
        self.add_java_button.configure(
            state=state,
        )

    def add_java(self):
        pass

    def validate_memory(self, value):
        return value.isdigit() or value == ""

    def memory_slider_changed(self, value):
        value = int(round(float(value) / self.memory_step) * self.memory_step)
        value = max(self.memory_min, min(self.memory_max, value))

        self.memory_value = value

        self.memory_entry.delete(0, "end")
        self.memory_entry.insert(0, str(value))


    def memory_entry_changed(self, event=None):
        value = self.memory_entry.get()

        if not value:
            return

        value = int(value)
        value = max(self.memory_min, min(self.memory_max, value))

        self.memory_value = value
        self.memory_slider.set(value)


    def memory_entry_focus_out(self, event=None):
        value = self.memory_entry.get()

        if not value:
            value = self.memory_min
        else:
            value = int(value)

        value = max(self.memory_min, min(self.memory_max, value))
        value = int(round(value / self.memory_step) * self.memory_step)
        value = max(self.memory_min, min(self.memory_max, value))

        self.memory_value = value
        self.memory_slider.set(value)

        self.memory_entry.delete(0, "end")
        self.memory_entry.insert(0, str(value))
from .home import HomePage
from .accounts import AccountsPage
from .instances import InstancesPage
from .java import JavaPage
from .versions import VersionsPage
import customtkinter as ctk
from PIL import Image
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ICONS_DIR = os.path.join(CURRENT_DIR, 'icons')

class VerticalPagePanel(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)
        self.pages = []
        self.buttons = []
        self.current_index = 1
        self.btn_bg = ctk.ThemeManager.theme["CTkButton"]["fg_color"][1]
        self.btn_active = ctk.ThemeManager.theme["CTkButton"]["hover_color"][1]
        self._anim_id = None

        self._btn_size = 48
        self._indicator_h = 34
        self._pad_y = 10

        self.nav_frame = ctk.CTkFrame(self, width=70, corner_radius=0, border_width=0)
        self.nav_frame.pack(side="left", fill="y")

        self.content_frame = ctk.CTkFrame(self, corner_radius=0, border_width=0)
        self.content_frame.pack(side="left", fill="both", expand=True)

        self.indicator = ctk.CTkFrame(
            self.nav_frame,
            width=3,
            height=self._indicator_h,
            corner_radius=2,
            fg_color=self.btn_active
        )
        self.indicator.place(x=0, y=0)
        self.indicator.lower()
        
        pages_dict = {"home": HomePage(self.content_frame), "accounts": AccountsPage(self.content_frame),
                      "instances": InstancesPage(self.content_frame), "java": JavaPage(self.content_frame),
                      "versions": VersionsPage(self.content_frame)}
        for page in ["home", "accounts", "instances", "versions", "java", "logs", "settings"]:
            self._add_page(os.path.join(ICONS_DIR, f"{page}.png"), pages_dict.get(page))

        self.after(100, lambda: self.select_page(0))

    def _add_page(self, image_path: str, page_frame: ctk.CTkFrame=None):
        if page_frame is None:
            page_frame = ctk.CTkFrame(self.content_frame)
        idx = len(self.pages)
        self.pages.append(page_frame)

        pil_image = Image.open(image_path).convert("RGBA")
        ctk_image = ctk.CTkImage(
            light_image=pil_image,
            dark_image=pil_image,
            size=(23, 23)
        )

        btn = ctk.CTkButton(
            self.nav_frame,
            image=ctk_image,
            text="",
            width=self._btn_size,
            height=self._btn_size,
            corner_radius=11,
            fg_color=self.btn_bg,
            hover_color=("#D0D0D0", "#3A3A3A"),
            border_width=0,
            command=lambda i=idx: self.select_page(i)
        )
        btn.pack(pady=(self._pad_y * 2 if idx == 0 else self._pad_y, self._pad_y), padx=15)
        self.buttons.append(btn)

    def select_page(self, index: int):
        if index < 0 or index >= len(self.pages) or index == self.current_index:
            return

        self.pages[self.current_index].place_forget()
        self.buttons[self.current_index].configure(fg_color=self.btn_bg)

        self.pages[index].place(relx=0, rely=0.04, relwidth=0.96, relheight=0.92)
        self.buttons[index].configure(fg_color=self.btn_active)

        self.update_idletasks()
        btn = self.buttons[index]
        target_y = btn.winfo_y() + (btn.winfo_height() - self._indicator_h) // 2

        self._animate_indicator(target_y)
        self.current_index = index

    def _animate_indicator(self, target_y: int, duration: int = 180):
        if self._anim_id is not None:
            self.after_cancel(self._anim_id)
            self._anim_id = None

        start_y = self.indicator.winfo_y()
        delta = target_y - start_y
        if abs(delta) < 1:
            self.indicator.place(x=0, y=target_y)
            self.indicator.lift()
            return

        delay = max(1, round(1000 / 144))
        steps = max(1, round(duration / delay))
        step = 0

        def animate():
            nonlocal step
            step += 1
            t = step / steps
            eased = 1 - (1 - t) ** 3
            y = start_y + delta * eased
            self.indicator.place(x=0, y=int(y))
            self.indicator.lift()
            if step < steps:
                self._anim_id = self.after(delay, animate)
            else:
                self.indicator.place(x=0, y=target_y)
                self.indicator.lift()
                self._anim_id = None

        animate()

    def get_current_page(self):
        if 0 <= self.current_index < len(self.pages):
            return self.pages[self.current_index]
        return None

    def get_page(self, index: int):
        if 0 <= index < len(self.pages):
            return self.pages[index]
        return None
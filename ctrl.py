import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

# ========== TOOLTIP CLASS ==========

class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 600
        self.wraplength = 220
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        _id = self.id
        self.id = None
        if _id:
            self.widget.after_cancel(_id)

    def showtip(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert") if self.widget.bbox("insert") else (0,0,0,0)
        x += self.widget.winfo_rootx() + 20
        y += self.widget.winfo_rooty() + 20
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            self.tw, text=self.text, justify='left',
            background="#222", foreground="#ddd",
            relief='solid', borderwidth=1,
            wraplength=self.wraplength,
            font=("Segoe UI", 9)
        )
        label.pack(ipadx=4, ipady=2)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()

# ========== MAIN APP ==========

class CTRLBoostApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CTRL Boost - Performance Tweaks")
        self.geometry("900x650")
        self.minsize(900, 650)
        self.configure(bg="#0F172A")  # dark blue background
        self.wm_attributes('-alpha', 0.95)  # slight transparency

        # Colors
        self.purple = "#7B5FFF"
        self.blueice = "#6AC1FF"
        self.bg_color = "#0F172A"
        self.fg_color = "#E0E7FF"

        # Style setup
        self.style = ttk.Style(self)
        self.style.theme_use("default")

        # Configure styles manually
        self.style.configure('.', background=self.bg_color, foreground=self.fg_color, font=("Segoe UI", 10))
        self.style.configure('TNotebook', background=self.bg_color, borderwidth=0)
        self.style.configure('TNotebook.Tab', padding=[15, 8], font=("Segoe UI Semibold", 11), background=self.bg_color, foreground="#A6B0D9")
        self.style.map('TNotebook.Tab',
                       background=[("selected", self.purple), ("active", "#5A43D1")],
                       foreground=[("selected", "#FFFFFF"), ("!selected", "#A6B0D9")])
        self.style.configure('TLabel', background=self.bg_color, foreground=self.fg_color)
        self.style.configure('TCheckbutton', background=self.bg_color, foreground=self.fg_color)
        self.style.configure('TButton', background=self.purple, foreground="#FFF", font=("Segoe UI Semibold", 10))
        self.style.map('TButton',
                       background=[("active", "#6B4EF9")],
                       foreground=[("active", "#FFF")])

        # Header label
        header = ttk.Label(self, text="CTRL Boost - Performance Tweaks", font=("Segoe UI Black", 20), foreground=self.purple, background=self.bg_color)
        header.pack(pady=10)

        # Notebook with tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both', padx=15, pady=10)

        # Tabs frames
        self.home_tab = ttk.Frame(self.notebook)
        self.general_tab = ttk.Frame(self.notebook)
        self.games_tab = ttk.Frame(self.notebook)
        self.internet_tab = ttk.Frame(self.notebook)
        self.storage_tab = ttk.Frame(self.notebook)
        self.memory_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.home_tab, text="Home")
        self.notebook.add(self.general_tab, text="General")
        self.notebook.add(self.games_tab, text="Games")
        self.notebook.add(self.internet_tab, text="Internet")
        self.notebook.add(self.storage_tab, text="Storage")
        self.notebook.add(self.memory_tab, text="Memory")

        # Build tabs content
        self.build_home_tab()
        self.build_general_tab()
        self.build_games_tab()
        self.build_internet_tab()
        self.build_storage_tab()
        self.build_memory_tab()

        # Slideout notification bar
        self.slideout_frame = tk.Frame(self, bg=self.purple, height=30)
        self.slideout_label = tk.Label(self.slideout_frame, text="", fg="white", bg=self.purple, font=("Segoe UI", 10, "bold"))
        self.slideout_label.pack(side="left", padx=15)
        self.slideout_frame.place(relx=1.0, rely=1.0, anchor='se', x=0, y=0, width=0, height=30)
        self.slideout_animating = False

    def slideout_show(self, msg):
        if self.slideout_animating:
            return
        self.slideout_animating = True
        self.slideout_label.config(text=msg)
        width = 0
        max_width = self.winfo_width()

        def animate_in():
            nonlocal width
            width += 25
            if width >= max_width:
                width = max_width
                self.slideout_frame.place(relx=1.0, rely=1.0, anchor='se', x=0, y=0, width=width, height=30)
                self.after(2500, animate_out)
                return
            self.slideout_frame.place(relx=1.0, rely=1.0, anchor='se', x=0, y=0, width=width, height=30)
            self.after(10, animate_in)

        def animate_out():
            nonlocal width
            width -= 25
            if width <= 0:
                width = 0
                self.slideout_frame.place_forget()
                self.slideout_animating = False
                return
            self.slideout_frame.place(relx=1.0, rely=1.0, anchor='se', x=0, y=0, width=width, height=30)
            self.after(10, animate_out)

        animate_in()

    def build_home_tab(self):
        frame = self.home_tab
        discord_btn = ttk.Button(frame, text="Join Discord", command=self.open_discord)
        discord_btn.pack(pady=15)

        preset_frame = ttk.Frame(frame)
        preset_frame.pack(pady=10)

        ttk.Label(preset_frame, text="Select Preset:").pack(side="left", padx=5)
        self.preset_var = tk.StringVar(value="Balanced")
        presets = ["Desktop", "Balanced", "Laptop"]
        preset_dropdown = ttk.Combobox(preset_frame, values=presets, state="readonly", textvariable=self.preset_var)
        preset_dropdown.pack(side="left")
        preset_dropdown.bind("<<ComboboxSelected>>", self.preset_selected)

        credits_btn = ttk.Button(frame, text="Credits", command=self.show_ascii_credits)
        credits_btn.pack(pady=15)

        self.home_info_label = ttk.Label(frame, text="Choose a preset to auto-select best tweaks.", wraplength=600, justify="center")
        self.home_info_label.pack(pady=10)

    def open_discord(self):
        url = "https://discord.gg/7KCWNccRUe"  
        try:
            if sys.platform == "win32":
                os.startfile(url)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", url])
            else:
                subprocess.Popen(["xdg-open", url])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Discord:\n{e}")

    def show_ascii_credits(self):
        credits_text = r"""
██╗   ██╗██╗██████╗ ███████╗██╗     ███████╗
██║   ██║██║██╔══██╗██╔════╝██║     ██╔════╝
██║   ██║██║██████╔╝█████╗  ██║     █████╗  
██║   ██║██║██╔══██╗██╔══╝  ██║     ██╔══╝  
╚██████╔╝██║██║  ██║███████╗███████╗███████╗
 ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
        """
        os.system("cls")
        print("\033[38;5;54m" + credits_text + "\033[0m")
        input("Press Enter to return...")

    def preset_selected(self, event=None):
        preset = self.preset_var.get()
        all_toggles = self.get_all_toggles()
        # Clear all toggles first
        for toggles_list in all_toggles.values():
            for tvar in toggles_list:
                tvar.set(False)

        if preset == "Desktop":
            self.set_toggles("General", list(range(20)), True)
            self.set_toggles("Internet", list(range(20)), True)
            self.set_toggles("Storage", list(range(10)), True)
        elif preset == "Balanced":
            self.set_toggles("General", list(range(10)), True)
            self.set_toggles("Internet", list(range(10)), True)
        elif preset == "Laptop":
            self.set_toggles("General", list(range(10)), True)
            self.set_toggles("Memory", list(range(15)), True)

        self.slideout_show(f"Preset '{preset}' applied!")

    def get_all_toggles(self):
        return {
            "General": self.general_toggle_vars,
            "Games": self.games_toggle_vars,
            "Internet": self.internet_toggle_vars,
            "Storage": self.storage_toggle_vars,
            "Memory": self.memory_toggle_vars,
        }

    def set_toggles(self, category, indices, value):
        toggles_list = getattr(self, f"{category.lower()}_toggle_vars")
        for i in indices:
            if i < len(toggles_list):
                toggles_list[i].set(value)

    def build_general_tab(self):
        frame = self.general_tab
        self.general_toggle_vars = []
        general_tweaks = [
            ("Enable CPU Boost Mode", "Improves CPU frequency scaling."),
            ("Disable Startup Programs", "Speeds up boot time by disabling unneeded programs."),
            ("Enable Game Mode", "Optimizes system for gaming."),
            ("Disable Animations", "Turns off visual animations for better performance."),
            ("Disable Windows Tips", "Disables annoying tips and notifications."),
            ("Optimize Power Settings", "Sets power plan to high performance."),
            ("Disable Background Apps", "Stops apps from running in background."),
            ("Disable Windows Search Indexing", "Improves disk performance."),
            ("Increase Network Throughput", "Tweaks TCP settings for speed."),
            ("Clear Temp Files", "Removes temporary files to free space."),
        ]
        for text, tip in general_tweaks:
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(frame, text=text, variable=var)
            cb.pack(anchor="w", pady=5, padx=15)
            CreateToolTip(cb, tip)
            self.general_toggle_vars.append(var)

    def build_games_tab(self):
        frame = self.games_tab
        self.games_toggle_vars = []
        games_tweaks = [
            ("Disable VSync", "May reduce input lag but can cause tearing."),
            ("Enable Fullscreen Optimizations", "Allows Windows to optimize fullscreen apps."),
            ("Disable Game DVR", "Prevents Windows from recording gameplay."),
            ("Increase Process Priority", "Gives games higher CPU priority."),
            ("Disable Background Services", "Stops services not required during gaming."),
        ]
        for text, tip in games_tweaks:
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(frame, text=text, variable=var)
            cb.pack(anchor="w", pady=5, padx=15)
            CreateToolTip(cb, tip)
            self.games_toggle_vars.append(var)

    def build_internet_tab(self):
        frame = self.internet_tab
        self.internet_toggle_vars = []
        internet_tweaks = [
            ("Enable TCP Fast Open", "Speeds up TCP connections."),
            ("Disable Nagle's Algorithm", "Reduces latency for gaming."),
            ("Increase Max TCP Connections", "Allows more simultaneous connections."),
            ("Enable DNS Cache", "Speeds up DNS resolution."),
            ("Disable Auto-tuning", "Fixes some network performance issues."),
        ]
        for text, tip in internet_tweaks:
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(frame, text=text, variable=var)
            cb.pack(anchor="w", pady=5, padx=15)
            CreateToolTip(cb, tip)
            self.internet_toggle_vars.append(var)

    def build_storage_tab(self):
        frame = self.storage_tab
        self.storage_toggle_vars = []
        storage_tweaks = [
            ("Enable Write Caching", "Improves disk write speed."),
            ("Disable Superfetch", "Reduces disk usage."),
            ("Disable Disk Indexing", "Improves disk performance."),
            ("Enable TRIM for SSD", "Optimizes SSD performance."),
            ("Defragment HDD Weekly", "Schedules regular defragmentation."),
        ]
        for text, tip in storage_tweaks:
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(frame, text=text, variable=var)
            cb.pack(anchor="w", pady=5, padx=15)
            CreateToolTip(cb, tip)
            self.storage_toggle_vars.append(var)

    def build_memory_tab(self):
        frame = self.memory_tab
        self.memory_toggle_vars = []
        memory_tweaks = [
            ("Enable ReadyBoost", "Speeds up disk caching."),
            ("Increase Virtual Memory", "Expands paging file size."),
            ("Disable Memory Compression", "Turns off compression for speed."),
            ("Clear Standby List", "Frees up unused RAM."),
            ("Disable Prefetch", "Disables prefetch service."),
        ]
        for text, tip in memory_tweaks:
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(frame, text=text, variable=var)
            cb.pack(anchor="w", pady=5, padx=15)
            CreateToolTip(cb, tip)
            self.memory_toggle_vars.append(var)


def main():
    try:
        app = CTRLBoostApp()
        app.mainloop()
    except Exception as e:
        print("An error occurred:")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()

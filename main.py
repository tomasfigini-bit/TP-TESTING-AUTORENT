import customtkinter as ctk
from modelo import Agencia
from ui import PageVehiculos, PageClientes, PageAlquilar, PageDevolver

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Colores personalizados
ACCENT   = "#E8890C"
ACCENT_H = "#F0A030"
DANGER   = "#C0392B"
DANGER_H = "#E74c3C"
SUCCESS  = "#27AE60"
BG       = "#1A1C1E"
PANEL    = "#242628"
CARD     = "#2D2F32"
FG       = "#E8E6E3"
FG2      = "#9A9890"
FG3      = "#6A6865"
ENTRY_BG = "#1E2022"

FONT_TITLE  = ("Georgia",   20, "bold")
FONT_BOLD   = ("Helvetica", 13, "bold")
FONT_LABEL  = ("Helvetica", 12)
FONT_SMALL  = ("Helvetica", 11)
FONT_MONO   = ("Courier",   12, "bold")
FONT_NAV    = ("Helvetica", 13, "bold")
FONT_MICRO  = ("Helvetica",  9, "bold")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AutoRent - Sistema de Alquiler de Vehiculos")
        self.geometry("980x660")
        self.minsize(860, 580)
        self.configure(fg_color=BG)
        self.resizable(True, True)

        self.agencia = Agencia()
        self._seed_demo()
        self._current = None
        self._build()

    def _seed_demo(self):
        self.agencia.registrar_vehiculo("ABC123",  "Toyota Corolla",   5000)
        self.agencia.registrar_vehiculo("XYZ789",  "Ford Ranger",      8500)
        self.agencia.registrar_vehiculo("MNP456",  "Volkswagen Vento", 6200)
        self.agencia.registrar_cliente("30123456", "Ana Garcia")
        self.agencia.registrar_cliente("25987654", "Martin Lopez")
        self.agencia.alquilar_vehiculo("XYZ789",  "30123456", 5)

    def _build(self):
        # Header
        header = ctk.CTkFrame(self, fg_color=PANEL, height=58, corner_radius=0)
        header.pack(side="top", fill="x")
        header.pack_propagate(False)

        ctk.CTkLabel(header, text="AutoRent", font=FONT_TITLE,
                     text_color=FG).pack(side="left", padx=(24, 10), pady=10)
        ctk.CTkLabel(header, text="Sistema de Alquiler de Vehiculos",
                     font=FONT_SMALL, text_color=FG3).pack(side="left", pady=20)

        # Separador naranja
        ctk.CTkFrame(self, fg_color=ACCENT, height=2, corner_radius=0).pack(
            side="top", fill="x")

        # Cuerpo
        body = ctk.CTkFrame(self, fg_color=BG, corner_radius=0)
        body.pack(side="top", fill="both", expand=True)

        # Sidebar
        sidebar = ctk.CTkFrame(body, fg_color=PANEL, width=175, corner_radius=0)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        ctk.CTkLabel(sidebar, text="MENU", font=FONT_MICRO,
                     text_color=FG3).pack(anchor="w", padx=16, pady=(20, 6))

        # Contenedor pÃ¡ginas
        self._content = ctk.CTkFrame(body, fg_color=BG, corner_radius=0)
        self._content.pack(side="left", fill="both", expand=True)

        # Instanciar pÃ¡ginas
        self._pages = {
            "vehiculos": PageVehiculos(self._content, self.agencia),
            "clientes":  PageClientes(self._content, self.agencia),
            "alquilar":  PageAlquilar(self._content, self.agencia),
            "devolver":  PageDevolver(self._content, self.agencia),
        }

        # Botones nav
        nav_items = [
            ("vehiculos", "  Vehiculos"),
            ("clientes",  "  Clientes"),
            ("alquilar",  "  Alquilar"),
            ("devolver",  "  Devolver"),
        ]
        self._nav_btns = {}
        for key, label in nav_items:
            b = ctk.CTkButton(
                sidebar,
                text=label,
                font=FONT_NAV,
                fg_color="transparent",
                text_color=FG2,
                hover_color="#2A2C2E",
                anchor="w",
                height=44,
                corner_radius=0,
                command=lambda k=key: self._show(k),
            )
            b.pack(fill="x")
            self._nav_btns[key] = b

        self._show("vehiculos")

    def _show(self, key):
        if self._current and self._current in self._pages:
            self._pages[self._current].pack_forget()

        self._current = key

        for k, b in self._nav_btns.items():
            if k == key:
                b.configure(fg_color=ACCENT, text_color="#111111",
                            hover_color=ACCENT_H)
            else:
                b.configure(fg_color="transparent", text_color=FG2,
                            hover_color="#2A2C2E")

        page = self._pages[key]
        page.pack(fill="both", expand=True)
        page.on_show()


if __name__ == "__main__":
    app = App()
    app.mainloop()

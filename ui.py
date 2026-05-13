import customtkinter as ctk
from componentes import Table, mk_field, mk_btn, section_title, msg_label, set_msg

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

class BasePage(ctk.CTkFrame):
    def __init__(self, master, agencia):
        super().__init__(master, fg_color=BG, corner_radius=0)
        self.agencia = agencia

    def on_show(self): pass


# ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
class PageVehiculos(BasePage):
    def __init__(self, master, agencia):
        super().__init__(master, agencia)
        self._build()

    def _build(self):
        # Formulario
        frm = ctk.CTkFrame(self, fg_color=CARD, corner_radius=10)
        frm.pack(fill="x", padx=20, pady=(20, 10))

        inner = ctk.CTkFrame(frm, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=16)

        section_title(inner, "Registrar vehiculo")

        self.v_pat = ctk.StringVar()
        self.v_mod = ctk.StringVar()
        self.v_tar = ctk.StringVar()

        row = ctk.CTkFrame(inner, fg_color="transparent")
        row.pack(fill="x", pady=4)
        mk_field(row, "PATENTE", self.v_pat, mono=True, w=140).pack(side="left", padx=(0, 16))
        mk_field(row, "MODELO",  self.v_mod, w=240).pack(side="left", padx=(0, 16))
        mk_field(row, "TARIFA / DIA ($)", self.v_tar, w=140).pack(side="left")

        bot = ctk.CTkFrame(inner, fg_color="transparent")
        bot.pack(anchor="w", pady=(14, 0))
        mk_btn(bot, "+ Registrar vehiculo", self._registrar).pack(side="left")

        self.lbl = msg_label(inner)

        # Tabla
        wrap = ctk.CTkFrame(self, fg_color="transparent")
        wrap.pack(fill="both", expand=True, padx=20, pady=4)
        ctk.CTkLabel(wrap, text="Flota registrada", font=FONT_SMALL,
                     text_color=FG2).pack(anchor="w", pady=(0, 4))
        self.table = Table(wrap, [
            ("PATENTE",    120),
            ("MODELO",     220),
            ("TARIFA/DIA", 130),
            ("ESTADO",     130),
        ])
        self.table.pack(fill="both", expand=True)
        self._reload()

    def _registrar(self):
        try:
            tarifa = float(self.v_tar.get())
        except ValueError:
            set_msg(self.lbl, "Tarifa invalida.", ok=False); return
        try:
            v = self.agencia.registrar_vehiculo(self.v_pat.get(), self.v_mod.get(), tarifa)
            self.v_pat.set(""); self.v_mod.set(""); self.v_tar.set("")
            set_msg(self.lbl, f"Vehiculo '{v.patente}' registrado correctamente.")
            self._reload()
        except ValueError as e:
            set_msg(self.lbl, str(e), ok=False)

    def _reload(self):
        rows = []
        for v in self.agencia.listar_vehiculos():
            est = "disponible" if v.esta_disponible() else "alquilado"
            rows.append((v.patente, v.modelo, f"${v.tarifa_diaria:,.2f}", est))
        self.table.load(rows)

    def on_show(self): self._reload()


# ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
class PageClientes(BasePage):
    def __init__(self, master, agencia):
        super().__init__(master, agencia)
        self._build()

    def _build(self):
        frm = ctk.CTkFrame(self, fg_color=CARD, corner_radius=10)
        frm.pack(fill="x", padx=20, pady=(20, 10))
        inner = ctk.CTkFrame(frm, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=16)

        section_title(inner, "Registrar cliente")

        self.v_dni = ctk.StringVar()
        self.v_nom = ctk.StringVar()

        row = ctk.CTkFrame(inner, fg_color="transparent")
        row.pack(fill="x", pady=4)
        mk_field(row, "DNI", self.v_dni, mono=True, w=160).pack(side="left", padx=(0, 16))
        mk_field(row, "NOMBRE COMPLETO", self.v_nom, w=300).pack(side="left")

        bot = ctk.CTkFrame(inner, fg_color="transparent")
        bot.pack(anchor="w", pady=(14, 0))
        mk_btn(bot, "+ Registrar cliente", self._registrar).pack(side="left")
        self.lbl = msg_label(inner)

        wrap = ctk.CTkFrame(self, fg_color="transparent")
        wrap.pack(fill="both", expand=True, padx=20, pady=4)
        ctk.CTkLabel(wrap, text="Clientes registrados", font=FONT_SMALL,
                     text_color=FG2).pack(anchor="w", pady=(0, 4))
        self.table = Table(wrap, [("DNI", 160), ("NOMBRE", 400)])
        self.table.pack(fill="both", expand=True)
        self._reload()

    def _registrar(self):
        try:
            c = self.agencia.registrar_cliente(self.v_dni.get(), self.v_nom.get())
            self.v_dni.set(""); self.v_nom.set("")
            set_msg(self.lbl, f"Cliente '{c.nombre}' registrado correctamente.")
            self._reload()
        except ValueError as e:
            set_msg(self.lbl, str(e), ok=False)

    def _reload(self):
        rows = [(c.dni, c.nombre) for c in self.agencia.listar_clientes()]
        self.table.load(rows)

    def on_show(self): self._reload()


# ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
class PageAlquilar(BasePage):
    def __init__(self, master, agencia):
        super().__init__(master, agencia)
        self._build()

    def _build(self):
        frm = ctk.CTkFrame(self, fg_color=CARD, corner_radius=10)
        frm.pack(fill="x", padx=20, pady=(20, 10))
        inner = ctk.CTkFrame(frm, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=16)

        section_title(inner, "Registrar alquiler")

        self.v_pat  = ctk.StringVar()
        self.v_dni  = ctk.StringVar()
        self.v_dias = ctk.StringVar()

        row = ctk.CTkFrame(inner, fg_color="transparent")
        row.pack(fill="x", pady=4)
        mk_field(row, "PATENTE", self.v_pat, mono=True, w=140).pack(side="left", padx=(0, 16))
        mk_field(row, "DNI CLIENTE", self.v_dni, mono=True, w=160).pack(side="left", padx=(0, 16))
        mk_field(row, "DIAS", self.v_dias, w=80).pack(side="left")

        ctk.CTkLabel(inner, text="Tip: hace clic en la tabla para autocompletar la patente",
                     font=FONT_SMALL, text_color=FG3).pack(anchor="w", pady=(8, 0))

        bot = ctk.CTkFrame(inner, fg_color="transparent")
        bot.pack(anchor="w", pady=(12, 0))
        mk_btn(bot, "Confirmar alquiler", self._alquilar).pack(side="left")
        self.lbl = msg_label(inner)

        wrap = ctk.CTkFrame(self, fg_color="transparent")
        wrap.pack(fill="both", expand=True, padx=20, pady=4)
        ctk.CTkLabel(wrap, text="Vehiculos disponibles  (clic para seleccionar)",
                     font=FONT_SMALL, text_color=FG2).pack(anchor="w", pady=(0, 4))
        self.table = Table(wrap, [
            ("PATENTE",    120),
            ("MODELO",     240),
            ("TARIFA/DIA", 130),
        ])
        self.table.bind_select(lambda row: self.v_pat.set(row[0]))
        self.table.pack(fill="both", expand=True)
        self._reload()

    def _alquilar(self):
        try:
            dias = int(self.v_dias.get())
        except ValueError:
            set_msg(self.lbl, "Dias invalidos (entero positivo).", ok=False); return
        try:
            a = self.agencia.alquilar_vehiculo(self.v_pat.get(), self.v_dni.get(), dias)
            self.v_pat.set(""); self.v_dni.set(""); self.v_dias.set("")
            set_msg(self.lbl,
                f"Alquiler OK  |  {a.vehiculo.patente}  |  {a.dias} dias  |  ${a.calcular_costo():,.2f} estimado")
            self._reload()
        except ValueError as e:
            set_msg(self.lbl, str(e), ok=False)

    def _reload(self):
        rows = [
            (v.patente, v.modelo, f"${v.tarifa_diaria:,.2f}")
            for v in self.agencia.listar_vehiculos() if v.esta_disponible()
        ]
        self.table.load(rows)

    def on_show(self): self._reload()


# ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
class PageDevolver(BasePage):
    def __init__(self, master, agencia):
        super().__init__(master, agencia)
        self._build()

    def _build(self):
        frm = ctk.CTkFrame(self, fg_color=CARD, corner_radius=10)
        frm.pack(fill="x", padx=20, pady=(20, 10))
        inner = ctk.CTkFrame(frm, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=16)

        section_title(inner, "Procesar devolucion")

        self.v_pat = ctk.StringVar()
        row = ctk.CTkFrame(inner, fg_color="transparent")
        row.pack(fill="x", pady=4)
        mk_field(row, "PATENTE A DEVOLVER", self.v_pat, mono=True, w=160).pack(side="left")

        ctk.CTkLabel(inner, text="Tip: hace clic en la tabla para seleccionar",
                     font=FONT_SMALL, text_color=FG3).pack(anchor="w", pady=(8, 0))

        bot = ctk.CTkFrame(inner, fg_color="transparent")
        bot.pack(anchor="w", pady=(12, 0))
        mk_btn(bot, "Procesar devolucion", self._devolver,
               color=DANGER, hover=DANGER_H).pack(side="left")
        self.lbl = msg_label(inner)

        wrap = ctk.CTkFrame(self, fg_color="transparent")
        wrap.pack(fill="both", expand=True, padx=20, pady=4)
        ctk.CTkLabel(wrap, text="Alquileres activos  (clic para seleccionar)",
                     font=FONT_SMALL, text_color=FG2).pack(anchor="w", pady=(0, 4))
        self.table = Table(wrap, [
            ("PATENTE",    110),
            ("MODELO",     180),
            ("CLIENTE",    160),
            ("DNI",        120),
            ("DIAS",        60),
            ("COSTO EST.", 120),
        ])
        self.table.bind_select(lambda row: self.v_pat.set(row[0]))
        self.table.pack(fill="both", expand=True)
        self._reload()

    def _devolver(self):
        try:
            alq, costo = self.agencia.devolver_vehiculo(self.v_pat.get())
            self.v_pat.set("")
            set_msg(self.lbl,
                f"Devolucion OK  |  {alq.vehiculo.patente}  |  {alq.cliente.nombre}  |  TOTAL: ${costo:,.2f}")
            self._reload()
        except ValueError as e:
            set_msg(self.lbl, str(e), ok=False)

    def _reload(self):
        rows = [
            (a.vehiculo.patente, a.vehiculo.modelo,
             a.cliente.nombre, a.cliente.dni,
             a.dias, f"${a.calcular_costo():,.2f}")
            for a in self.agencia.listar_alquileres()
        ]
        self.table.load(rows)

    def on_show(self): self._reload()
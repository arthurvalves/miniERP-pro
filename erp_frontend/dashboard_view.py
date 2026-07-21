import customtkinter as ctk
import sqlite3

from erp_backend.utils.db import get_connection
from erp_frontend.theme import COLORS, CORNERS, SPACING, TYPOGRAPHY, ThemeManager


class DashboardView(ctk.CTkFrame):
    def __init__(self, master, app_window, **kwargs):
        super().__init__(master, fg_color=COLORS["bg_dark"], **kwargs)
        self.app_window = app_window
        self.setup_ui()
        self.refresh()

    def setup_ui(self):
        """Configura layout do dashboard com header e cards"""
        # HEADER
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=SPACING["xl"], pady=(SPACING["xl"], SPACING["lg"]))

        title = ctk.CTkLabel(
            header,
            text="Dashboard",
            font=("Inter", 32, "bold"),
            text_color=COLORS["text_primary"],
        )
        title.pack(side="left")

        refresh_btn = ctk.CTkButton(
            header,
            text="🔄 Atualizar",
            width=140,
            height=40,
            font=("Inter", 12, "bold"),
            command=self.refresh,
            **ThemeManager.get_button_style("primary")
        )
        refresh_btn.pack(side="right")

        # CARDS FRAME (Grid 2x2)
        self.cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.cards_frame.pack(fill="both", expand=True, padx=SPACING["xl"], pady=SPACING["xl"])
        self.cards_frame.grid_columnconfigure((0, 1), weight=1)
        self.cards_frame.grid_rowconfigure((0, 1), weight=1)

        # Criar cards com novas cores e estilos
        self.metric_sales = self._create_card(
            self.cards_frame, 0, 0,
            "💰 Vendas Hoje",
            "R$ 0,00",
            COLORS["success"],
            PALETTES["success"]
        )
        self.metric_pending_nfe = self._create_card(
            self.cards_frame, 0, 1,
            "📄 NF-e Pendentes",
            "0",
            COLORS["info"],
            PALETTES["info"]
        )
        self.metric_low_stock = self._create_card(
            self.cards_frame, 1, 0,
            "📦 Estoque Baixo",
            "0 itens",
            COLORS["warning"],
            PALETTES["warning"]
        )
        self.metric_products = self._create_card(
            self.cards_frame, 1, 1,
            "🏷️ Produtos Cadastrados",
            "0",
            COLORS["primary"],
            PALETTES["primary"]
        )

    def _create_card(self, parent, row, column, label_text, value_text, accent_color, palette):
        """Cria card super customizado com gradiente e hover"""
        card = ctk.CTkFrame(
            parent,
            corner_radius=CORNERS["lg"],
            fg_color=palette["bg"],
            border_width=2,
            border_color=palette["border"]
        )
        card.grid(row=row, column=column, sticky="nsew", padx=SPACING["md"], pady=SPACING["md"])

        # Inner frame para padding
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=SPACING["lg"], pady=SPACING["lg"])

        # Label (Título)
        label = ctk.CTkLabel(
            inner,
            text=label_text,
            font=("Inter", 14, "bold"),
            text_color=palette["text"]
        )
        label.pack(anchor="w", pady=(0, SPACING["md"]))

        # Value (Número/Valor)
        value = ctk.CTkLabel(
            inner,
            text=value_text,
            font=("Inter", 36, "bold"),
            text_color=palette["fg"]
        )
        value.pack(anchor="w", fill="both", expand=True)

        # Barra de cor embaixo (visual accent)
        bar = ctk.CTkFrame(card, height=3, fg_color=palette["border"], corner_radius=2)
        bar.pack(fill="x", side="bottom")
        bar.pack_propagate(False)

        return value

    def refresh(self):
        """Atualiza dados do dashboard"""
        total_sales = 0
        pending_nfe = 0
        low_stock = 0
        total_products = 0

        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT COALESCE(SUM(total), 0) AS total_sales FROM sales WHERE date(data) = date('now')")
            total_sales = cur.fetchone()["total_sales"] or 0

            cur.execute("SELECT COUNT(*) AS pending FROM purchases WHERE chave_acesso IS NOT NULL")
            pending_nfe = cur.fetchone()["pending"] or 0

            cur.execute("SELECT COUNT(*) AS low_stock FROM products WHERE estoque_atual <= 5")
            low_stock = cur.fetchone()["low_stock"] or 0

            cur.execute("SELECT COUNT(*) AS total_products FROM products")
            total_products = cur.fetchone()["total_products"] or 0
        except sqlite3.OperationalError:
            # O schema ainda pode estar sendo inicializado na primeira execução.
            pass
        finally:
            conn.close()

        self.metric_sales.configure(text=f"R$ {total_sales:.2f}")
        self.metric_pending_nfe.configure(text=str(pending_nfe))
        self.metric_low_stock.configure(text=f"{low_stock} itens")
        self.metric_products.configure(text=str(total_products))


# Importar paletas de cores
PALETTES = {
    "success": {
        "bg": "#064E3B",
        "fg": "#6EE7B7",
        "border": "#10B981",
        "text": "#FFFFFF",
    },
    "info": {
        "bg": "#0C2340",
        "fg": "#93C5FD",
        "border": "#3B82F6",
        "text": "#FFFFFF",
    },
    "warning": {
        "bg": "#78350F",
        "fg": "#FBBF24",
        "border": "#F59E0B",
        "text": "#FFFFFF",
    },
    "primary": {
        "bg": "#451A03",
        "fg": "#FDB913",
        "border": "#F59E0B",
        "text": "#FFFFFF",
    },
}

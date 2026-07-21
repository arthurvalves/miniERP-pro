import customtkinter as ctk
from erp_frontend.dashboard_view import DashboardView
from erp_frontend.pdv_view import PDVView
from erp_frontend.nfe_view import NFeView
from erp_frontend.products_view import ProductsView
from erp_frontend.services_view import ServicesView
from erp_frontend.printer_view import PrinterView
from erp_frontend.os_view import OSView
from erp_frontend.quotes_view import QuotesView
from erp_frontend.history_view import HistoryView
from erp_frontend.accounts_receivable_view import AccountsReceivableView
from erp_frontend.schedule_view import ScheduleView
from erp_frontend.maintenance_alerts_view import MaintenanceAlertsView
from erp_frontend.reports_view import ReportsView
from erp_frontend.session import get_current_user
from erp_frontend.theme import COLORS, CORNERS, SPACING, ThemeManager

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("miniERP Pro - Autopeças & Oficina")
        self.geometry("1400x900")
        self.minsize(1200, 700)
        self.current_user = get_current_user()
        self.current_view = None
        self.active_button = None
        
        # Configurar fundo
        self.configure(fg_color=COLORS["bg_dark"])
        
        self.setup_main_ui()
        self.show_view(DashboardView)

    def setup_main_ui(self):
        """Configura layout principal: navbar + sidebar + content"""
        # NAVBAR (Topo)
        self.navbar = ctk.CTkFrame(
            self, 
            height=70,
            fg_color=COLORS["bg_secondary"],
            border_width=1,
            border_color=COLORS["border"]
        )
        self.navbar.pack(side="top", fill="x")
        self.navbar.pack_propagate(False)
        
        # Logo + Nome da app
        logo_frame = ctk.CTkFrame(self.navbar, fg_color="transparent")
        logo_frame.pack(side="left", padx=SPACING["lg"], pady=SPACING["md"])
        
        logo_label = ctk.CTkLabel(
            logo_frame,
            text="⚙️",
            font=("Inter", 32, "bold")
        )
        logo_label.pack(side="left", padx=(0, SPACING["md"]))
        
        title_label = ctk.CTkLabel(
            logo_frame,
            text="miniERP Pro",
            font=("Inter", 20, "bold"),
            text_color=COLORS["primary"]
        )
        title_label.pack(side="left")
        
        # User info (lado direito da navbar)
        user_frame = ctk.CTkFrame(self.navbar, fg_color="transparent")
        user_frame.pack(side="right", padx=SPACING["lg"], pady=SPACING["md"])
        
        user_label = ctk.CTkLabel(
            user_frame,
            text=f"👤 {self.current_user or 'Usuário'}",
            font=("Inter", 12),
            text_color=COLORS["text_secondary"]
        )
        user_label.pack()
        
        # Container principal (sidebar + content)
        main_container = ctk.CTkFrame(self, fg_color=COLORS["bg_dark"])
        main_container.pack(fill="both", expand=True)
        main_container.pack_propagate(False)
        
        # SIDEBAR (Esquerda)
        self.sidebar = ctk.CTkFrame(
            main_container,
            width=280,
            fg_color=COLORS["bg_secondary"],
            border_width=1,
            border_color=COLORS["border"],
            corner_radius=0
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        
        # Menu items na sidebar
        self._create_sidebar_menu()
        
        # CONTENT AREA (Direita - principal)
        self.content_frame = ctk.CTkFrame(
            main_container,
            fg_color=COLORS["bg_dark"],
            corner_radius=0
        )
        self.content_frame.pack(side="right", fill="both", expand=True)

    def _create_sidebar_menu(self):
        """Cria menu estruturado na sidebar"""
        scrollable_frame = ctk.CTkScrollableFrame(
            self.sidebar,
            fg_color="transparent"
        )
        scrollable_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Menu items com categorias
        menu_structure = [
            ("🏠 Dashboard", DashboardView),
            ("━" * 35, None),
            ("📊 OPERACIONAL", None),
            ("  💰 PDV (Ponto de Venda)", PDVView),
            ("  📋 Orçamentos", QuotesView),
            ("  🔧 Ordens de Serviço", OSView),
            ("  📅 Agenda", ScheduleView),
            ("━" * 35, None),
            ("📦 CADASTROS", None),
            ("  🛍️ Produtos", ProductsView),
            ("  🔩 Serviços", ServicesView),
            ("━" * 35, None),
            ("📈 ANÁLISE", None),
            ("  🚗 Histórico de Veículos", HistoryView),
            ("  ⚠️ Alertas de Manutenção", MaintenanceAlertsView),
            ("  📊 Relatórios", ReportsView),
            ("━" * 35, None),
            ("💳 FINANCEIRO", None),
            ("  💵 Contas a Receber", AccountsReceivableView),
            ("━" * 35, None),
            ("⚙️ ADMINISTRATIVO", None),
            ("  📄 Importar NF-e", NFeView),
            ("  🖨️ Impressoras", PrinterView),
        ]
        
        for label, view_class in menu_structure:
            if view_class is None:
                # Separador ou categoria
                if label.startswith("━"):
                    sep = ctk.CTkFrame(scrollable_frame, height=1, fg_color=COLORS["border"])
                    sep.pack(fill="x", padx=SPACING["md"], pady=SPACING["md"])
                else:
                    # Categoria
                    cat_label = ctk.CTkLabel(
                        scrollable_frame,
                        text=label,
                        font=("Inter", 11, "bold"),
                        text_color=COLORS["primary"],
                        anchor="w"
                    )
                    cat_label.pack(fill="x", padx=SPACING["lg"], pady=(SPACING["lg"], SPACING["sm"]))
            else:
                # Menu item clicável
                btn = ctk.CTkButton(
                    scrollable_frame,
                    text=label,
                    font=("Inter", 13),
                    height=40,
                    corner_radius=CORNERS["sm"],
                    fg_color="transparent",
                    text_color=COLORS["text_primary"],
                    hover_color=COLORS["bg_tertiary"],
                    anchor="w",
                    command=lambda v=view_class: self._on_menu_click(btn, v)
                )
                btn.pack(fill="x", padx=SPACING["md"], pady=SPACING["xs"])

    def _on_menu_click(self, button, view_class):
        """Callback ao clicar em item do menu"""
        # Remover highlight do botão anterior
        if self.active_button:
            self.active_button.configure(
                fg_color="transparent",
                text_color=COLORS["text_primary"]
            )
        
        # Destacar novo botão
        button.configure(
            fg_color=COLORS["bg_tertiary"],
            text_color=COLORS["primary"]
        )
        self.active_button = button
        
        # Mostrar view
        self.show_view(view_class)

    def show_view(self, view_class):
        """Substitui conteúdo atual pela nova view"""
        if self.current_view:
            self.current_view.destroy()
        self.current_view = view_class(self.content_frame, self)
        self.current_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainWindow()
    # Tries to maximize on Windows
    try:
        app.state('zoomed')
    except:
        pass
    app.mainloop()

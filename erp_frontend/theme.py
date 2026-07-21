"""
Sistema de temas centralizado para miniERP
Design: Dark Mode + Amarelo (marca) + Cinzas neutros
Foco: Velocidade operacional com contrastes altos
"""

# Paleta de cores - exatamente 5 cores conforme guidelines
COLORS = {
    # Primário (Amarelo - marca)
    "primary": "#FDB913",
    "primary_dark": "#E5A600",
    "primary_hover": "#FFCC00",
    
    # Neutros
    "bg_dark": "#0F1419",        # Fundo principal (muito escuro)
    "bg_secondary": "#1A1F28",   # Fundo secundário
    "bg_tertiary": "#232A35",    # Fundo terciário (cards, elementos)
    
    # Texto
    "text_primary": "#FFFFFF",   # Texto principal
    "text_secondary": "#B0B8C5", # Texto secundário
    "text_tertiary": "#7A8392",  # Texto terciário
    
    # Estados
    "success": "#10B981",
    "warning": "#F59E0B",
    "error": "#EF4444",
    "info": "#3B82F6",
    
    # Bordas e divisores
    "border": "#2F3A47",
    "border_light": "#3F4A57",
}

# Spacing (Escala de espaçamento)
SPACING = {
    "xs": 4,
    "sm": 8,
    "md": 12,
    "lg": 16,
    "xl": 24,
    "2xl": 32,
}

# Typography (Fontes e tamanhos)
TYPOGRAPHY = {
    "font_family": "Inter",
    "font_mono": "Courier New",
    "size_xs": 10,
    "size_sm": 12,
    "size_base": 14,
    "size_lg": 16,
    "size_xl": 18,
    "size_2xl": 20,
    "size_3xl": 24,
    "size_4xl": 32,
}

# Corners (Raios de borda)
CORNERS = {
    "sm": 4,
    "md": 8,
    "lg": 12,
    "xl": 16,
    "full": 9999,
}

# Shadows
SHADOWS = {
    "sm": "0 1px 2px rgba(0, 0, 0, 0.05)",
    "md": "0 4px 6px rgba(0, 0, 0, 0.1)",
    "lg": "0 10px 15px rgba(0, 0, 0, 0.2)",
    "xl": "0 20px 25px rgba(0, 0, 0, 0.3)",
}

# Paletas por contexto
PALETTES = {
    "danger": {
        "bg": "#7F1D1D",
        "fg": "#FCA5A5",
        "border": "#DC2626",
        "text": "#FFFFFF",
    },
    "success": {
        "bg": "#064E3B",
        "fg": "#6EE7B7",
        "border": "#10B981",
        "text": "#FFFFFF",
    },
    "warning": {
        "bg": "#78350F",
        "fg": "#FBBF24",
        "border": "#F59E0B",
        "text": "#FFFFFF",
    },
    "info": {
        "bg": "#0C2340",
        "fg": "#93C5FD",
        "border": "#3B82F6",
        "text": "#FFFFFF",
    },
    "primary": {
        "bg": "#451A03",
        "fg": "#FDB913",
        "border": "#F59E0B",
        "text": "#FFFFFF",
    },
}


class ThemeManager:
    """Gerenciador centralizado de temas"""
    
    @staticmethod
    def get_bg_color(level: str = "primary") -> str:
        """Retorna cor de fundo por nível (primary, secondary, tertiary)"""
        return COLORS[f"bg_{level}"] if level != "primary" else COLORS["bg_dark"]
    
    @staticmethod
    def get_text_color(level: str = "primary") -> str:
        """Retorna cor de texto por nível (primary, secondary, tertiary)"""
        return COLORS[f"text_{level}"] if level in ["primary", "secondary", "tertiary"] else COLORS["text_primary"]
    
    @staticmethod
    def get_button_style(variant: str = "primary") -> dict:
        """Retorna estilos de botão por variante"""
        styles = {
            "primary": {
                "fg_color": COLORS["primary"],
                "hover_color": COLORS["primary_hover"],
                "text_color": "#000000",
                "border_width": 0,
            },
            "secondary": {
                "fg_color": COLORS["bg_tertiary"],
                "hover_color": COLORS["border_light"],
                "text_color": COLORS["text_primary"],
                "border_width": 1,
                "border_color": COLORS["border_light"],
            },
            "danger": {
                "fg_color": PALETTES["danger"]["bg"],
                "hover_color": PALETTES["danger"]["border"],
                "text_color": PALETTES["danger"]["text"],
                "border_width": 0,
            },
            "success": {
                "fg_color": PALETTES["success"]["bg"],
                "hover_color": PALETTES["success"]["border"],
                "text_color": PALETTES["success"]["text"],
                "border_width": 0,
            },
        }
        return styles.get(variant, styles["primary"])
    
    @staticmethod
    def get_card_style() -> dict:
        """Retorna estilos de card"""
        return {
            "fg_color": COLORS["bg_tertiary"],
            "border_color": COLORS["border"],
            "border_width": 1,
            "corner_radius": CORNERS["md"],
        }
    
    @staticmethod
    def get_input_style() -> dict:
        """Retorna estilos de input"""
        return {
            "fg_color": COLORS["bg_secondary"],
            "border_color": COLORS["border"],
            "border_width": 1,
            "text_color": COLORS["text_primary"],
            "placeholder_text_color": COLORS["text_tertiary"],
            "corner_radius": CORNERS["sm"],
        }

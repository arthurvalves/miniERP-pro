# 🎨 miniERP Pro - Super Customização Visual

> **Redesign completo do frontend Tkinter com tema dark mode premium + amarelo corporativo**

## ✨ O Que Foi Feito

Transformação visual completa focada em **velocidade operacional** para um sistema ERP/PDV de autopeças e oficina mecânica.

### 🎯 Mudanças Principais

1. **Sistema de Temas Centralizado** (`theme.py`)
   - Paleta de 5 cores (guidelines design)
   - Componentes reutilizáveis
   - Espaçamento e tipografia padronizados

2. **Nova Arquitetura de Interface** (`main_window.py`)
   - Layout 3-camadas: Navbar + Sidebar + Content
   - Menu categorizado com ícones
   - Highlight ativo em itens selecionados

3. **Dashboard Premium** (`dashboard_view.py`)
   - 4 cards com paletas de contexto
   - Cores vibrantes para cada métrica
   - Emojis para identificação rápida

## 📁 Arquivos Importantes

### Implementação
```
erp_frontend/
├── theme.py                    # Sistema temático centralizado (177 linhas)
├── main_window.py              # Interface principal refatorada (190 linhas)
└── dashboard_view.py           # Dashboard customizado (160 linhas)
```

### Documentação
```
├── DESIGN_UPDATES.md          # Visão geral das mudanças
├── VISUAL_DESIGN_GUIDE.md     # Especificações detalhadas (329 linhas)
├── CHANGES_SUMMARY.md         # Resumo técnico de mudanças
├── MOCKUP_VISUAL.txt          # Mockup ASCII art com cores
└── README_DESIGN.md           # Este arquivo
```

## 🎨 Paleta de Cores

### Core (5 cores)
| Nome | Cor | Uso |
|------|-----|-----|
| Primary | #FDB913 | Amarelo (marca) |
| BG Dark | #0F1419 | Fundo principal |
| BG Secondary | #1A1F28 | Navbar/Sidebar |
| BG Tertiary | #232A35 | Cards |
| Text Primary | #FFFFFF | Texto principal |

### Contexto
| Tipo | BG | Border | Value | Uso |
|------|-----|--------|-------|-----|
| Success | #064E3B | #10B981 | #6EE7B7 | Vendas |
| Info | #0C2340 | #3B82F6 | #93C5FD | NF-e |
| Warning | #78350F | #F59E0B | #FBBF24 | Estoque |
| Primary | #451A03 | #F59E0B | #FDB913 | Marca |

## 🚀 Como Usar

### Importar o Sistema de Temas

```python
from erp_frontend.theme import COLORS, ThemeManager

# Opção 1: Usar estilos prontos
button = ctk.CTkButton(
    parent,
    text="Salvar",
    **ThemeManager.get_button_style("primary")
)

# Opção 2: Acessar cores direto
label.configure(text_color=COLORS["primary"])
frame.configure(fg_color=COLORS["bg_tertiary"])

# Opção 3: Usar em componentes customizados
card = ctk.CTkFrame(
    parent,
    **ThemeManager.get_card_style()
)
```

### Migrar Um View

```python
from erp_frontend.theme import COLORS, ThemeManager

class MinhaView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        # 1. Usar fundo do tema
        super().__init__(master, fg_color=COLORS["bg_dark"], **kwargs)
        
        # 2. Usar spacing do tema
        self.pack(padx=SPACING["xl"], pady=SPACING["xl"])
        
        # 3. Usar tipografia do tema
        title = ctk.CTkLabel(
            self,
            text="Título",
            font=("Inter", 32, "bold"),  # Ou usar TYPOGRAPHY
            text_color=COLORS["text_primary"]
        )
```

## 📊 Layout Principal

```
┌──────────────────────────────────────┐
│  Navbar 70px (Dark)                  │
├────────┬────────────────────────────┤
│Sidebar │       Content Area          │
│ 280px  │       (Responsivo)          │
│(Dark)  │                             │
│        │  - Cards em grid 2x2        │
│        │  - Tabelas                  │
│        │  - Formulários              │
│        │  - Modais                   │
└────────┴────────────────────────────┘
```

## 🔧 Tecnologias

- **Framework**: CustomTkinter 5.2.2
- **Tipografia**: Inter (moderna) + Courier (mono)
- **Cores**: Tema centralizado em `theme.py`
- **Python**: 3.9+

## ✅ Status

| Item | Status |
|------|--------|
| Sistema temático | ✅ Implementado |
| Main window | ✅ Refatorada |
| Dashboard | ✅ Customizado |
| Documentação | ✅ Completa |
| Outros 15+ views | ⏳ Pendente |
| Animações | ⏳ Sugerido |
| Modo light | ⏳ Sugerido |

## 🎯 Próximos Passos

1. **Curto Prazo** (1-2 semanas)
   - [ ] Atualizar `pdv_view.py` com novo tema
   - [ ] Atualizar `os_view.py` com novo tema
   - [ ] Atualizar componentes (`table.py`, `scanner_input.py`)

2. **Médio Prazo** (2-4 semanas)
   - [ ] Migrar todos os 15+ views
   - [ ] Adicionar animações hover
   - [ ] Implementar modo light

3. **Longo Prazo** (1-2 meses)
   - [ ] Componentes reutilizáveis customizados
   - [ ] Temas personalizáveis por usuário
   - [ ] Dark mode + Light mode toggle

## 📚 Documentação

Para mais detalhes, consulte:

- **[DESIGN_UPDATES.md](DESIGN_UPDATES.md)** - Visão geral e mudanças
- **[VISUAL_DESIGN_GUIDE.md](VISUAL_DESIGN_GUIDE.md)** - Especificações técnicas (329 linhas)
- **[CHANGES_SUMMARY.md](CHANGES_SUMMARY.md)** - Resumo de mudanças por arquivo
- **[MOCKUP_VISUAL.txt](MOCKUP_VISUAL.txt)** - Mockup ASCII art com cores

## 🎬 Commits

```bash
# Ver histórico de commits
git log --oneline | head -5

# Commits desta customização:
# ac5dfad - Adicionado mockup visual ASCII art
# 91b2df1 - Documentação completa da super customização
# 0b7b45c - Super customização visual - Dark Mode + Amarelo
```

## 🤝 Como Contribuir

Se quiser adicionar mais views com este design:

1. Copie o padrão de `dashboard_view.py`
2. Importe `from erp_frontend.theme import ...`
3. Use `ThemeManager.get_*_style()` para componentes
4. Mantenha a paleta de cores consistente

## 📞 Suporte

Dúvidas sobre o sistema temático?

1. Consulte `theme.py` para ver todas as opções
2. Veja os exemplos em `dashboard_view.py`
3. Leia `VISUAL_DESIGN_GUIDE.md` para detalhes

## 📄 Licença

Mesmo que o projeto original

---

**Data**: 21/07/2026  
**Versão**: 1.0  
**Status**: ✅ Pronto para uso  
**Próxima Revisão**: 04/08/2026

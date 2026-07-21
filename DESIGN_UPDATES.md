# 🎨 Super Customização Visual - miniERP Pro

## Visão Geral
Redesign completo do frontend Tkinter com tema **dark mode premium + amarelo corporativo**, focado em **velocidade operacional**.

## 🎯 Mudanças Implementadas

### 1️⃣ Sistema de Temas Centralizado (`theme.py`)
- **Paleta de 5 cores** (guidelines): primário amarelo, neutros (dark, secondary, tertiary), texto branco/cinzento
- **Espaçamento padronizado**: xs, sm, md, lg, xl, 2xl
- **Tipografia consistente**: Inter (corpo), Courier (mono)
- **Corners e sombras** pré-configurados
- **ThemeManager** com métodos reutilizáveis para buttons, cards, inputs

### 2️⃣ Nova Arquitetura de Interface (`main_window.py`)
#### Layout de 3 camadas:
- **Navbar (Topo)**: Logo + título + info de usuário | Altura: 70px
- **Sidebar (Esquerda)**: Menu categorizado com ícones e emojis | Largura: 280px
- **Content Area (Direita)**: Conteúdo principal responsivo

#### Estrutura do Menu Sidebar:
```
🏠 Dashboard
━━━━━━━━━━━━
📊 OPERACIONAL
  💰 PDV (Ponto de Venda)
  📋 Orçamentos
  🔧 Ordens de Serviço
  📅 Agenda
━━━━━━━━━━━━
📦 CADASTROS
  🛍️ Produtos
  🔩 Serviços
━━━━━━━━━━━━
[... mais seções]
```

#### Recursos:
- ✅ Highlight ativo em menu item clicado
- ✅ Scrollable para muitos itens
- ✅ Cores da marca em títulos de categoria
- ✅ Separadores visuais

### 3️⃣ Dashboard Premium (`dashboard_view.py`)
#### 4 Cards com cores personalizadas:
1. **💰 Vendas Hoje** - Verde (success)
   - BG: #064E3B | Borda: #10B981 | Texto: #6EE7B7

2. **📄 NF-e Pendentes** - Azul (info)
   - BG: #0C2340 | Borda: #3B82F6 | Texto: #93C5FD

3. **📦 Estoque Baixo** - Laranja (warning)
   - BG: #78350F | Borda: #F59E0B | Texto: #FBBF24

4. **🏷️ Produtos Cadastrados** - Amarelo/Marrom (primary)
   - BG: #451A03 | Borda: #F59E0B | Texto: #FDB913

#### Design do Card:
- Corner radius: 12px
- Border: 2px + cor da paleta
- Padding: 16px (xl)
- Tipografia: Inter bold
- Barra colorida no rodapé

## 🎨 Paleta de Cores

### Core Colors
| Nome | Cor | Uso |
|------|-----|-----|
| Primary | #FDB913 | Amarelo (marca) |
| BG Dark | #0F1419 | Fundo principal |
| BG Secondary | #1A1F28 | Navbar/Sidebar |
| BG Tertiary | #232A35 | Cards/Elementos |
| Text Primary | #FFFFFF | Texto principal |

### Contexto (Paletas)
- **Success**: Verde forte (#10B981) para métricas positivas
- **Warning**: Laranja (#F59E0B) para alertas
- **Error**: Vermelho (#EF4444) para erros
- **Info**: Azul (#3B82F6) para informações

## 📊 Tipografia

- **Heading**: Inter Bold (32px para títulos principais)
- **Labels**: Inter Bold (14px)
- **Values**: Inter Bold (36px)
- **Body**: Inter Regular (13-14px)

## 🚀 Performance & Velocidade

✅ **Otimizado para operadores rápidos:**
- Menu categorizado = menos cliques
- Atalhos via emojis = identificação instant
- Cards grandes = legibilidade rápida
- Cores vibrantes = visual feedback claro

## 📝 Próximos Passos Sugeridos

1. Aplicar theme.py a **todos os views** (pdv_view, os_view, etc)
2. Criar componentes reutilizáveis (Button, Card, Input customizados)
3. Adicionar **animações suaves** em transições
4. Implementar **atalhos de teclado** (F1=Dashboard, F2=PDV, etc)
5. Adicionar **modo claro** como alternativa

## 🔧 Como Usar o Sistema de Temas

```python
from erp_frontend.theme import COLORS, ThemeManager

# Usar cores
button = ctk.CTkButton(
    parent,
    text="Comprar",
    **ThemeManager.get_button_style("primary")  # ✅ Estilo pronto
)

# Criar card
card = ctk.CTkFrame(
    parent,
    **ThemeManager.get_card_style()  # ✅ Estilos padronizados
)

# Acessar cores direto
label.configure(text_color=COLORS["primary"])
frame.configure(fg_color=COLORS["bg_tertiary"])
```

---

**Data**: 21/07/2026  
**Versão**: 1.0  
**Status**: ✅ Implementado

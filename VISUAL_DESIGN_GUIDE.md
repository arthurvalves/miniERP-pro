# 🎨 Guia Visual - miniERP Pro Design System

## 📐 Layout Principal

```
┌─────────────────────────────────────────────────────────────┐
│  ⚙️ miniERP Pro      [Navbar - 70px, Dark]    👤 Usuário    │
├──────────────┬───────────────────────────────────────────────┤
│              │                                               │
│  🏠 MENU     │  [CONTENT AREA - Responsivo]                │
│  ────────    │                                               │
│  📊 Seção 1  │  - Cards com métricas                       │
│    Item 1    │  - Tabelas de dados                         │
│    Item 2    │  - Formulários                              │
│              │  - Modais                                    │
│  📦 Seção 2  │                                               │
│    Item 3    │  Fundo: #0F1419                             │
│    Item 4    │  Padding: 24px (xl)                         │
│              │  Responsivo: expande/contrai                 │
│  [Sidebar]   │  [Conteúdo]                                 │
│  280px       │  width: auto                                │
│  Dark        │                                               │
└──────────────┴───────────────────────────────────────────────┘
```

## 🎯 Componentes Principais

### 1. Navbar
```
HEIGHT: 70px
BG: #1A1F28
BORDER-BOTTOM: 1px #2F3A47

┌──────────────────────────────────────────────────────────┐
│ ⚙️ miniERP Pro     |  Logo: 32px, Bold, Amarelo         │
│                   |  Título: 20px, Bold, Amarelo        │
│                   |  Separator: |                         │
│                                           👤 User Info  │
│                                           12px, Cinzento│
└──────────────────────────────────────────────────────────┘

Padding: 16px (lg) horizontal, 12px (md) vertical
```

### 2. Sidebar
```
WIDTH: 280px
BG: #1A1F28
BORDER-RIGHT: 1px #2F3A47
SCROLLABLE: Sim

ESTRUTURA:
🏠 Dashboard         [altura: 40px]
━━━━━━━━━━━━━━━━    [separador visual]
📊 OPERACIONAL       [título categoria: amarelo, 11px bold]
  💰 PDV (PV)        [item: 40px, hover bg]
  📋 Orçamentos
  🔧 OS
  📅 Agenda
━━━━━━━━━━━━━━━━
[... mais seções]

ITEM STYLE:
- Height: 40px
- Padding: 8px (xs) y, 16px (lg) x
- Font: Inter 13px
- Color: #B0B8C5 (text_secondary)
- Hover: #232A35 (bg_tertiary)
- Active: Amarelo #FDB913 + #232A35 bg

CATEGORIA STYLE:
- Font: Inter 11px Bold
- Color: #FDB913 (primary)
- Padding: 16px (lg) x, 8px (sm/md) y
- Margin-top: 16px (lg)
```

### 3. Dashboard Cards
```
┌─────────────────────┬─────────────────────┐
│  💰 Card 1 (2x2)    │  📄 Card 2          │
├─────────────────────┼─────────────────────┤
│  📦 Card 3          │  🏷️ Card 4         │
└─────────────────────┴─────────────────────┘

CARD DIMENSIONS:
- Cada card ocupa 50% do container (weight=1 grid)
- Padding: 12px (md) entre cards
- Min-height: ~200px

CARD INTERNO:
┌──────────────────────────────────────────┐
│ 💰 Vendas Hoje                 │ label   │ ← 14px bold
│                                │         │
│ R$ 5.230,45                    │ value   │ ← 36px bold
│                                │         │
│ [Barra colorida: 3px height]   │ accent  │
└──────────────────────────────────────────┘

Padding: 16px (xl) interno
Border-radius: 12px (lg)
Border: 2px + cor da paleta

CARD COLORS (Paletas de Contexto):
1. Vendas - Success
   BG: #064E3B (dark green)
   BORDER: #10B981
   TEXT: #FFFFFF
   VALUE: #6EE7B7 (light green)

2. NF-e - Info
   BG: #0C2340 (dark blue)
   BORDER: #3B82F6
   TEXT: #FFFFFF
   VALUE: #93C5FD (light blue)

3. Estoque - Warning
   BG: #78350F (dark orange)
   BORDER: #F59E0B
   TEXT: #FFFFFF
   VALUE: #FBBF24 (light orange)

4. Produtos - Primary
   BG: #451A03 (dark brown/yellow)
   BORDER: #F59E0B
   TEXT: #FFFFFF
   VALUE: #FDB913 (brand yellow)
```

## 🎨 Paleta de Cores

### Core (5 cores)
```
┌─────────────────────────────────────────┐
│ 🟡 PRIMARY                              │ #FDB913
│ Amarelo corporativo - marca             │
│ Uso: Botões principais, destaque        │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ ⬛ BG DARK                              │ #0F1419
│ Fundo principal (muito escuro)          │
│ Uso: Main background                    │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ 🔲 BG SECONDARY                        │ #1A1F28
│ Fundo secundário (sidebar, navbar)      │
│ Uso: Containers secundários             │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ ◻️ BG TERTIARY                         │ #232A35
│ Fundo terciário (cards, elementos)      │
│ Uso: Elementos dentro de cards          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ ⚪ TEXT PRIMARY                         │ #FFFFFF
│ Texto principal (máximo contraste)      │
│ Uso: Textos principais                  │
└─────────────────────────────────────────┘
```

### Contexto (Status/Type)
```
SUCCESS ✓
├─ BG: #064E3B (Dark Green)
├─ TEXT: #FFFFFF
├─ BORDER: #10B981
└─ VALUE: #6EE7B7

WARNING ⚠
├─ BG: #78350F (Dark Orange)
├─ TEXT: #FFFFFF
├─ BORDER: #F59E0B
└─ VALUE: #FBBF24

ERROR ✗
├─ BG: #7F1D1D (Dark Red)
├─ TEXT: #FFFFFF
├─ BORDER: #DC2626
└─ VALUE: #FCA5A5

INFO ℹ
├─ BG: #0C2340 (Dark Blue)
├─ TEXT: #FFFFFF
├─ BORDER: #3B82F6
└─ VALUE: #93C5FD
```

## 📝 Tipografia

```
HEADINGS:
- Título principal (Dashboard): 32px, Bold, Inter, Branco
- Título seção: 24px, Bold, Inter, Branco
- Título categoria: 11px, Bold, Inter, Amarelo

BODY:
- Padrão: 14px, Regular, Inter, Branco
- Pequeno: 12px, Regular, Inter, Cinzento
- Label: 14px, Bold, Inter, Cinzento

VALUES:
- Grande (cards): 36px, Bold, Inter, Colorido
- Médio: 20px, Bold, Inter, Colorido

MONO:
- Código/IDs: Courier New, 12px
```

## ⏐ Espaçamento

```
XS: 4px   (gaps mínimos)
SM: 8px   (gaps pequenos)
MD: 12px  (gaps padrão)
LG: 16px  (gaps grandes)
XL: 24px  (gaps container)
2XL: 32px (gaps seções)
```

## 🔘 Componentes

### Botão Primary
```
┌─────────────────┐
│   COMPRAR       │ ← 12px Bold, Preto
│                 │ ← height: 40px
└─────────────────┘
BG: #FDB913 (amarelo)
HOVER: #FFCC00 (amarelo claro)
Border-radius: 8px (md)
Font: Inter 12px Bold
```

### Botão Secondary
```
┌─────────────────────────────────┐
│    CANCELAR                     │
└─────────────────────────────────┘
BG: #232A35 (tertiary)
BORDER: 1px #3F4A57 (light border)
HOVER: #3F4A57
Font: Inter 12px
Color: Branco
```

### Input
```
┌───────────────────────────┐
│ Digite aqui...            │ ← placeholder: cinzento
│ Texto digitado            │ ← text: branco
└───────────────────────────┘
BG: #1A1F28 (secondary)
BORDER: 1px #2F3A47
BORDER-RADIUS: 4px (sm)
Focus: BORDER #FDB913 2px
Padding: 12px (md)
```

## 🎬 Animações (Sugeridas)

```
HOVER EFFECTS:
- Sidebar item: fade to #232A35 (50ms)
- Button: fade to hover_color (100ms)
- Card: subtle scale 1.02 (150ms)

TRANSITIONS:
- Color changes: 150ms
- Size changes: 200ms
- Position changes: 300ms

EASING: ease-out (suave)
```

## 📱 Responsividade

```
DESKTOP (>1200px):
- Sidebar: 280px fixa
- Content: auto (expand)
- Navbar: altura fixa 70px

TABLET (800-1200px):
- Sidebar: 280px (pode ficar colapsável)
- Content: auto
- Cards: 2 colunas → 1 coluna em 768px

MOBILE (<800px):
- Sidebar: colapsável/drawer
- Content: full width
- Cards: 1 coluna
- Navbar: menor (60px)

[Nota: Tkinter tem limitações em responsividade,
mas respeitar essas proporções é importante]
```

## 🎯 Princípios de Design

1. **Velocidade Operacional**
   - Ícones e cores vibrantes para reconhecimento rápido
   - Menu categorizado = menos cliques
   - Tipografia grande = legibilidade rápida

2. **Contraste Alto**
   - Dark mode premium reduz fadiga
   - Cores vibrantes destacam dados importantes
   - Branco puro (#FFFFFF) em dark (#0F1419)

3. **Consistência**
   - Sistema de temas centralizado
   - Paletas pré-definidas
   - Spacing e corners padronizados

4. **Acessibilidade**
   - Cores com contraste WCAG AA+
   - Ícones + texto (não apenas ícones)
   - Tamanhos de fonte legíveis (mín. 12px)

---

**Versão**: 1.0  
**Data**: 21/07/2026  
**Mantido por**: Theme System  

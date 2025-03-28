# Especificação de Requisitos do App SaneAgile

## 1. Visão Geral
SaneAgile é um aplicativo móvel desenvolvido para cálculo de erro em medições, utilizando Python e framework Django.

## 2. Especificações Técnicas
- Versão Python: 3.13.1 ou superior
- Versão Django: 5.1.7 ou superior
- Esquema de Cores:
  - Primária: #f78f34
  - Secundária: #1baaa1
  - Fundo do Menu: #263544

## 3. Interface do Usuário

### 3.1 Tela Principal
- Logo da empresa centralizado na tela
- Menu de navegação lateral esquerdo
  - Fundo escuro (#263544)
  - Texto e ícones brancos
  - Ícone de calculadora para item "Erro"

### 3.2 Tela de Cálculo de Erro
#### Layout da Grade
- Múltiplas linhas com as seguintes colunas:
  1. Checkbox (Ativar/Desativar)
  2. Valor de Referência
  3. Valor do Medidor
  4. Percentual de Erro

#### Controles
- Botão Calcular
- Botão Limpar

## 4. Requisitos Funcionais

### 4.1 Gerenciamento de Linhas
- Cada linha pode ser ativada/desativada via checkbox
- Linhas desativadas:
  - Mostram "---" na coluna de erro
  - Campos de entrada bloqueados
  - Indicação visual de estado inativo

### 4.2 Cálculo de Erro
- Fórmula: ((Referência - Medidor) / Medidor * 100)
- Exibição dos Resultados:
  - Valores positivos: Texto azul em negrito com percentual
  - Valores negativos: Texto vermelho em negrito com percentual
  - Valor zero no medidor: "Referência Inválida"
  - Linhas desativadas: "---"

### 4.3 Funcionalidade de Limpeza
- Reinicia todos os campos de entrada
- Reinicia todos os cálculos de erro
- Mantém estados dos checkboxes

## 5. Regras de Validação
- Apenas linhas ativadas são incluídas nos cálculos
- Valor zero no medidor gera mensagem de referência inválida
- Apenas entradas numéricas para Referência e Medidor

## 6. Experiência do Usuário
- Design responsivo para dispositivos móveis
- Feedback visual claro para estados ativos/inativos
- Processo intuitivo de cálculo de erro
- Resultados de fácil leitura com código de cores

## 7. Requisitos de Desempenho
- Resposta imediata às interações do usuário
- Processamento suave dos cálculos
- Manipulação eficiente de múltiplas linhas
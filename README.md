# Analisador Sintático de Frases em Português

Projeto desenvolvido como parte do **P0 — P0-PRIMEIRO-FLUXO-LLM**, com o objetivo de explorar a integração entre Python e Modelos de Linguagem de Grande Porte (LLMs).

## Sobre o projeto

O Analisador Sintático de Frases em Português é uma aplicação executada pelo terminal que utiliza a API do Google Gemini para realizar análises sintáticas de frases fornecidas pelo usuário.

A aplicação recebe uma frase em língua portuguesa, envia o conteúdo para um modelo de linguagem e apresenta os elementos sintáticos identificados, acompanhados de explicações sobre suas funções na oração.

## Funcionalidades

- Recebimento de frases em português pelo terminal.
- Integração com a API do Google Gemini.
- Identificação dos elementos sintáticos:
  - Sujeito;
  - Núcleo do sujeito;
  - Predicado;
  - Núcleo do predicado;
  - Verbo;
  - Objeto direto;
  - Objeto indireto;
  - Adjunto adverbial e seu tipo, quando identificado.
- Apresentação dos resultados em texto simples.
- Explicação aprofundada das relações entre os elementos sintáticos.

## Tecnologias utilizadas

- **Python 3.14:** linguagem de programação utilizada no desenvolvimento.
- **Google Gemini API:** modelo de linguagem utilizado para realizar a análise sintática.
- **google-genai:** SDK para integração com a API do Gemini.
- **python-dotenv:** biblioteca utilizada para carregar variáveis de ambiente.

## Estrutura do projeto

```text
P0-Primeiro-fluxo-com-LLM/
│
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.14 ou compatível com as dependências utilizadas.
- Git.
- Uma chave de API do Google Gemini.

## Instalação e configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/ashaleyalcantara/P0-Primeiro-fluxo-com-LLM.git
```

### 2. Acessar a pasta do projeto

```bash
cd P0-Primeiro-fluxo-com-LLM
```

### 3. Criar o ambiente virtual

No Windows, utilizando PowerShell:

```powershell
py -3.14 -m venv .venv
```

### 4. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 6. Configurar a chave de API

Na raiz do projeto, crie um arquivo chamado `.env`, utilizando o `.env.example` como referência.

Adicione sua chave de API:

```env
GEMINI_API_KEY=sua_chave_de_api
```

**Importante:** o arquivo `.env` contém credenciais privadas e não deve ser compartilhado ou enviado ao GitHub.

## Como executar

Com o ambiente virtual ativado e as dependências instaladas, execute:

```powershell
python main.py
```

O programa solicitará uma frase para análise sintática.

## Exemplo de utilização

**Entrada:**

```text
Digite uma frase para análise sintática: A menina comprou um livro ontem
```

**Saída:**

A aplicação apresenta uma análise contendo os elementos sintáticos identificados, seguida de uma explicação sobre a estrutura da oração e a relação entre seus componentes.

## Observações

A análise é realizada por um Modelo de Linguagem de Grande Porte (LLM). Portanto, os resultados podem variar conforme a interpretação do modelo e a complexidade da construção sintática apresentada.

## Autoria

Desenvolvido por **Ashaley de Oliveira Alcantara**.

Projeto acadêmico e experimental desenvolvido durante o Programa de Capacitação em Agentes de Inteligência Artificial.

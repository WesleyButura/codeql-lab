# 🔐 CodeQL Lab

Projeto desenvolvido para estudos e práticas de análise estática de código utilizando o **CodeQL**, ferramenta de segurança da GitHub voltada para identificação de vulnerabilidades, falhas de qualidade e padrões inseguros em aplicações.

## 📌 Sobre o Projeto

Este laboratório tem como objetivo explorar o funcionamento do CodeQL, compreendendo como consultas (queries) podem ser utilizadas para identificar problemas de segurança em projetos de software.

O repositório serve como ambiente de aprendizado para:

- Configuração do CodeQL;
- Execução de análises automatizadas;
- Criação e execução de queries personalizadas;
- Estudo de vulnerabilidades conhecidas;
- Integração com GitHub Actions.

## 🚀 Tecnologias Utilizadas

- GitHub
- GitHub Actions
- CodeQL
- Visual Studio Code
- Git

## 🛡️ O que é CodeQL?

O CodeQL é uma plataforma de análise semântica de código desenvolvida pela GitHub que permite tratar o código-fonte como um banco de dados consultável. Dessa forma, é possível criar consultas capazes de identificar vulnerabilidades, bugs e problemas de qualidade em diferentes linguagens de programação.

Entre os benefícios do CodeQL estão:

- Identificação de vulnerabilidades de segurança;
- Automação de análises estáticas;
- Integração com pipelines CI/CD;
- Criação de consultas personalizadas;
- Escalabilidade para grandes bases de código.

## 📂 Estrutura do Projeto

```text
codeql-lab/
├── .github/
│   └── workflows/
├── queries/
├── databases/
├── src/
└── README.md
```

> A estrutura pode variar conforme a evolução do laboratório e os experimentos realizados.

## ⚙️ Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/WesleyButura/codeql-lab.git
```

### 2. Acesse o diretório

```bash
cd codeql-lab
```

### 3. Instale a extensão CodeQL

No Visual Studio Code, instale:

- CodeQL Extension for VS Code

### 4. Configure o CodeQL CLI

Baixe e configure o CodeQL CLI conforme a documentação oficial.

## ▶️ Executando Análises

Após criar ou importar uma base de dados CodeQL:

```bash
codeql database analyze database-name query.ql
```

Ou execute as análises automaticamente através do GitHub Actions configurado no repositório.

## 📖 Objetivos de Aprendizagem

- Entender os conceitos de Static Application Security Testing (SAST);
- Aprender a escrever consultas CodeQL;
- Detectar vulnerabilidades em aplicações;
- Integrar análise de segurança ao fluxo DevSecOps;
- Explorar recursos do GitHub Advanced Security.

## 📊 Possíveis Vulnerabilidades Analisadas

- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Path Traversal
- Hardcoded Credentials
- Insecure Deserialization

## 🔄 Integração com GitHub Actions

O CodeQL pode ser executado automaticamente em cada push ou pull request através do GitHub Actions, permitindo análise contínua da segurança do código.

Exemplo de fluxo:

```text
Push / Pull Request
        ↓
GitHub Actions
        ↓
CodeQL Analysis
        ↓
Security Alerts
```

## 📚 Referências

- https://codeql.github.com/
- https://github.com/github/codeql
- https://github.com/github/codeql-action
- https://docs.github.com/en/code-security

## 👨‍💻 Autor

**Wesley Butura da Silva**

GitHub: https://github.com/WesleyButura

---

⭐ Projeto criado para fins acadêmicos, pesquisa e aprendizado em segurança de aplicações utilizando CodeQL.

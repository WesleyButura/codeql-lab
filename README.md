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


## Evidências da Pipeline

### Teste 1 – Execução da Pipeline

A pipeline foi executada com sucesso, concluindo as etapas de análise de segurança, testes automatizados e deploy para o ambiente stage.

![Execução da Pipeline](Imagens/Pipeline%20funcionando%20corretamente%20(finalização%20da%20confecção).png)

Observação:  a Imagem abaixo apresenta a pipeline durante a confecção (e dando erro)

![Execução da Pipeline Erro](Imagens/Erro%20pipeline%20(processo%20de%20confecção).png)


### Teste 2 – Detecção de Vulnerabilidade

Foi identificada uma vulnerabilidade de SQL Injection através da análise estática realizada pelo CodeQL.

![Detecção de Vulnerabilidade no Alerta](Imagens/Primeira%20vez%20da%20detecção%20da%20vulnerabilidade%20(Alerta).png)
![Detecção de Vulnerabilidade no Commit](Imagens/Primeira%20vez%20da%20detecção%20da%20vulnerabilidade%20(commit).png)

### Teste 3 – Correção da Vulnerabilidade

A vulnerabilidade foi corrigida utilizando consultas parametrizadas, e o CodeQL registrou a correção na branch principal.

![Correção de Vulnerabilidade no Alerta](Imagens/Correção%20de%20Vulnerabilidade%20(Alerta).png)
![Correção de Vulnerabilidade no Commit](Imagens/Correção%20de%20Vulnerabilidade%20(Commit).png)

Observações Adicionais: No folder imagens, possui mais algumas imagens durante o processo de confecção e testes. 
Qualquer dúvida contatar Wesley Butura da Silva

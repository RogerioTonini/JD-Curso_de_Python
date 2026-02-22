#!/usr/bin/env bash

# 1. Adicione o script ao repositório
git add git-inicial.sh
git commit -m "chore(scripts): adicionar script de inicialização do repositório"

# Commit 2: Estrutura inicial
git add .gitignore .python-version
git commit -m "init: configurar estrutura inicial do projeto Python"

# Commit 3: Dependências
git add pyproject.toml poetry.lock
git commit -m "build: configurar Poetry e dependências do projeto"

# Commit 4: VSCode
git add .vscode/
git commit -m "chore(vscode): adicionar configurações do editor"

# Commit 5: Git Hooks
git add .githooks-scripts/
git commit -m "chore(git): adicionar scripts de hooks para Conventional Commits"

# Commit 6: App
git add app/
git commit -m "feat(app): criar estrutura base da aplicação"

# Commit 7: Testes
git add tests/
git commit -m "test: adicionar estrutura de testes"
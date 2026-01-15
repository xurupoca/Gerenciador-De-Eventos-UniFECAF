# Gerenciador-De-Eventos-UniFECAF

Sistema em **Python** para gerenciamento de eventos acadêmicos, permitindo que:
- Organizadores criem e gerenciem eventos (nome, data, descrição, vagas).
- Alunos se inscrevam e cancelem inscrições.
- Organizadores exportem relatórios de inscritos em **CSV/PDF**.
- Alunos avaliem eventos após participação.

## Métodologia de Desenvolvimento
Este projeto foi desenvolvido seguindo práticas de **Engenharia de Software**, aplicando metodologias ágeis e ferramentas de apoio ao ciclo de vida do software.

### Levantamento de Requisitos
- Entrevistas com o cliente.
- Identificação das necessidades do sistema.
- Registro dos requisitos funcionais (RF) e não funcionais (RNF).

### Especificação de Requisitos
| Tipos de requisitos | Descrição |
| :-- | :--- |
|RF01 |O sistema deve permitir login de usuários (organizadores e alunos).|
|RF02 |O sistema deve permitir que organizadores criem eventos com nome, data, descrição e número máximo de participantes.|
|RF03 |O sistema deve permitir atualização de  eventos (data e número de vagas) feitas por organizadores.|
|RF04 |O sistema deve permitir exclusão de eventos cancelados, por organizadores.|
|RF05 |O sistema deve permitir inscrição de alunos em eventos disponíveis.|
|RF06 |O sistema deve permitir cancelamento de inscrição em eventos por alunos.|
|RF07 |O sistema deve permitir a visualização de eventos disponíveis com informações detalhadas.|
|RF08 |O sistema deve permitir organizadores visualizarem a lista de inscritos em seus eventos.|
|RF09 |O sistema deve permitir organizadores a exportarem a lista de inscritos em formato CSV ou PDF.|
|RF10 |O sistema deve permitir aos alunos deixar uma avaliação aos eventos após participação (ex.: nota ou comentário).|
|RNF01|O tempo de resposta para qualquer operação deve ser inferior a 2 segundos.|
|RNF02|O sistema deve ter interface intuitiva, com feedback claro para ações do usuário (ex.: confirmação de inscrição).|
|RNF03|O sistema deve processar inscrições em menos de 1 segundo por operação.|
|RNF04|O sistema deve ser desenvolvido de forma modular, permitindo fácil manutenção e evolução.|

### Uso de Diagramas

**Caso de Uso**
![Diagrama Estudo de caso](src/docs/Diagrama%20de%20caso%20de%20uso.png)

---
**Diagrama de Classes**
![Diagrama de Classes](src/docs/Classe%20UML.png)


### Gestão ágil com KanBan
- Utilização do **GitHub Projects** para organizar tarefas.
- Quadro Kanban com colunas: **To Do**, **In Progress**, **Done**.
- Issues criadas para cada **Requisito Funcional**
- Labels para classificação (feature, bug, docs, test).

### Controle de Qualidade
- **GitHub Workflows (CI/CD):**
  - Execução automática de testes (Pytest).
  - Verificação de estilo e formatação (Black, Ruff).
  - Integração contínua para garantir qualidade do código.
- Testes unitários para validar regras de negócio.
- Exportação e relatórios verificados com casos de teste.

### Engenharia de Software
- Aplicação dos conceitos de:
  - **Modelagem de requisitos** (casos de uso, classes).
  - **Modularidade** para facilitar manutenção.
  - **Integração contínua** para garantir confiabilidade.
  - **Documentação** clara no README.

## Como rodar localmente

### Clonar o repositório
```bash
git clone https://github.com/jonathan-JIPSlok/Gestao-de-Eventos-UniFECAF.git
```

### Pré-Requisitos
- Python 3.12+
- Git Instalado
---

### Instalação
1. Crie um ambiente virtual (opcional, mas recomendado):

```Bash
python -m venv venv
```

2. Ative o ambiente:
```Bash
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instale as Dependências:
```Bash
pip install -r requirements.txt
```

### Executando o Sistema
Como o sistema é local e <b>baseado em prompt</b>, basta rodar:
```Bash
python main.py
```

O programa abrira um menu interativo no terminal, permitindo:
- Login como organizador ou aluno
- Criar / atualizar / remover eventos
- Inscrever-se ou cancelar inscrição
- Exportar lista de inscritos (CSV / PDF)
- Avaliar eventos concluídos

## Testes
Execute testes automatizados com:
```Bash
pytest
```

## Estrutura do projeto
```
src/
|--- models/                # Classes principais
|--- utils/                 # Funções auxiliares (exportação CSV/PDF)
|--- tests/                 # Testes automatizados
|--- docs/                  # Documentos do projeto
|--- main.py                # Ponto de entrada (Menu do prompt)
```

## Funcionalidades
- [x] Login de Usuário (organizador, aluno)
- [x] CRUD de Eventos
- [x] Inscrição e cancelamento de inscrição
- [x] Exportação de lista de inscritos (CSV/PDF)

## Licença
Este projeto está sob licença (MIT License) - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autor
Projeto desenvolvido para disciplina de Engenharia de Software

- Aluno: Lucas
- UniFECAF
- 2025
# Bolão Estaduais Cartolândia

## Descrição
O **Bolão Estaduais Cartolândia** é um sistema desenvolvido em **Python com Django**, utilizando **HTML e CSS**, onde os usuários podem participar de um bolão para tentar acertar os campeões e artilheiros dos campeonatos estaduais. Cada palpite correto acumula pontos, e ao final da competição, um ranking é gerado com os participantes que mais pontuaram.

## Funcionalidades
- Interface simples e intuitiva para seleção de palpites.
- Registro do nome do participante antes de submeter os palpites.
- Opção de escolher times campeões e artilheiros de cada campeonato.
- Possibilidade de adicionar opções personalizadas para campeão e artilheiro.
- Botão de "Ver Ranking" para acompanhar os resultados.
- Tema escuro com layout responsivo.

## Tecnologias Utilizadas
- **Backend:** Python + Django
- **Frontend:** HTML, CSS
- **Banco de Dados:** SQLite (pode ser alterado para PostgreSQL, MySQL, etc.)

## Como Executar o Projeto
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/bolao-estaduais.git
   cd bolao-estaduais
   ```
2. **Crie um ambiente virtual e ative-o:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Realize as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```
5. **Inicie o servidor Django:**
   ```bash
   python manage.py runserver
   ```
6. **Acesse a aplicação no navegador:**
   ```
   http://127.0.0.1:8000/
   ```

## Estrutura do Projeto
```
bolao-estaduais/
│-- manage.py
│-- bolao/  # App principal
│   │-- models.py  # Modelos do banco de dados
│   │-- views.py  # Lógica das views
│   │-- urls.py  # Rotas da aplicação
│   │-- templates/  # HTML das páginas
│   │-- static/  # Arquivos CSS e JS
│-- db.sqlite3  # Banco de dados SQLite (pode ser substituído por outro)
│-- requirements.txt  # Dependências do projeto
```

## Contribuição
Sinta-se à vontade para contribuir com o projeto! Basta fazer um **fork**, criar um **branch** para suas alterações e enviar um **pull request**.

## Licença
Este projeto é distribuído sob a licença MIT.


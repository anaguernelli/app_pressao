from flask import (
    Flask,
    render_template,
    request,
    redirect
)

import sqlite3

from datetime import datetime

app = Flask(__name__)

DATABASE = 'database.db'


# =========================
# CONEXÃO DATABASE
# =========================

def conectar():

    return sqlite3.connect(DATABASE)


# =========================
# CRIAR TABELA
# =========================

def criar_tabela():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicoes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            sistolica INTEGER NOT NULL,

            diastolica INTEGER NOT NULL,

            categoria TEXT NOT NULL,

            cor TEXT NOT NULL,

            emoji TEXT NOT NULL,
            
            mensagem TEXT NOT NULL,

            data_hora TEXT NOT NULL
        )
    ''')

    conn.commit()

    conn.close()


criar_tabela()

# =========================
# CLASSIFICAR PRESSÃO
# =========================

def classificar_pressao(
    sistolica,
    diastolica
):

    # =========================
    # CONVERSÃO AUTOMÁTICA
    # 12 -> 120
    # 8 -> 80
    # =========================

    if sistolica <= 30:

        sistolica = sistolica * 10

    if diastolica <= 30:

        diastolica = diastolica * 10


    # =========================
    # CLASSIFICAÇÃO
    # =========================

    if (
        sistolica < 120
        and
        diastolica < 80
    ):

        return {
            'categoria': 'NORMAL',
            'cor': 'verde',
            'emoji': '🟢',
            'mensagem': (
                'Pressão dentro da faixa normal. Continue mantendo '
                'hábitos saudáveis.'
            )
        }


    elif (
        120 <= sistolica < 140
        or
        80 <= diastolica < 90
    ):

        return {
            'categoria': 'ATENÇÃO',
            'cor': 'amarelo',
            'emoji': '🟡'
        }


    elif (
        140 <= sistolica < 180
        or
        90 <= diastolica < 120
    ):

        return {
            'categoria': 'HIPERTENSÃO',
            'cor': 'laranja',
            'emoji': '🟠'
        }


    else:

        return {
            'categoria': 'RISCO ALTO',
            'cor': 'vermelho',
            'emoji': '🔴'
        }


# =========================
# HOME
# =========================

@app.route('/')
def index():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute('''
        SELECT *
        FROM medicoes
        ORDER BY id DESC
        LIMIT 1
    ''')

    ultima_medicao = cursor.fetchone()

    conn.close()

    return render_template(
        'index.html',
        ultima_medicao=ultima_medicao
    )


# =========================
# REGISTRAR
# =========================

@app.route(
    '/registrar',
    methods=['POST']
)

def registrar():

    sistolica = int(
        request.form['sistolica']
    )

    diastolica = int(
        request.form['diastolica']
    )

    classificacao = classificar_pressao(
        sistolica,
        diastolica
    )

    categoria = classificacao['categoria']

    cor = classificacao['cor']

    emoji = classificacao['emoji']

    mensagem = classificacao['mensagem']

    data_hora = datetime.now().strftime(
        '%d/%m/%Y %H:%M'
    )

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO medicoes (

            sistolica,
            diastolica,
            categoria,
            cor,
            emoji,
            mensagem,
            data_hora

        )

        VALUES (?, ?, ?, ?, ?, ?, ?)

    ''', (

        sistolica,
        diastolica,
        categoria,
        cor,
        emoji,
        mensagem,
        data_hora
    ))

    conn.commit()

    conn.close()

    return redirect('/')


# =========================
# HISTÓRICO
# =========================

@app.route('/historico')
def historico():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute('''
        SELECT *
        FROM medicoes
        ORDER BY id DESC
    ''')

    medicoes = cursor.fetchall()

    conn.close()

    return render_template(
        'historico.html',
        medicoes=medicoes
    )


# =========================
# EXECUTAR
# =========================

if __name__ == '__main__':

    app.run(
        debug=True
    )
# Projecte M12

## Creat i programat amb amor per Alex Martinez i Óscar Gómez

<<<<<<< HEAD
=======
## Projecte de  Python, amb el framework Flask i repositoris Git, ampliant el primer projecte de M12 amb funcionalitats d’autenticació, autorització i creant més continguts. :)

> [!IMPORTANT]
> La lista de products para poder hacer ban es /products/list/admin (Ejemplo: http://127.0.0.1:5000/products/list/admin) //
> Solo pueden entrar usuarios con el rol de moderator

> [!TIP]
> En /admin/user solo puede acceder el admin para bloquear y debloquear users
>>>>>>> b0.2
## Setup

### Python Virtual Environment

Crea l'entorn:

    python3 -m venv .venv

Activa'l:

    source .venv/bin/activate

Instal·la el requisits:

    pip install -r requirements.txt

Per a generar el fitxer de requiriments:

    pip freeze > requirements.txt

Per desactivar l'entorn:

    deactivate

### Base de dades

La base de dades [SQLite](https://www.sqlite.org) s'ha de dir `database.db`. S'ha creat amb l'script [database.sql](./database.sql).

## Run des de terminal

Executa:

    flask --debug run

I obre un navegador a l'adreça: [http://127.0.0.1:5000](http://127.0.0.1:5000).

Aquesta comanda executa el codi de `wsgi.py` 

## Debug amb Visual Code

Des de l'opció de `Run and Debug`, crea un fitxer anomenat `launch.json` amb el contingut següent:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "WANNAPOP",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "wsgi.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```

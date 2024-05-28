# sabedoria

A project to store personal data in PostgreSQL, distribute in
json format through REST API, facilitating the use in some projects.

The routes are made up of scripts put together, taken from several
other applications that I needed and so I removed the duplication,
defined a format for use in all and thus came the wisdom.

The name wisdom is an irony to the fact that in the first version
some information was served by a yaml in base64 passed by environment
variable.

**Note**: that gunicorn was specially configured for flyio,
specifically the `Fly-Client-Ip` header in the 
[sabedoria/gunicorn.py](sabedoria/gunicorn.py) file

## How to works

### env variables

Languages or strings that represent the language you want to display,
remember that the columns in the baserow must also receive these prefixes

- https://www.rfc-editor.org/rfc/rfc9110.html#name-accept-language

```
LANGS="en-US,pt-BR"
```

Token to access your instance, send in header

```
TOKEN=awesometokenbutchangeit
```

Linkedin username
```
NAME=Sabio
```

Linkedin username

```
GITHUB=sabio
```

Linkedin username

```
LINKEDIN=sabio
```

To use, without schema (mailto:)
```
EMAIL=example@example.com
```

URL to site, without schema
```
SITE=example.com
```

Automatically calculates the number of cpus based on your processor with the formula cpu_count() * 2 + 1, can be specified manually and override

```
WEB_CONCURRENCY=cpu_count
```

Indicates the number of threads started, deafult is 1

```
PYTHON_MAX_THREADS=1
```

Hot reload application, deafult is `False`

```
WEB_RELOAD=False
```

### Use

Install dependencies from file, 

```
python -m venv ./venv
./venv/bin/activate
pip install -r requirements.txt
```

Running with **Flask**:

```
LANGS=en-US,pt-BR \
TOKEN=aawesometoken \
NAME=Sabio \
GITHUB=sabio \
LINKEDIN=sabio \
EMAIL=example@example.com \
SITE=example.com \
FLASK_APP="sabedoria:create_app('sabedoria.config.ProductionConfig')" flask run
```

**Or** running with **Docker**:

```
docker compose up
```

Call to service:

```
curl -H "Authorization: Bearer aawesometoken" \
     -H "Accept-Language: en-US" \
     http://localhost:5000/v2/education
```

## API docs

- [openapi.yml](openapi.yml)
- [swagger](https://editor-next.swagger.io/?url=https://raw.githubusercontent.com/droposhado/sabedoria/main/openapi.yml)

## License

See [LICENSE](LICENSE)

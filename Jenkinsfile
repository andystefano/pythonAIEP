pipeline {
    agent any

    stages {
        stage('Clonar repo') {
            steps {
                git 'https://github.com/andystefano/pythonAIEP'
            }
        }

        stage('Crear .env') {
            steps {
                withCredentials([
                    string(credentialsId: 'server',         variable: 'server'),
                    string(credentialsId: 'port',           variable: 'port'),
                    string(credentialsId: 'database',       variable: 'database'),
                    string(credentialsId: 'user',           variable: 'user'),
                    string(credentialsId: 'password',       variable: 'password'),
                    string(credentialsId: 'openai',         variable: 'openai'),
                    string(credentialsId: 'mailgun_secret', variable: 'mailgun_secret'),
                    string(credentialsId: 'mailgun_url',    variable: 'mailgun_url'),
                ]) {
                    sh '''
                        cat > .env <<EOF
server=${server}
port=${port}
database=${database}
user=${user}
password=${password}
openai=${openai}
mailgun_secret=${mailgun_secret}
mailgun_url=${mailgun_url}
EOF
                    '''
                }
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '''
                    if python3 -m venv .venv; then
                        . .venv/bin/activate
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                    else
                        echo "venv no disponible; usando instalacion de usuario"
                        python3 -m pip install --user --break-system-packages -r requirements.txt
                    fi
                '''
            }
        }

        stage('Validar app') {
            steps {
                sh '''
                    if [ -f .venv/bin/activate ]; then
                        PYTHON_BIN=".venv/bin/python"
                    else
                        PYTHON_BIN="python3"
                    fi

                    $PYTHON_BIN -m py_compile index.py

                    $PYTHON_BIN - <<'PY'
from index import app

client = app.test_client()
response = client.get("/")

assert response.status_code == 200, f"status inesperado: {response.status_code}"
print("Smoke test OK: GET / -> 200")
PY
                '''
            }
        }

        stage('Desplegar app') {
            steps {
                sh '''
                    if [ -f .venv/bin/activate ]; then
                        PYTHON_BIN=".venv/bin/python"
                    else
                        PYTHON_BIN="python3"
                    fi

                    if [ -f app.pid ] && kill -0 "$(cat app.pid)" 2>/dev/null; then
                        kill "$(cat app.pid)" || true
                        sleep 1
                    fi

                    JENKINS_NODE_COOKIE=dontKillMe BUILD_ID=dontKillMe nohup $PYTHON_BIN index.py > app.log 2>&1 &
                    echo $! > app.pid
                    sleep 3
                    if ! kill -0 "$(cat app.pid)" 2>/dev/null; then
                        echo "La app no quedo corriendo. Revisar app.log"
                        exit 1
                    fi

                    $PYTHON_BIN - <<'PY'
import urllib.request

with urllib.request.urlopen("http://127.0.0.1:8000/", timeout=10) as r:
    status = r.getcode()

assert status == 200, f"deploy fallido, status: {status}"
print("Deploy OK: app corriendo en puerto 8000")
PY
                '''
            }
        }
    }
}
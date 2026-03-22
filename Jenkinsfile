pipeline {
    agent any

    stages {
        stage('Clonar repo') {
            steps {
                git 'https://github.com/andystefano/pythonAIEP'
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
    }
}
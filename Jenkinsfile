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

        stage('Ejecutar app') {
            steps {
                sh '''
                    if [ -f .venv/bin/activate ]; then
                        . .venv/bin/activate
                        python index.py
                    else
                        python3 index.py
                    fi
                '''
            }
        }
    }
}
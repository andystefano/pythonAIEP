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
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar app') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python index.py
                '''
            }
        }
    }
}
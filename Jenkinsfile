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
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Ejecutar app') {
            steps {
                sh 'python3 index.py'
            }
        }
    }
}
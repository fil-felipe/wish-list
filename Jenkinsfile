pipeline {
    agent any 
    stages {
        stage('Install') { 
            steps {
                sh 'python3 -m pip install -r requirements.txt' 
            }
        }
        stage('Migrate') { 
            steps {
                sh './manage.py  makemigrations' 
            }
        }
    }
}
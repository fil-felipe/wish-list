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
                sh '/usr/bin/python3.8 manage.py  makemigrations' 
                sh '/usr/bin/python3.8 manage.py  migrate' 
            }
        }
        stage('Collect Static') { 
            steps {
                sh '/usr/bin/python3.8 manage.py  collectstatic -yes' 
            }
        }
        stage('Run') { 
            steps {
                sh 'JENKINS_NODE_COOKIE=dontKillMe nohup /usr/bin/python3.8 manage.py runserver 192.168.0.108:8000 &' 
            }
        }
    }
}

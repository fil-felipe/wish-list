pipeline {
    agent any 
    environment {
        DJANGO_SUPERUSER = credentials('django-superuser-filada')
        DJANGO_SUPERUSER_PASSWORD = "${DJANGO_SUPERUSER_USR}"
        DJANGO_SUPERUSER_USERNAME = "${DJANGO_SUPERUSER_PSW}"
        DJANGO_SUPERUSER_EMAIL  = credentials('django-superuser-mail')
    }
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
        stage('Create super user') { 
            steps {
                sh '/usr/bin/python3.8 manage.py  createsuperuser --noinput' 
            }
        }
        stage('Collect Static') { 
            steps {
                sh '/usr/bin/python3.8 manage.py  collectstatic --noinput' 
            }
        }
        stage('Run') { 
            steps {
                sh 'JENKINS_NODE_COOKIE=dontKillMe nohup /usr/bin/python3.8 manage.py runserver 192.168.0.108:8000 &' 
            }
        }
    }
}

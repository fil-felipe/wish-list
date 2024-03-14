pipeline {
    agent any 
    environment {
        DJANGO_SUPERUSER = credentials('django-superuser-filada')
        DJANGO_SUPERUSER_USERNAME = "${DJANGO_SUPERUSER_USR}"
        DJANGO_SUPERUSER_PASSWORD = "${DJANGO_SUPERUSER_PSW}"
        DJANGO_SUPERUSER_EMAIL  = credentials('django-superuser-mail')
    }
    stages {
        stage('docker compose') { 
            steps {
                sh 'docker-compose up' 
            }
        }
    }
}

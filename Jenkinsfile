pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m pip install -r requirements.txt' 
                sh 'echo "DONE"' 
            }
        }
    }
}

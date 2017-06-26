
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'printenv'
                sh 'python main_tests.py'
            }
        }
    }
}

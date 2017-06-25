
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python main_tests.py'
            }
        }
    }
}

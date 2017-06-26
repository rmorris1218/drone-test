
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Running ${env.BUILD_TAG}..."
                sh 'python main_tests.py'
            }
        }
    }
}


pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building $ENV.BRANCH_NAME from $ENV.CHANGE_AUTHOR_DISPLAY_NAME..."
                sh 'python main_tests.py'
            }
        }
    }
}


pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building $BRANCH_NAME from $CHANGE_AUTHOR_DISPLAY_NAME...'
                sh 'python main_tests.py'
                echo 'Done.'
            }
        }
    }
}

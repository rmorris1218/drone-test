
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building ${env.BRANCH_NAME} from ${env.CHANGE_AUTHOR_DISPLAY_NAME}...'
                sh 'python main_tests.py'
            }
        }
    }
}

#!/usr/bin/env groovy

pipeline {
    agent {
        docker {
            image 'python'
            args '-u root'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python main_tests.py'
            }
        }
    }
}

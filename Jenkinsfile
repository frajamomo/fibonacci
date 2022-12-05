pipeline {
    agent { dockerfile true }

    stages {
        stage ('Test') {
            sh 'python -m unittest --verbose'
        }
    }
}
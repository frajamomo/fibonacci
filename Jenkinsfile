pipeline {
    agent { dockerfile true }

    stages {
        stage('Verify Branch') {

            steps {
                echo "$GIT_BRANCH"
            }
        }

        stage ('Test'){
            steps {
                sh 'python -m unittest --verbose'
            }
        }
    }
}
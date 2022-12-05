pipeline {
    agent any

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
            post {
                success {
                    echo "Test PASS"
                }
                failure {
                    echo "Test FAIL"
                }
            }
        }
    }
}

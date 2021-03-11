pipeline {
    agent any

    stages {        
        stage('Build'){
            steps{
                bat 'python test_api.py'
            }
        }
        stage('Test'){
            steps{
                echo 'The job has been tested'
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deployed successfully'
            }
        }
    }
}

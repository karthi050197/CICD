pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your version control system
                git 'https://github.com/muthuramanathanm/jenkins-cicd.git'
            }
        }
        
        stage('Install dependencies') {
            steps {
                // Install Python dependencies using pip
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run tests') {
            steps {
                // Run your Python tests
                sh 'python -m unittest discover -s tests -p "*_test.py"'
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy your Python application
                sh 'python HelloWorld.py'
            }
        }
    }
    
    post {
        success {
            // Notify on successful deployment
            echo 'Deployment successful!'
        }
        failure {
            // Notify on deployment failure
            echo 'Deployment failed!'
        }
    }
}


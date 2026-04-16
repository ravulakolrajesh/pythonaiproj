pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/ravulakolrajesh/pythonaiproj.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t my-app:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop my-app || true
                docker rm my-app || true
                docker run -d --name my-app -p 8081:80 my-app:latest
                '''
            }
        }
    }
}
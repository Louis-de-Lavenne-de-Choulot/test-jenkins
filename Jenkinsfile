pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                git branch source, url 'https://github.com/Louis-de-Lavenne-de-Choulot/test-jenkins.git'
        }
        stage('Build') {
            agent {
                label 'jenkins-agent-python'
            }
            steps {
                echo 'Building...'
                //verify python
                sh 'python --version'
                //install requirements
                sh 'pip install -r requirements.txt'
                // compile python main.py


                }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
            }
    }
}
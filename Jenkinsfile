pipeline{
    agent any
    stages
    {
        stage('Build Docker Image'){
            steps {
                echo "Build Docker Image"
                bat "docker build -t kubedemoapp:v1 ."
            }
        }
        stage('Docker Login'){
            steps{
                bat "docker login -u kadarinandhini -p password"
            }
        }
        stage('push Docker Image to Docker Hub'){
            steps{
                echo "push Docker Image to Docker Hub"
                bat "docker tag kubedemospp:v1 kadarinandhini/sample:kubeimage1"
                bat "docker push kadarinandhini/sample:kubeimage1"
            }
        }
        stage('Deploy to Kubernetes'){
            steps{
                //apply deployment and service
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post{
        sucess{
            echo 'Pipeline completed sucessfully'
        }
        failure{
            echo 'Pipeline failed. Please check the logs'
        }
    }
}
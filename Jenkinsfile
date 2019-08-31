pipeline {
  agent any
  stages {
    stage('hi') {
      steps {
        echo 'hello world'
      }
    }
    stage('Lint   html') {
      steps {
        sh '''
                                               tidy -q -e templates/index.html
                                               tidy -q -e templates/addition.html
                                               tidy -q -e templates/sub.html
                                               tidy -q -e templates/mult.html
                                               tidy -q -e templates/div.html
                                               tidy -q -e templates/exp.html
                                          '''
      }
    }
    stage('Credentials') {
      steps {
        withCredentials(bindings: [[$class:  'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'bear1', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
          sh """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               mkdir -p ~/.aws
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               echo "[default]" >~/.aws/credentials
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               echo "[default]" >~/.boto
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               echo "aws_access_key_id = ${AWS_ACCESS_KEY_ID}" >>~/.boto
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               echo "aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY}" >>~/.boto
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               echo "aws_access_key_id = ${AWS_ACCESS_KEY_ID}" >>~/.aws/credentials
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               echo "aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY}" >>~/.aws/credentials
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        """
        }

      }
    }
    stage('docker login') {
      steps {
        sh 'sudo docker login --username beartuchman --password BearBarky1'
      }
    }
    stage('push docker') {
      steps {
        sh './push_docker.sh'
      }
    }
    stage('create eksctl') {
      steps {
        sh '''eksctl create cluster --region us-east-1 --name prod --nodegroup-name standard-workers --node-type t2.micro
'''
      }
    }
    stage('kubectl') {
      steps {
        sh 'kubectl get pods'
      }
    }
    stage('bye') {
      steps {
        echo 'bye'
      }
    }
  }
}

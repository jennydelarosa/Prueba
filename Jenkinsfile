pipeline {
    agent any
//  agent { node { label 'docker' } }
 parameters {
        string(name: 'name_container', defaultValue: 'python-flask-jenny', description: 'nombre del docker')
        string(name: 'name_imagen', defaultValue: 'python-flask', description: 'nombre de la imagen')
        string(name: 'tag_imagen', defaultValue: '0.0.1', description: 'etiqueta de la imagen')
        string(name: 'puerto_imagen', defaultValue: '80', description: 'puerto a publicar')
    }
    environment {
        name_final = "${name_container}${tag_imagen}"        
    }
    stages {
        stage('stop/rm') {

            when {
                expression { 
                    DOCKER_EXIST = sh(returnStdout: true, script: 'echo "$(docker ps -q -a --filter name=${name_final})"').trim()
                    return  DOCKER_EXIST != '' 
                }
            }
            steps {
                script{
                    sh ''' 
                         docker stop ${name_final}
                         docker rm ${name_final}
                    '''
                    }
                    
                }                    
                                  
            }
           
        stage('build') {
            steps {
                script{
                    sh ''' 
                    docker build -t ${name_imagen}:${tag_imagen} .
                    '''
                    }
                    
                }                    
                                  
            }
        stage('run') {
            steps {
                script{
                    sh ''' 
                        docker run -dp ${puerto_imagen}:8080 --name ${name_final} ${name_imagen}:${tag_imagen}
 
                    '''
                    }
                    
                }                    
                                  
            }
        stage('ecr') {
            steps {
                script{
                    withCredentials([usernamePassword(credentialsId: 'credentials_jenny', passwordVariable: 'pass', usernameVariable: 'user')]) {
                        print 'username=' + username + 'password=' + password
                    }
                    //sh ''' 
                    //    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 897616845305.dkr.ecr.us-east-1.amazonaws.com
                    //    docker tag python-flask:0.0.1 897616845305.dkr.ecr.us-east-1.amazonaws.com/helloword:0.0.2
                    //    docker push 897616845305.dkr.ecr.us-east-1.amazonaws.com/helloword:0.0.2
 
                    //'''
                    }
                    
                }                    
                                  
            } 
            
          
        }   
    }
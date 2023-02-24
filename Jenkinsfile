pipeline {
  agent any
 parameters {
        string(name: 'name_container', defaultValue: 'python-flask-jenny', description: 'nombre del docker')
        string(name: 'name_imagen', defaultValue: 'python-flask', description: 'nombre de la imagen')
        string(name: 'tag_imagen', defaultValue: '0.0.1', description: 'etiqueta de la imagen')
        string(name: 'puerto_imagen', defaultValue: '8080', description: 'puerto a publicar')
    }
    environment {
        name_final = "${name_container}${tag_imagen}"        
    }
    stages {
        stage('stop/rm') {

            when {
                expression { 
                    DOCKER_EXIST = sh(returnStdout: true, script: 'echo "$(docker ps -q --filter name=${name_final})"').trim()
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
            
          
        }   
    }
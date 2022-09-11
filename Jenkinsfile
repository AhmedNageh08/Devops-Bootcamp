properties([
  parameters([
    string(name: 'VERSION', description: 'Version for tag')
    ])
  ])
node('pharmec'){
    stage("Sync"){
        checkout scm
    }
    stage("Build"){
        docker.withRegistry('', 'token-hub'){
           //def commit = sh(returnStdout: true, script: "git log -n 1 --pretty=format:'%h'").trim() 
           def testImage = docker.build("ahmednageh08/flask-app:${VERSION}")
           testImage.push() 
        }
        currentBuild.result = 'SUCCESS'
    }
    stage("Deploy"){
        withKubeConfig([credentialsId: 'ccs3-chs-dev-qa-shared', serverUrl: 'https://k8s-eb.cegedim.cloud/k8s/clusters/c-c9n4r']){
                sh ("kubectl set image deployment/flaskapp-deployment nodeserver=ahmednageh08/flask-app:${VERSION} --namespace=ccs3-his-hotfix --output=yaml")
        }
    }
}
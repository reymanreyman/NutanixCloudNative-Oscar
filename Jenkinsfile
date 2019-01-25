node("docker") {
    docker.withRegistry('https://cloud.docker.com', 'bef9483a-47b8-4096-9bce-bc0cdd198b9a') {
    
        git url: "https://drt-it-github-prod-1.eng.nutanix.com/michael-haigh/NutanixCloudNative-Oscar/", credentialsId: 'd8500ae9-87ba-4fdc-bf16-2535b0a51011'
    
        sh "git rev-parse HEAD > .git/commit-id"
        def commit_id = readFile('.git/commit-id').trim()
        println commit_id
    
        stage "build"
        def app = docker.build "michaelatnutanix/oscar_jet"
    
        stage "publish"
        app.push 'master'
        app.push "${commit_id}"
    }
}

node("docker") {
    docker.withRegistry('', 'bef9483a-47b8-4096-9bce-bc0cdd198b9a') {
    
        git url: "https://github.com/MichaelHaigh/NutanixCloudNative-Oscar/"
    
        sh "git rev-parse HEAD > .git/commit-id"
        def commit_id = readFile('.git/commit-id').trim()
        println commit_id
    
        stage "Build"
        def oscarApp = docker.build "michaelatnutanix/oscar_jet"
    
        stage "Publish"
        oscarApp.push 'latest'
        oscarApp.push "${commit_id}"

        stage "Application Launch"
        step([$class: 'BlueprintLaunch', appProfileName: 'Default', applicationName: 'NCN_${BUILD_ID}', blueprintDescription: 'Description is empty', blueprintName: 'NutanixCloudNativeDemo', projectName: 'Demo', runtimeVariables: '{}', waitForSuccessFulLaunch: true])
    }
}

node("built-in") {
    docker.withRegistry('', 'dockerhub-cred-andresrey') {
    
        git url: "https://github.com/reymanreyman/NutanixCloudNative-Oscar/"
    
        sh "git rev-parse HEAD > .git/commit-id"
        def commit_id = readFile('.git/commit-id').trim()
        println commit_id
    
        stage "Build"
        def oscarApp = docker.build "andresrey/oscar_jet"
    
        stage "Publish"
        oscarApp.push 'latest'
        oscarApp.push "${commit_id}"

        stage "Application Launch"
        step([$class: 'BlueprintLaunch', appProfileName: 'Default', applicationName: 'NCN_${BUILD_ID}', blueprintDescription: 'Description is empty', blueprintName: 'NutanixCloudNativeWithDatabaseProvisioning', projectName: 'Default', runtimeVariables: '{}', waitForSuccessFulLaunch: 'false'])
    }
}

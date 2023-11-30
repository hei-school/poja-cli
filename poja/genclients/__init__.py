import poja.sed as sed


def set_gen_clients(with_gen_clients, temp_dir, exclude):
    if with_gen_clients == "true":
        sed.find_replace(
            temp_dir,
            "<?gen-clients>",
            """task generateJavaClient(type: GenerateTask) {
    generatorName = "java"
    inputSpec = "$rootDir/doc/api.yml".toString()
    outputDir = "$buildDir/gen".toString()
    apiPackage = "school.hei.poja.endpoint.rest.api"
    invokerPackage = "school.hei.poja.endpoint.rest.client"
    modelPackage = "school.hei.poja.endpoint.rest.model"

    configOptions = [
            serializationLibrary: "jackson",
            dateLibrary: "custom"
    ]
    typeMappings = [
            // What date-time type to use when? https://i.stack.imgur.com/QPhGW.png
            Date: "java.time.LocalDate",
            DateTime: "java.time.Instant",
    ]
    library = "native"

    groupId = 'school.hei'
    id = '<?app-name>-gen'
    skipValidateSpec = false
    logToStderr = true
    generateAliasAsModel = false
    enablePostProcessFile = false
}
task generateTsClient(type: org.openapitools.generator.gradle.plugin.tasks.GenerateTask) {
    generatorName = "typescript-axios"
    inputSpec = "$rootDir/doc/api.yml".toString()
    outputDir = "$buildDir/gen-ts".toString()
    typeMappings = [
            Date    : "Date",
            DateTime: "Date",
    ]
    additionalProperties = [
            enumPropertyNaming: "original",
            npmName           : "@<?app-name>/typescript-client",
            npmVersion        : project.properties["args"] ?: "latest"
    ]
}
task publishJavaClientToMavenLocal(type: Exec, dependsOn: generateJavaClient) {
    if (Os.isFamily(Os.FAMILY_WINDOWS)){
        commandLine './.shell/publish_gen_to_maven_local.bat'
    } else {
        commandLine './.shell/publish_gen_to_maven_local.sh'
    }
}
tasks.compileJava.dependsOn publishJavaClientToMavenLocal
""",
            exclude,
        )
    else:
        sed.find_replace(temp_dir, "<?gen-clients>", "", exclude)

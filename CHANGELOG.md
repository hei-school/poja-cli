# [9.1.0](https://github.com/hei-school/poja-cli/compare/v9.0.3...v9.1.0) (2024-01-03)


### Features

* specify SesClient region ([86a211b](https://github.com/hei-school/poja-cli/commit/86a211b54ac33eeb7fdb4d05f311a3b2dee57056))



## [9.0.3](https://github.com/hei-school/poja-cli/compare/v9.0.2...v9.0.3) (2023-12-29)


### Bug Fixes

* -Dspring.data.jpa.repositories.bootstrap-mode=lazy when no snapstart ([2d4a783](https://github.com/hei-school/poja-cli/commit/2d4a783001cd61023fab9773e17090ab75394956))



## [9.0.2](https://github.com/hei-school/poja-cli/compare/v9.0.1...v9.0.2) (2023-12-21)


### Bug Fixes

* add execute permission on gradlew before running tests ([193a887](https://github.com/hei-school/poja-cli/commit/193a88748cf8b3da5ce4a887305a6eb5cd810600))



## [9.0.1](https://github.com/hei-school/poja-cli/compare/v9.0.0...v9.0.1) (2023-12-21)


### Bug Fixes

* configure and registerModules in objectMapper ([0e56300](https://github.com/hei-school/poja-cli/commit/0e56300e4486a208a0558e1ac6a0c140f4439bd0))



# [9.0.0](https://github.com/hei-school/poja-cli/compare/v8.0.0...v9.0.0) (2023-12-20)


### Bug Fixes

* add EndpointConf ([35e5c9f](https://github.com/hei-school/poja-cli/commit/35e5c9fcd7352bf3159fc810a2d1fe9e9d2e84a2))


### BREAKING CHANGES

* manually rm JacksonMappingConfiguration as it now becomes EndpointConf



# [8.0.0](https://github.com/hei-school/poja-cli/compare/v7.0.1...v8.0.0) (2023-12-20)


### Bug Fixes

* --frontal-memory defaults to 2048 instead of 512 ([42c5cef](https://github.com/hei-school/poja-cli/commit/42c5cef99ccd1554c89d938fb477d78021f6220a))
* --with-snapstart defaults to false instead of true ([f0b1a52](https://github.com/hei-school/poja-cli/commit/f0b1a52f24f5a3090b048881736e6a1959e1a009))


### BREAKING CHANGES

* --frontal-memory defaults to 2048 instead of 512
* --with-snapstart defaults to false instead of true



## [7.0.1](https://github.com/hei-school/poja-cli/compare/v7.0.0...v7.0.1) (2023-12-18)


### Bug Fixes

* configurable region in deploy event and compute permission workflows ([6e68f8b](https://github.com/hei-school/poja-cli/commit/6e68f8b346291f9a211d406d5685a2532bdd02f4))
* set aws credentials in CI ([b103d4a](https://github.com/hei-school/poja-cli/commit/b103d4a8127e2fb9b2690011271f0509349732cb))
* use spring bean object mapper instead of creating a new instance ([d0a2840](https://github.com/hei-school/poja-cli/commit/d0a2840e4f6154a5f7e267556102373bc870d3ba))



# [7.0.0](https://github.com/hei-school/poja-cli/compare/v6.0.0...v7.0.0) (2023-12-13)


### Features

* support for directory upload ([fe5c750](https://github.com/hei-school/poja-cli/commit/fe5c750cc9653261cd51d8d004729f300d575f7e))


### BREAKING CHANGES

* former BucketComponent.download that returned an InputStream now returns a File



# [6.0.0](https://github.com/hei-school/poja-cli/compare/v5.0.0...v6.0.0) (2023-12-12)


### Features

* --with-database=sqlite ([bb72bad](https://github.com/hei-school/poja-cli/commit/bb72bad6fff1d0c00bdc07edb6433d91ea076c49))


### BREAKING CHANGES

* former with_postgres defaulting to true now becomes with_database defaulting to sqlite
* manually remove former repository.DatasourceConf as poja now generates repository.conf.DatasourceConf



# [5.0.0](https://github.com/hei-school/poja-cli/compare/v4.1.2...v5.0.0) (2023-12-11)


### Features

* mail package ([9c488da](https://github.com/hei-school/poja-cli/commit/9c488dac4c9ba055aa16f9daf181b2a027fa2c61))


### BREAKING CHANGES

* you need to manually rm HealthController and rm infra-health-check.yml



## [4.1.2](https://github.com/hei-school/poja-cli/compare/v4.1.1...v4.1.2) (2023-12-08)


### Bug Fixes

* use .shell/checkHealth.sh ([f57bef6](https://github.com/hei-school/poja-cli/commit/f57bef6506b24ca76b072689c693e1c59a83f981))



## [4.1.1](https://github.com/hei-school/poja-cli/compare/v4.1.0...v4.1.1) (2023-12-08)


### Bug Fixes

* use GHA hei-school/aws-credentials-setter ([369cc55](https://github.com/hei-school/poja-cli/commit/369cc559ef694b5b6f0c5d0ae18328abfe2d9e73))



# [4.1.0](https://github.com/hei-school/poja-cli/compare/v4.0.0...v4.1.0) (2023-12-07)


### Features

* file package with bucket component ([bdc0b6e](https://github.com/hei-school/poja-cli/commit/bdc0b6eb3d6430b1a00a90b6244422f704fd994a))



# [4.0.0](https://github.com/hei-school/poja-cli/compare/v3.6.1...v4.0.0) (2023-11-30)


### Bug Fixes

* add missing script to connect to codeartifact private repository ([9f40e38](https://github.com/hei-school/poja-cli/commit/9f40e3888c5ef9faf72c05ff62412ed41601d334))


* feat!: Update default values for frontal_memory and worker_memory ([6f92f32](https://github.com/hei-school/poja-cli/commit/6f92f329982ecd42e76fb9d37f6156414f2507de))


### BREAKING CHANGES

* Reduce frontal_memory default to 512 and worker_memory default to 1024



## [3.6.1](https://github.com/hei-school/poja-cli/compare/v3.6.0...v3.6.1) (2023-11-29)


### Bug Fixes

*  --> use py.open(w+) to create api.yml if not exist ([7da85ed](https://github.com/hei-school/poja-cli/commit/7da85edb4594944b728d44c19715b4c3a83e05cf))
* format.sh --> format.bat on Windows ([17871d7](https://github.com/hei-school/poja-cli/commit/17871d7ba2a15878f5b062f97dce4126b8eecbb7))
* os.mkdir --> pathlib.mkdir for Windows compatibility ([3379aa5](https://github.com/hei-school/poja-cli/commit/3379aa50326f4b232db555330642f572fc19a312))
* shutil.rmtree -> git.rmtree for windows compatibility ([da67f5b](https://github.com/hei-school/poja-cli/commit/da67f5b5cc12960f772debf7cd24978376da2317))



# [3.6.0](https://github.com/hei-school/poja-cli/compare/v3.5.2...v3.6.0) (2023-11-28)


### Features

* run spring boot on any available port when triggered from SQS Event ([ed66d5c](https://github.com/hei-school/poja-cli/commit/ed66d5c8b7827d92e53c36790957ee5ced44e48f))



## [3.5.2](https://github.com/hei-school/poja-cli/compare/v3.5.1...v3.5.2) (2023-11-28)


### Bug Fixes

* springfox --> springdoc ([ea8a1b0](https://github.com/hei-school/poja-cli/commit/ea8a1b080f3cc2f6b42f7bc715b7ca19c1fdfd18))



## [3.5.1](https://github.com/hei-school/poja-cli/compare/v3.5.0...v3.5.1) (2023-11-28)


### Bug Fixes

* use springfox-swagger2 for compatibility with spring2 ([8333aed](https://github.com/hei-school/poja-cli/commit/8333aedeeff3e862c0f26b369e1e7ba016d38ca6))



# [3.5.0](https://github.com/hei-school/poja-cli/compare/v3.4.1...v3.5.0) (2023-11-27)


### Features

* --with-swagger-ui ([c310209](https://github.com/hei-school/poja-cli/commit/c310209ec49354773be3214d578d4478a1956425))



## [3.4.1](https://github.com/hei-school/poja-cli/compare/v3.4.0...v3.4.1) (2023-11-27)


### Bug Fixes

* extra custom_java_deps --> custom_java_repositories ([367dadb](https://github.com/hei-school/poja-cli/commit/367dadbe4f284bcf726b9cfadaa04ae027b7a50c))



# [3.4.0](https://github.com/hei-school/poja-cli/compare/v3.3.0...v3.4.0) (2023-11-27)


### Features

* --custom-java-repositories ([517e531](https://github.com/hei-school/poja-cli/commit/517e531c536ab9b2e7cbeb80c82607034d34e7c7))



# [3.3.0](https://github.com/hei-school/poja-cli/compare/v3.2.0...v3.3.0) (2023-11-24)


### Features

* store eventBridge bus arn and Deadletter queue arn in SSM ([3057d3e](https://github.com/hei-school/poja-cli/commit/3057d3e1afd434be836f00123ab2b7e3545dd1c0))



# [3.2.0](https://github.com/hei-school/poja-cli/compare/v3.1.0...v3.2.0) (2023-11-21)


### Features

* storage = database + bucket ([4a8402d](https://github.com/hei-school/poja-cli/commit/4a8402d332ec70a518f735f891285cdd94052daa))



# [3.1.0](https://github.com/hei-school/poja-cli/compare/v3.0.6...v3.1.0) (2023-11-21)


### Bug Fixes

* default region is Paris ([99a0c37](https://github.com/hei-school/poja-cli/commit/99a0c371ccf72030c6aff2cc1155bb619957107b))


### Features

* --frontal-memory, --worker-memory and --worker-batch ([a3dd156](https://github.com/hei-school/poja-cli/commit/a3dd1569011ce42715a821a35d439a831fe06231))



## [3.0.6](https://github.com/hei-school/poja-cli/compare/v3.0.5...v3.0.6) (2023-11-17)


### Bug Fixes

* read version directly from gradle.properties file ([81426b5](https://github.com/hei-school/poja-cli/commit/81426b5dcd45f515e5c29180b885223fd471146f))



## [3.0.5](https://github.com/hei-school/poja-cli/compare/v3.0.4...v3.0.5) (2023-11-17)


### Bug Fixes

* read directly version from gradle.properties ([a44ca79](https://github.com/hei-school/poja-cli/commit/a44ca790a8f6fb709c9036ac86839ddf751c9283))



## [3.0.4](https://github.com/hei-school/poja-cli/compare/v3.0.3...v3.0.4) (2023-11-16)


### Bug Fixes

* cannot touch ./doc/api.yml file ([7647e7e](https://github.com/hei-school/poja-cli/commit/7647e7e97228662c1660e171b57f2cd942ca5472))



## [3.0.3](https://github.com/hei-school/poja-cli/compare/v3.0.2...v3.0.3) (2023-11-15)


### Bug Fixes

* add checkout step in publish-client script ([f6189d7](https://github.com/hei-school/poja-cli/commit/f6189d79a08b5d5c4e1817ea398a65e4132a0705))



## [3.0.2](https://github.com/hei-school/poja-cli/compare/v3.0.1...v3.0.2) (2023-11-15)


### Bug Fixes

* mkdir ./doc --> mkdir -p ([0421b4f](https://github.com/hei-school/poja-cli/commit/0421b4ff663f8ecec802d3458a41edb33db0f5f8))



## [3.0.1](https://github.com/hei-school/poja-cli/compare/v3.0.0...v3.0.1) (2023-11-14)


### Bug Fixes

* typo in release-version.yml ([c946fa9](https://github.com/hei-school/poja-cli/commit/c946fa9bfb3f108d23988711bbbdd894fa61fcc5))



# [3.0.0](https://github.com/hei-school/poja-cli/compare/v2.5.0...v3.0.0) (2023-11-14)


### Bug Fixes

* --with-gen-clients ([0b2d2ca](https://github.com/hei-school/poja-cli/commit/0b2d2ca502c9ceac613dad44943a03a397ebd8b0))
* DatasourceConf for handling optional appProp when --with-postgres ([9de177f](https://github.com/hei-school/poja-cli/commit/9de177feb05cc6026aa3369d095ff869ca034abe))
* touch doc/api.yml ([1aa0a65](https://github.com/hei-school/poja-cli/commit/1aa0a65a870887a2a4f632b7fdc974f4d31b21c4))


### Features

* --with-own-vpc ([d5418e1](https://github.com/hei-school/poja-cli/commit/d5418e1c7e1d6c79c84ac55b2436f8cb5c864a57))
* EnvConf is optional ([62b30b6](https://github.com/hei-school/poja-cli/commit/62b30b6ebd770a55a9a6e723781aba5f3cf4f51d))


### BREAKING CHANGES

* default value of --with-gen-clients is false
* default value of --with-own-vpc is false



# [2.5.0](https://github.com/hei-school/poja-cli/compare/v2.4.3...v2.5.0) (2023-11-14)


### Features

* --with-publish-to-npm-registry ([3ae4850](https://github.com/hei-school/poja-cli/commit/3ae4850f8400e7e23a0d2e6b40bb4900222e40cf))



## [2.4.3](https://github.com/hei-school/poja-cli/compare/v2.4.2...v2.4.3) (2023-11-10)


### Bug Fixes

* do not save heading whitespace in varenvs ([d31f0fd](https://github.com/hei-school/poja-cli/commit/d31f0fd21b29603ab1ca214fa26038ec85304b09))



## [2.4.2](https://github.com/hei-school/poja-cli/compare/v2.4.1...v2.4.2) (2023-11-10)


### Bug Fixes

* allow spring-web in mailbox for instantions like spring-secu ([c9e8d46](https://github.com/hei-school/poja-cli/commit/c9e8d46d6c99677a38858ac0e768ab584a932194))



## [2.4.1](https://github.com/hei-school/poja-cli/compare/v2.4.0...v2.4.1) (2023-11-10)


### Bug Fixes

* --jacoco-min-coverage is a string ([085b676](https://github.com/hei-school/poja-cli/commit/085b676f854f73bebf3b6297cac3d1555914c7b8))



# [2.4.0](https://github.com/hei-school/poja-cli/compare/v2.3.0...v2.4.0) (2023-11-10)


### Features

* EnvConf for project-specific env vars ([da19a48](https://github.com/hei-school/poja-cli/commit/da19a48636fba36a9cede31fb82832c1c0c8d2c8))



# [2.3.0](https://github.com/hei-school/poja-cli/compare/v2.2.0...v2.3.0) (2023-11-10)


### Features

* make jacoco min coverage configurable ([6e78078](https://github.com/hei-school/poja-cli/commit/6e780788e6b974f8543f77dd6aeeb5b388922b39))



# [2.2.0](https://github.com/hei-school/poja-cli/compare/v2.1.0...v2.2.0) (2023-11-10)


### Bug Fixes

* revert "feat: rm writing permission on generated files" ([1e03204](https://github.com/hei-school/poja-cli/commit/1e0320466370123a61c531beab89f71c8597a1af))


### Features

* publish to mvn local and gen ts-axios ([9bb4ccc](https://github.com/hei-school/poja-cli/commit/9bb4cccce72d3650f0d5db3addca4afd79ab6c18))



# [2.1.0](https://github.com/hei-school/poja-cli/compare/v2.0.4...v2.1.0) (2023-11-09)


### Bug Fixes

* version.yml --> poja-version.yml ([7039e9b](https://github.com/hei-school/poja-cli/commit/7039e9b3031f67b9e4c4b59055526a418350f3a3))


### Features

* rm writing permission on generated files ([bb7679a](https://github.com/hei-school/poja-cli/commit/bb7679a72c9e14e92bd47a887cf91b95741a1d76))



## [2.0.4](https://github.com/hei-school/poja-cli/compare/v2.0.2...v2.0.4) (2023-11-09)


### Bug Fixes

* correctly set package name in build.gradle ([12f1275](https://github.com/hei-school/poja-cli/commit/12f1275b73b38e4098c498af4f656d4c300f6717))
* with_postgres is a string in cli ([1d831a1](https://github.com/hei-school/poja-cli/commit/1d831a131270d509a4a10cf453e47c4bf2b07243))



## [2.0.2](https://github.com/hei-school/poja-cli/compare/v2.0.1...v2.0.2) (2023-11-08)


### Bug Fixes

* no poja-base in db env vars ([124ac36](https://github.com/hei-school/poja-cli/commit/124ac3641f0552e9b13bdadbfd2f67ca1a0c57d0))



## [2.0.1](https://github.com/hei-school/poja-cli/compare/v2.0.0...v2.0.1) (2023-11-08)


### Bug Fixes

* java-deps: swagger and and hibernate-types ([d963481](https://github.com/hei-school/poja-cli/commit/d963481007debb6f68a4773af273ea71c5f0139b))



# [2.0.0](https://github.com/hei-school/poja-cli/compare/v1.4.0...v2.0.0) (2023-11-08)

### BREAKING CHANGES

* downgrade to Spring 2

### Features

* openapi-gen Java client

### Bug Fixes

* no cd-domain


# [1.4.0](https://github.com/hei-school/poja-cli/compare/v1.3.0...v1.4.0) (2023-11-07)


### Features

* --custom-java-env-vars ([c51e18b](https://github.com/hei-school/poja-cli/commit/c51e18b65a2c0a0102b213f733c4791fafc6d31e))
* --with-postgres ([a684996](https://github.com/hei-school/poja-cli/commit/a684996550b4a6b95bc21fcd224db6efdb4d0ade))



# [1.3.0](https://github.com/hei-school/poja-cli/compare/v1.2.1...v1.3.0) (2023-11-05)


### Features

* custom Java deps ([ac9676f](https://github.com/hei-school/poja-cli/commit/ac9676f0f5bcb1faa1246a5f18c1890be9223f39))



## [1.2.1](https://github.com/hei-school/poja-cli/compare/v1.2.0...v1.2.1) (2023-11-05)


### Bug Fixes

* manually add missing entries to CHANGELOG.md ([4fdf063](https://github.com/hei-school/poja-cli/commit/4fdf063387eb259908b0d05e2910e15a052bbc6b))



# [1.2.0](https://github.com/hei-school/poja-cli/compare/v1.1.0...v1.2.0) (2023-11-05)


### Features

* reflection for event routing ([ab01a26](https://github.com/hei-school/poja-cli/commit/ab01a2621289e9fe5e3862048cb9baee0cd2927b))



# [1.1.0](https://github.com/hei-school/poja-cli/compare/v1.0.0...v1.1.0) (2023-11-04)


### Features

* health check on async stack ([d307cb6](https://github.com/hei-school/poja-cli/commit/d307cb68c856f44913925ae847adb800aedda7f9))

* format.sh using Google Java Format
    
* fail tests under 0.8 line cov


# [1.0.0](https://github.com/hei-school/poja-cli/compare/v0.3.0...v1.0.0) (2023-11-03)


### Features

* event stack ([f186d82](https://github.com/hei-school/poja-cli/commit/f186d82ed886d16c5f6786186092e7e465466067))

* disable flyway migration during Mailbox

* push messages by batch of 5

### Bug Fixes

* SpringApp is Poja, not Mailbox

### BREAKING CHANGES

* POJA subnets must be private


# [0.3.0](https://github.com/hei-school/poja-cli/compare/v0.2.0...v0.3.0) (2023-11-02)


### Bug Fixes

* do not override target README ([b345b5c](https://github.com/hei-school/poja-cli/commit/b345b5c61fec507059d60d27221f1e4ed429cbe9))


### Features

* --package-full-name ([1ade51a](https://github.com/hei-school/poja-cli/commit/1ade51acbb6eb55189263134d68c7b796a756f5c))



# [0.2.0](https://github.com/hei-school/poja-cli/compare/v0.1.4...v0.2.0) (2023-11-02)


### Features

* configurable scaling down timeout for prod db ([35e31da](https://github.com/hei-school/poja-cli/commit/35e31da756706a7100b5d3817f5270f3da58fbbe))



## [0.1.4](https://github.com/hei-school/poja-cli/compare/v0.1.3...v0.1.4) (2023-11-01)


### Bug Fixes

* save conf after gen ([b2d57b9](https://github.com/hei-school/poja-cli/commit/b2d57b98048b23bd34d8f2a5291d0928cefd2068))



## [0.1.3](https://github.com/hei-school/poja-cli/compare/v0.1.2...v0.1.3) (2023-11-01)


### Bug Fixes

* do not print final gen output ([631d1f3](https://github.com/hei-school/poja-cli/commit/631d1f3efaaf2a38282e00a988f6f84d66efde80))



## [0.1.2](https://github.com/hei-school/poja-cli/compare/v0.1.1...v0.1.2) (2023-11-01)


### Bug Fixes

* pyyaml is a main dependency ([ee0e054](https://github.com/hei-school/poja-cli/commit/ee0e05469f0fa949901f4efcc321fdbb4ce73052))



## [0.1.1](https://github.com/hei-school/poja-cli/compare/v0.1.0...v0.1.1) (2023-11-01)


### Bug Fixes

* pretty print progression ([e673ce3](https://github.com/hei-school/poja-cli/commit/e673ce3a819c75ea35d1ebaee0d2530774db22da))



# [0.1.0](https://github.com/hei-school/poja-cli/compare/25a899959c3e74d8fbbef6840629c2c3a3c18cf1...v0.1.0) (2023-11-01)


### Features

* poja.gen ([25a8999](https://github.com/hei-school/poja-cli/commit/25a899959c3e74d8fbbef6840629c2c3a3c18cf1))
* py package ([5cf4f58](https://github.com/hei-school/poja-cli/commit/5cf4f58218cc6394704d1b3011be40933e19a35d))




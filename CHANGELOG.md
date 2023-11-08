## [2.0.3](https://github.com/hei-school/poja-cli/compare/v2.0.2...v2.0.3) (2023-11-08)


### Bug Fixes

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




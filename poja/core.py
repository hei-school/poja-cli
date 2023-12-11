import poja.mygit as mygit
import shutil
import poja.sed as sed
from poja.myrich import print_title, print_normal, print_banner
from poja.version import get_version
from poja.vpcscoped import set_vpc_scoped_resources
from poja.genclients import set_gen_clients
import yaml
import os
import platform
from pathlib import Path

GIT_URL = "https://github.com/hei-school/poja"
GIT_TAG_OR_COMMIT = "e62789f"

DEFAULT_GROUP_NAME = "school.hei"
DEFAULT_PACKAGE_FULL_NAME = DEFAULT_GROUP_NAME + ".poja"


def gen(
    app_name,
    region="eu-west-3",
    with_own_vpc="false",
    ssm_sg_id=None,
    ssm_subnet1_id=None,
    ssm_subnet2_id=None,
    ses_source="noreply@nowhere.com",
    with_swagger_ui="false",
    package_full_name=DEFAULT_PACKAGE_FULL_NAME,
    custom_java_repositories=None,
    custom_java_deps=None,
    custom_java_env_vars=None,
    with_gen_clients="false",
    with_postgres="true",
    output_dir=None,
    jacoco_min_coverage="0.8",
    with_publish_to_npm_registry="false",
    ts_client_default_openapi_server_url="",
    ts_client_api_url_env_var_name="",
    frontal_memory=512,
    worker_memory=1024,
    worker_batch=5,
):
    if output_dir is None:
        output_dir = app_name

    print_banner("POJA v" + get_version())

    print_title("Checkout base repository...")
    print_normal("git_url=%s" % GIT_URL)
    print_normal("git_tag=%s" % GIT_TAG_OR_COMMIT)
    temp_dir = mygit.checkout(GIT_URL, GIT_TAG_OR_COMMIT, no_git=True)
    print_normal("temp_dir=%s" % temp_dir)

    print_title("Handle arguments...")
    exclude = "*.jar"
    print_normal("region")
    sed.find_replace(temp_dir, "<?aws-region>", region, exclude)
    print_normal("ses_source")
    sed.find_replace(temp_dir, "<?aws-ses-source>", ses_source, exclude)

    print_normal("frontal_memory")
    sed.find_replace(temp_dir, "<?frontal-memory>", str(frontal_memory), exclude)
    print_normal("worker_memory")
    sed.find_replace(temp_dir, "<?worker-memory>", str(worker_memory), exclude)
    print_normal("worker_batch")
    sed.find_replace(temp_dir, "<?worker-batch>", str(worker_batch), exclude)

    print_normal("with_own_vpc")
    set_vpc_scoped_resources(
        with_own_vpc, ssm_sg_id, ssm_subnet1_id, ssm_subnet2_id, temp_dir, exclude
    )

    print_normal("with_gen_clients")
    set_gen_clients(with_gen_clients, temp_dir, exclude)

    print_normal("with_swagger_ui")
    if with_swagger_ui == "true":
        springdoc_java_dep = "implementation 'org.springdoc:springdoc-openapi-ui:1.7.0'"
    else:
        springdoc_java_dep = ""
    sed.find_replace(temp_dir, "<?java-deps-springdoc>", springdoc_java_dep, exclude)

    print_normal("package_full_name")
    sed.find_replace(temp_dir, DEFAULT_PACKAGE_FULL_NAME, package_full_name, exclude)
    sed.find_replace(
        temp_dir,
        DEFAULT_GROUP_NAME,
        group_name_from_package_full_name(package_full_name),
        exclude,
    )
    print_normal("custom_java_repositories")
    java_repositories = replace_with_file_content(
        temp_dir, "<?java-repositories>", custom_java_repositories, exclude
    )
    set_package_dirs(temp_dir, package_full_name, "main")
    set_package_dirs(temp_dir, package_full_name, "test")
    print_normal("custom_java_deps")
    java_deps = replace_with_file_content(
        temp_dir, "<?java-deps>", custom_java_deps, exclude
    )
    print_normal("custom_java_env_vars")
    indent = "        "
    java_env_vars = replace_with_file_content(
        temp_dir, "<?java-env-vars>", custom_java_env_vars, exclude, joiner=indent
    )

    print_normal("with_postgres")
    set_postgres(with_postgres, temp_dir, exclude)
    print_normal("app_name")
    sed.find_replace(temp_dir, "<?app-name>", app_name, exclude)
    print_normal("jacoco_min_coverage")
    sed.find_replace(
        temp_dir, "<?jacoco-min-coverage>", str(jacoco_min_coverage), exclude
    )
    if with_publish_to_npm_registry == "true":
        print_normal("ts_client_default_openapi_server_url")
        sed.find_replace(
            temp_dir,
            "<?ts-client-default-openapi-server-url>",
            ts_client_default_openapi_server_url,
            exclude,
        )
        print_normal("ts_client_api_url_env_var_name")
        sed.find_replace(
            temp_dir,
            "<?ts-client-api-url-env-var-name>",
            ts_client_api_url_env_var_name,
            exclude,
        )
    else:
        os.remove("%s/.github/workflows/publish-client.yml" % temp_dir)

    print_title("Save conf...")
    save_conf(
        temp_dir,
        app_name,
        region,
        with_own_vpc,
        ssm_sg_id,
        ssm_subnet1_id,
        ssm_subnet2_id,
        ses_source,
        with_swagger_ui,
        package_full_name,
        java_repositories,
        java_deps,
        java_env_vars,
        with_gen_clients,
        with_postgres,
        jacoco_min_coverage,
        ts_client_default_openapi_server_url,
        ts_client_api_url_env_var_name,
        frontal_memory,
        worker_memory,
        worker_batch,
    )
    print_normal("poja.yml")

    print_title("Rm project-specific files...")
    print_normal("README.md")
    os.remove(temp_dir + "/README.md")
    print_normal("application.properties")
    os.remove(temp_dir + "/src/main/resources/application.properties")
    print_normal("gradle.properties")
    os.remove(temp_dir + "/gradle.properties")

    print_title("Format...")
    if "Windows" in platform.system():
        os.system("cd /D %s && format.bat" % temp_dir)
    else:
        os.system("cd %s && ./format.sh" % temp_dir)

    print_title("Copy to output dir...")
    shutil.copytree(temp_dir, output_dir, dirs_exist_ok=True)

    print_title("Client generation...")
    print_normal("doc/api.yml")
    # create doc/ and doc/api.yml if not exist
    Path("%s/doc" % output_dir).mkdir(parents=True, exist_ok=True)
    open("%s/doc/api.yml" % output_dir, "w+")

    print_title("... all done!")


def group_name_from_package_full_name(package_full_name):
    package_full_name_parts = get_package_full_name_parts(package_full_name)
    return package_full_name_parts[0] + "." + package_full_name_parts[1]


def save_conf(
    temp_dir,
    app_name,
    region,
    with_own_vpc,
    ssm_sg_id,
    ssm_subnet1_id,
    ssm_subnet2_id,
    ses_source,
    with_swagger_ui,
    package_full_name,
    custom_java_repositories,
    custom_java_deps,
    custom_java_env_vars,
    with_gen_clients,
    with_postgres,
    jacoco_min_coverage,
    ts_client_default_openapi_server_url,
    ts_client_api_url_env_var_name,
    frontal_memory,
    worker_memory,
    worker_batch,
):
    custom_java_repositories_filename = "poja-custom-java-repositories.txt"
    custom_java_deps_filename = "poja-custom-java-deps.txt"
    custom_java_env_vars_filename = "poja-custom-java-env-vars.txt"
    conf = {
        "cli_version": get_version(),
        "app_name": app_name,
        "region": region,
        "with_own_vpc": with_own_vpc,
        "ssm_sg_id": ssm_sg_id,
        "ssm_subnet1_id": ssm_subnet1_id,
        "ssm_subnet2_id": ssm_subnet2_id,
        "ses_source": ses_source,
        "with_swagger_ui": with_swagger_ui,
        "package_full_name": package_full_name,
        "custom_java_repositories": custom_java_repositories_filename,
        "custom_java_deps": custom_java_deps_filename,
        "custom_java_env_vars": custom_java_env_vars_filename,
        "with_gen_clients": with_gen_clients,
        "with_postgres": with_postgres,
        "jacoco-min-coverage": jacoco_min_coverage,
        "ts_client_default_openapi_server_url": ts_client_default_openapi_server_url,
        "ts_client_api_url_env_var_name": ts_client_api_url_env_var_name,
        "frontal_memory": frontal_memory,
        "worker_memory": worker_memory,
        "worker_batch": worker_batch,
    }
    with open(temp_dir + "/poja.yml", "w") as conf_file:
        yaml.dump(conf, conf_file)

    print_normal(custom_java_repositories_filename)
    with open(
        "%s/%s" % (temp_dir, custom_java_repositories_filename), "w"
    ) as custom_java_repositories_file:
        custom_java_repositories_file.write(custom_java_repositories)

    print_normal(custom_java_deps_filename)
    with open(
        "%s/%s" % (temp_dir, custom_java_deps_filename), "w"
    ) as custom_java_deps_file:
        custom_java_deps_file.write(custom_java_deps)

    print_normal(custom_java_env_vars_filename)
    with open(
        "%s/%s" % (temp_dir, custom_java_env_vars_filename), "w"
    ) as custom_java_env_vars_file:
        custom_java_env_vars_file.write(
            "\n".join([s.strip() for s in custom_java_env_vars.split("\n")])
        )


def replace_with_file_content(
    project_dir, to_replace, replacement_filepath, exclude, joiner=""
):
    if replacement_filepath is None:
        content = ""
    else:
        file = open(replacement_filepath, "r")
        content = joiner.join(file.readlines())
    sed.find_replace(project_dir, to_replace, content, exclude)
    return content


def set_postgres(with_postgres, temp, exclude):
    if with_postgres == "true":
        post_gres_env_vars = """DATABASE_URL: !Sub '{{resolve:ssm:/<?app-name>/${Env}/db/url}}'
        DATABASE_USERNAME: !Sub '{{resolve:ssm:/<?app-name>/${Env}/db/username}}'
        DATABASE_PASSWORD: !Sub '{{resolve:ssm:/<?app-name>/${Env}/db/password}}'"""
    else:
        post_gres_env_vars = ""
        os.remove("%s/.github/workflows/cd-storage-database.yml" % temp)
    sed.find_replace(
        temp,
        "<?postgres-env-vars>",
        post_gres_env_vars,
        exclude,
    )


def set_package_dirs(temp_dir, package_full_name, scope):
    package_full_name_parts = get_package_full_name_parts(package_full_name)
    default_package_full_name_parts = DEFAULT_PACKAGE_FULL_NAME.split(".")
    os.rename(
        "%s/src/%s/java/%s" % (temp_dir, scope, default_package_full_name_parts[0]),
        "%s/src/%s/java/%s" % (temp_dir, scope, package_full_name_parts[0]),
    )
    os.rename(
        "%s/src/%s/java/%s/%s"
        % (
            temp_dir,
            scope,
            package_full_name_parts[0],
            default_package_full_name_parts[1],
        ),
        "%s/src/%s/java/%s/%s"
        % (temp_dir, scope, package_full_name_parts[0], package_full_name_parts[1]),
    )
    os.rename(
        "%s/src/%s/java/%s/%s/%s"
        % (
            temp_dir,
            scope,
            package_full_name_parts[0],
            package_full_name_parts[1],
            default_package_full_name_parts[2],
        ),
        "%s/src/%s/java/%s/%s/%s"
        % (
            temp_dir,
            scope,
            package_full_name_parts[0],
            package_full_name_parts[1],
            package_full_name_parts[2],
        ),
    )


def get_package_full_name_parts(package_full_name):
    package_full_name_parts = package_full_name.split(".")
    if len(package_full_name_parts) != 3:
        raise Exception(
            "package_full_name must exactly have 3 parts such as com.company.base"
        )
    return package_full_name_parts

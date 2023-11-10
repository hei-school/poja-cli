import poja.mygit as mygit
import shutil
import poja.sed as sed
from poja.myrich import print_title, print_normal, print_banner
from poja.version import get_version
import yaml
import os

GIT_URL = "https://github.com/hei-school/poja"
GIT_TAG_OR_COMMIT = "a649900"

DEFAULT_GROUP_NAME = "school.hei"
DEFAULT_PACKAGE_FULL_NAME = DEFAULT_GROUP_NAME + ".poja"

def gen(
    app_name,
    region,
    ssm_sg_id,
    ssm_subnet1_id,
    ssm_subnet2_id,
    package_full_name=DEFAULT_PACKAGE_FULL_NAME,
    custom_java_deps=None,
    custom_java_env_vars=None,
    with_postgres="true",
    output_dir=None,
    jacoco_min_coverage=0.8,
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
    print_normal("ssm_sg_id")
    sed.find_replace(temp_dir, "<?ssm-param-sg-id>", ssm_sg_id, exclude)
    print_normal("ssm_subnet1_id")
    sed.find_replace(temp_dir, "<?ssm-param-name-subnet1-id>", ssm_subnet1_id, exclude)
    print_normal("ssm_subnet2_id")
    sed.find_replace(temp_dir, "<?ssm-param-name-subnet2-id>", ssm_subnet2_id, exclude)
    print_normal("package_full_name")
    sed.find_replace(temp_dir, DEFAULT_PACKAGE_FULL_NAME, package_full_name, exclude)
    sed.find_replace(
        temp_dir,
        DEFAULT_GROUP_NAME,
        group_name_from_package_full_name(package_full_name),
        exclude,
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
    sed.find_replace(temp_dir, "<?jacoco-min-coverage>", jacoco_min_coverage, exclude)

    print_title("Save conf...")
    save_conf(
        temp_dir,
        app_name,
        region,
        ssm_sg_id,
        ssm_subnet1_id,
        ssm_subnet2_id,
        package_full_name,
        java_deps,
        java_env_vars,
        with_postgres,
        jacoco_min_coverage
    )
    print_normal("poja.yml")

    print_title("Rm project-specific files...")
    print_normal("README.md")
    os.remove(temp_dir + "/README.md")
    print_normal("application.properties")
    os.remove(temp_dir + "/src/main/resources/application.properties")

    print_title("Format...")
    os.system("cd %s && ./format.sh" % temp_dir)

    print_title("Copy to output dir...")
    shutil.copytree(temp_dir, output_dir, dirs_exist_ok=True)

    print_title("... all done!")


def group_name_from_package_full_name(package_full_name):
    package_full_name_parts = get_package_full_name_parts(package_full_name)
    return package_full_name_parts[0] + "." + package_full_name_parts[1]


def save_conf(
    temp_dir,
    app_name,
    region,
    ssm_sg_id,
    ssm_subnet1_id,
    ssm_subnet2_id,
    package_full_name,
    custom_java_deps,
    custom_java_env_vars,
    with_postgres,
    jacoco_min_coverage,
):
    custom_java_deps_filename = "poja-custom-java-deps.txt"
    custom_java_env_vars_filename = "poja-custom-java-env-vars.txt"
    conf = {
        "cli_version": get_version(),
        "app_name": app_name,
        "region": region,
        "ssm_sg_id": ssm_sg_id,
        "ssm_subnet1_id": ssm_subnet1_id,
        "ssm_subnet2_id": ssm_subnet2_id,
        "package_full_name": package_full_name,
        "custom_java_deps": custom_java_deps_filename,
        "custom_java_env_vars": custom_java_env_vars_filename,
        "with_postgres": with_postgres,
        "jacoco-min-coverage": jacoco_min_coverage
    }
    with open(temp_dir + "/poja.yml", "w") as conf_file:
        yaml.dump(conf, conf_file)

    print_normal(custom_java_deps_filename)
    with open(
        "%s/%s" % (temp_dir, custom_java_deps_filename), "w"
    ) as custom_java_deps_file:
        custom_java_deps_file.write(custom_java_deps)

    print_normal(custom_java_env_vars_filename)
    with open(
        "%s/%s" % (temp_dir, custom_java_env_vars_filename), "w"
    ) as custom_java_env_vars_file:
        custom_java_env_vars_file.write(custom_java_env_vars)


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
        os.remove("%s/.github/workflows/cd-storage.yml" % temp)
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

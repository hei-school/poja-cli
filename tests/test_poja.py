import poja
from filecmp import dircmp
import os.path


def test_base():
    output_dir = "test-poja-base"
    poja.gen(
        "poja-base",
        region="eu-west-3",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/private1/id",
        ssm_subnet2_id="/poja/subnet/private2/id",
        package_full_name="com.company.base",
        output_dir=output_dir,
        jacoco_min_coverage="0.9",
    )
    assert is_dir_superset_of("oracle-poja-base", output_dir)


def test_base_without_postgres():
    output_dir = "test-poja-base-without-postgres"
    poja.gen(
        "poja-base-without-postgres",
        region="eu-west-3",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/private1/id",
        ssm_subnet2_id="/poja/subnet/private2/id",
        package_full_name="com.company.base",
        output_dir=output_dir,
        with_postgres="false",
        jacoco_min_coverage="0.9",
    )
    assert is_dir_superset_of("oracle-poja-base-without-postgres", output_dir)


def test_base_with_custom_java_deps():
    output_dir = "test-poja-base-with-aws-ses"
    poja.gen(
        "poja-base",
        region="eu-west-3",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/private1/id",
        ssm_subnet2_id="/poja/subnet/private2/id",
        package_full_name="com.company.base",
        custom_java_deps="custom-java-deps-aws-ses.txt",
        output_dir=output_dir,
        jacoco_min_coverage="0.9",
    )
    assert is_dir_superset_of("oracle-poja-base-with-aws-ses", output_dir)


def test_base_with_custom_java_env_vars():
    output_dir = "test-poja-base-with-java-env-vars"
    poja.gen(
        "poja-base-with-java-env-vars",
        region="eu-west-3",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/private1/id",
        ssm_subnet2_id="/poja/subnet/private2/id",
        package_full_name="com.company.base",
        with_postgres="false",
        custom_java_env_vars="custom-java-env-vars.txt",
        output_dir=output_dir,
        jacoco_min_coverage="0.9",
    )
    assert is_dir_superset_of("oracle-poja-base-with-java-env-vars", output_dir)


def test_base_with_script_to_publish_to_npm_registry():
    output_dir = "test-poja-base-with-publication-to-npm-registry"
    poja.gen(
        "poja-base-with-publication-to-npm-registry",
        region="eu-west-3",
        ssm_sg_id="/poja/sg/id",
        ssm_subnet1_id="/poja/subnet/private1/id",
        ssm_subnet2_id="/poja/subnet/private2/id",
        package_full_name="com.company.base",
        with_postgres="false",
        custom_java_env_vars="custom-java-env-vars.txt",
        output_dir=output_dir,
        jacoco_min_coverage="0.9",
        with_publish_to_npm_registry="true",
        ts_client_default_openapi_server_url="http://localhost",
        ts_client_api_url_env_var_name="CLIENT_API_URL",
    )
    assert is_dir_superset_of(
        "oracle-poja-base-with-publication-to-npm-registry", output_dir
    )


def is_dir_superset_of(superset_dir, subset_dir):
    compared = dircmp(superset_dir, subset_dir)
    print(
        "superset_only=%s, subset_only=%s, both=%s, incomparables=%s"
        % (
            compared.left_only,
            compared.right_only,
            compared.diff_files,
            compared.funny_files,
        ),
    )
    if compared.right_only or compared.diff_files or compared.funny_files:
        return False
    for subdir in compared.common_dirs:
        if not is_dir_superset_of(
            os.path.join(superset_dir, subdir), os.path.join(subset_dir, subdir)
        ):
            return False
    return True

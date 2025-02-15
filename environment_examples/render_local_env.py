from jinja2 import Environment, FileSystemLoader
import shlex


def create_double_quoted_list_of_strings(l):
    return ",".join([f'"{s}"' for s in l])


def create_spaced_list_of_strings(l):
    return " ".join([f'"{s}"' for s in l])


var_dict = {
    "environment_name": "local-2023b",
    "project_name": "lund-vision-group-cave",
    "pcg_bucket_name": "heinze-lab",
    "depl_region": "europe-west3",
    "depl_zone": "europe-west3-b",
    "dns_zone": "cave-2023b-braininbrain-org",
    "domain_name": "cave-2023b.braininbrain.org",
    "letsencrypt_email": "kevin@tedore.com",
    "supported_datastack_list": ["megalopta_NO_R_v4", "megalopta_PB1_v2", "megalopta_NO_test_0713", "megalopta_NO_test_0713a", "megalopta_NO", "dacke_lamarckii_NO_R"],
    "data_project_name": "lund-vision-group-cave",
    "data_project_region": "europe-west3",
    "docker_repository": "docker.io/caveconnectome",
    "add_dns_hostnames": ["local.cave.braininbrain.org"],
    "add_dns_zones": ["$DNS_ZONE", "cave-braininbrain-org"],
    "postgres_password": "4xynrttJ2A9IkhNFSw",
    "sql_instance_name": "daf-depl",
    "bigtable_instance_name": "pychunkedgraph",
    "add_storage_secrets": [],
    "mat_health_aligned_volume_name": "megalopta_NO",
    "mat_datastacks": "megalopta_NO_R_v4,megalopta_PB1_v2",
    "mat_beat_schedule": "${ENV_REPO_PATH}/my_mat_schedule.json",
    "pcg_graph_ids": "megalopta_NO_R_v4, megalopta_PB1_v2, megalopta_NO_test_0713, megalopta_NO_test_0713a, megalopta_NO, dacke_lamarckii_NO_R",
    "authservice_secret_key": "e!dBmxJ@V3KfbUsg@mQA8Ji8hURQ",
    "global_server": "global.connectomics.braininbrain.org",
    "guidebook_csrf_key": "Fih965^NwrjZpo15fE",
    "guidebook_datastack": "megalopta_NO_R_v4",
    "guidebook_expected_resolution": "10,10,50",
    "dash_secret_key": "E!8W&iL8KBu#EHG&DS",
    "dash_config_filename": "${ENV_REPO_PATH}/my_dash_config.py",
    "l2cache_config_filename": "${ENV_REPO_PATH}/my_l2cache_config.yml",
    "skeleton_cache_bucket": "gs://my_skeleton_cache_bucket",
    "proxy_map": "'datastack1': 'https://storage.googleapis.com/datastack1_imagery'}",
    "ann_excluded_permission_groups": ["default"],
    "redis_password": "PoZjTzxr7BunrcU_KNj!",
    "slack_token": "bp23hmTaQ0uFny2RtkyRUvaD",
    "slack_channel": "braininbraingroup.slack.com",
}

# Additional modifications to parameters and checks
var_dict["supported_datastacks"] = create_double_quoted_list_of_strings(
    var_dict["supported_datastack_list"]
)
var_dict["ann_excluded_permission_groups"] = create_double_quoted_list_of_strings(
    var_dict["ann_excluded_permission_groups"]
)
var_dict["dns_hostnames"] = create_spaced_list_of_strings(
    ["$DNS_HOSTNAME"] + var_dict["add_dns_hostnames"]
)
var_dict["dns_zones"] = create_spaced_list_of_strings(
    ["$DNS_ZONE"] + var_dict["add_dns_hostnames"]
)
var_dict["pcg_service_account_addon"] = " ".join(
    [
        "".join(["--from-file=", sec, "=${ADD_STORAGE_SECRET_FOLDER}/", sec])
        for sec in var_dict["add_storage_secrets"]
    ]
)
var_dict["postgres_password"] = shlex.quote(var_dict["postgres_password"])


# Load and render template
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("local_env_template.sh")
rendered_template = template.render(var_dict)

# Write rendered tempalte
with open(f"{var_dict['environment_name']}.sh", "w") as f:
    f.write(rendered_template)

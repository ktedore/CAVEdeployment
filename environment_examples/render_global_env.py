from jinja2 import Environment, FileSystemLoader
import shlex


def create_spaced_list_of_strings(l):
    return " ".join(
        [
            f'"{s}"' if s.startswith("$") and not s.startswith("${") else f"{s}"
            for s in l
        ]
    )


var_dict = {
    "environment_name": "global-2025",
    "project_name": "heinze-lab-daf-global",
    "depl_region": "europe-west3",
    "depl_zone": "europe-west3-b",
    "dns_zone": "global-staging-connectomics-braininbrain-org",
    "domain_name": "global-staging.connectomics.braininbrain.org",
    "letsencrypt_email": "kevin@tedore.com",
    "docker_repository": "docker.io/caveconnectome",
    "add_dns_hostnames": [
        "global.connectomics.braininbrain.org",
    ],
    "add_dns_zones": [
        "connectomics-braininbrain-org"
    ],
    "postgres_password": "adBIihbvcQ29DSfedjq",
    "sql_instance_name": "cave-global",
    "add_storage_secrets": [],
    "global_server": "global.connectomics.braininbrain.org",
    "infoservice_csrf_key": "U7Kcu6Fr7nxeFc6PTJ",
    "infoservice_secret_key": "JRSuzTiN3qxnVaEx1i",
    "authservice_secret_key": "JRSuzTiN3q#nVaEA1i",
    "ngl_link_db_table_name": "neuroglancerjsondb",
    "default_admins": [
        ["kevin@tedore.com", "Kevin Tedore", "Admin1Tech"],
        ["stanley.heinze@gmx.de", "Stanley Heinze", "Admin2PI"],
        ["lund.neuroscience@gmail.com", "Kevin Tedore", "Admin2Tech"],
    ],
}

# Additional modifications to parameters and checks
var_dict["dns_hostnames"] = create_spaced_list_of_strings(
    ["$DNS_HOSTNAME"] + var_dict["add_dns_hostnames"]
)
var_dict["dns_zones"] = create_spaced_list_of_strings(
    ["$DNS_ZONE"] + var_dict["add_dns_zones"]
)
var_dict["postgres_password"] = shlex.quote(var_dict["postgres_password"])

# Load and render template
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("global_env_template.sh")
rendered_template = template.render(var_dict)

# Write rendered tempalte
with open(f"{var_dict['environment_name']}.sh", "w") as f:
    f.write(rendered_template)

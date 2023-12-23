from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="my_db_conn",
        profile_args={"schema": "my_schema"},
    ),
)

DbtTaskGroup(
    project_config=ProjectConfig("/home/abresh/Desktop/CSV/traffic_data"),
    profile_config=profile_config,
    default_args={"retries": 2},
)
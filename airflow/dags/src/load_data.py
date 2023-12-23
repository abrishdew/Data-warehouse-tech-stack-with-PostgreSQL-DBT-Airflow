




def load_data(**kwargs):
    """
    Read the json file from the /data/ directory and then load
    """
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids='transform_data')
    transformed_data = transformed_data + "to database"
    print(transformed_data)
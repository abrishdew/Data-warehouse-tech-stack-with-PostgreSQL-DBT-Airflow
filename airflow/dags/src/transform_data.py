




def transform_data (**kwargs):
    """
    Read the json file from the /data/ directory and then transform   
    """
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='get_data')
    data = data+ "transformed data"
    return data

    
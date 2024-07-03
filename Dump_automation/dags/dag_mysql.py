from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.bash import BashOperator


def chk_space(ti):
    class InsufficientDiskSpaceError(Exception):
        """Exception raised when there is not enough disk space."""
        pass

    estimated_size_mb = ti.xcom_pull(task_ids='estimate_table_size', key='return_value')
    if estimated_size_mb:
        estimated_size_mb = estimated_size_mb[0][0]


    available_space = ti.xcom_pull(task_ids='get_space', key='return_value')
    if available_space:
        available_space_str = available_space[0]

        if 'G' in available_space_str:
            available_space_mb = float(available_space_str.replace('G', '')) * 1024
        elif 'M' in available_space_str:
            available_space_mb = float(available_space_str.replace('M', ''))
        elif 'K' in available_space_str:
            available_space_mb = float(available_space_str.replace('K', '')) / 1024
        else:
            available_space_mb = float(available_space_str)
    else:
        available_space_mb = 0


    if available_space_mb > estimated_size_mb:
        print("Insufficient disk space.")
        return 1/0
    else:
        print("Sufficient disk space.")
        return True


default_args = {
    'owner': 'bses',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_space',
    default_args=default_args,
    start_date=datetime(2024, 5, 1),
    schedule_interval='@daily'
) as dag:


    dump_table = BashOperator(
        task_id='dump_fc_account_master',
        bash_command="""
        mysqldump -h {{ params.host }} -u {{ params.user }} --password={{ params.password }} {{ params.database }} fc_account_master > /opt/airflow/dags/first.sql
        """,
        params={
            'host': 'host.docker.internal',  # Replace with your MySQL host or IP
            'user': 'root',   # Replace with your MySQL username
            'password': '12345678',  # Replace with your MySQL password
            'database': 'client_rw'  # Database name
        }
    )
    # restore_table = BashOperator(
    #     task_id='restore_fc_account_master',
    #     bash_command="""
    #         mysql -h {{ params.host }} -u {{ params.user }} --password={{ params.password }} {{ params.database }} < /opt/airflow/dags/first.sql
    #         """,
    #     params={
    #         'host': 'host.docker.internal',  # Replace with your MySQL host or IP
    #         'user': 'root',  # Replace with your MySQL username
    #         'password': '12345678',  # Replace with your MySQL password
    #         'database': 'fc_facts'  # Database name
    #     })

    get_space = BashOperator(
        task_id='get_space',
        bash_command = "df -h / | tail -1 | awk \'{print $4}\'",
        do_xcom_push=True,
    )
    check_space = PythonOperator(
        task_id='check_space',
        python_callable=chk_space,
    )
    estimate_size = MySqlOperator(
        task_id='estimate_table_size',
        mysql_conn_id='mysql_local',
        sql="""
            SELECT round(sum(data_length + index_length) / 1024 / 1024, 2)
            FROM information_schema.TABLES
            WHERE table_schema = 'client_rw' AND table_name = 'fc_account_master';
        """
    )

    estimate_size >> get_space >> check_space >> dump_table

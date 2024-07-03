from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator



default_args = {
    'owner': 'bses',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_tables',
    default_args=default_args,
    start_date=datetime(2024, 5, 1),
    schedule_interval='@daily'
) as dag:


    # dump_table = BashOperator(
    #     task_id='dump_fc_account_master',
    #     bash_command="""
    #     mysqldump -h {{ params.host }} -u {{ params.user }} --password={{ params.password }} {{ params.database }} fc_account_master > /opt/airflow/dags/first.sql
    #     """,
    #     params={
    #         'host': 'host.docker.internal',  # Replace with your MySQL host or IP
    #         'user': 'root',   # Replace with your MySQL username
    #         'password': '12345678',  # Replace with your MySQL password
    #         'database': 'test'  # Database name
    #     }
    # )
    restore_table = BashOperator(
        task_id='import_table1',
        bash_command="""
            mysql -h {{ params.host }} -u {{ params.user }} --password={{ params.password }} {{ params.database }} < /opt/airflow/dags/products.sql
           """,
        params={
            'host': 'host.docker.internal',  # Replace with your MySQL host or IP
            'user': 'root',  # Replace with your MySQL username
            'password': '12345678',  # Replace with your MySQL password
            'database': 'test'  # Database name
        })
    restore_table1 = BashOperator(
        task_id='import_table2',
        bash_command="""
                mysql -h {{ params.host }} -u {{ params.user }} --password={{ params.password }} {{ params.database }} < /opt/airflow/dags/product_category.sql
                """,
        params={
            'host': 'host.docker.internal',  # Replace with your MySQL host or IP
            'user': 'root',  # Replace with your MySQL username
            'password': '12345678',  # Replace with your MySQL password
            'database': 'test'  # Database name
        })
    restore_table2 = BashOperator(
        task_id='import_table3',
        bash_command="""
                mysql -h {{ params.host }} -u {{ params.user }} --password={{ params.password }} {{ params.database }} < /opt/airflow/dags/product_category_map.sql
                """,
        params={
            'host': 'host.docker.internal',  # Replace with your MySQL host or IP
            'user': 'root',  # Replace with your MySQL username
            'password': '12345678',  # Replace with your MySQL password
            'database': 'test'  # Database name
        })
    restore_table3 = BashOperator(
        task_id='import_table4',
        bash_command="""
                mysql -h {{ params.host }} -u {{ params.user }} --password={{ params.password }} {{ params.database }} < /opt/airflow/dags/report_table.sql
                """,
        params={
            'host': 'host.docker.internal',  # Replace with your MySQL host or IP
            'user': 'root',  # Replace with your MySQL username
            'password': '12345678',  # Replace with your MySQL password
            'database': 'test'  # Database name
        })
    restore_table4 = BashOperator(
        task_id='import_table5',
        bash_command="""
                mysql -h {{ params.host }} -u {{ params.user }} --password={{ params.password }} {{ params.database }} < /opt/airflow/dags/rw_transaction_data.sql
                """,
        params={
            'host': 'host.docker.internal',  # Replace with your MySQL host or IP
            'user': 'root',  # Replace with your MySQL username
            'password': '12345678',  # Replace with your MySQL password
            'database': 'test'  # Database name
        })



    restore_table >> restore_table1 >> restore_table2 >> restore_table3 >> restore_table4
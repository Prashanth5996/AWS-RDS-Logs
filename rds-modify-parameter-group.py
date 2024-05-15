import boto3

def modify_parameter_group_and_instance():
    rds = boto3.client('rds')
    instance_name = 'database-1'
    parameter_group_name = 'my-db-postres'
    
    # Modify RDS instance parameter group
    rds.modify_db_instance(
        DBInstanceIdentifier=instance_name,
        DBParameterGroupName=parameter_group_name,
        ApplyImmediately=True
    )
    
    # Reboot the RDS instance
    rds.reboot_db_instance(DBInstanceIdentifier=instance_name)

def lambda_handler(event, context):
    modify_parameter_group_and_instance()
    return {
        'statusCode': 200,
        'body': 'Parameter group modified and instance rebooted successfully!'
    }

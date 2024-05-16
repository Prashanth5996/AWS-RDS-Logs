import json
import boto3

def create_parameter_group():
    rds = boto3.client('rds')
    parameter_group_name = "my-db-postres"
    
    # Check if parameter group already exists
    existing_parameter_groups = rds.describe_db_parameter_groups(
        DBParameterGroupName=parameter_group_name
    )['DBParameterGroups']
    
    if not existing_parameter_groups:
        # Create parameter group if it doesn't exist
        rds.create_db_parameter_group(
            DBParameterGroupName=parameter_group_name,
            DBParameterGroupFamily='postgres16',
            Description='Parameter group for my-db PostgreSQL version 16'
        )
        
    # Modify parameter values
    parameters = [
        {"ParameterName": "log_connections", "ParameterValue": "1", "ApplyMethod": "immediate"},
        {"ParameterName": "log_statement", "ParameterValue": "all", "ApplyMethod": "immediate"},
        {"ParameterName": "log_destination", "ParameterValue": "stderr", "ApplyMethod": "immediate"},
        {"ParameterName": "log_disconnections", "ParameterValue": "1", "ApplyMethod": "immediate"},
        {"ParameterName": "log_hostname", "ParameterValue": "1", "ApplyMethod": "immediate"},
        {"ParameterName": "track_activities", "ParameterValue": "1", "ApplyMethod": "immediate"},
        {"ParameterName": "log_min_messages", "ParameterValue": "error", "ApplyMethod": "immediate"}
    ]
    
    # Apply parameters to parameter group
    rds.modify_db_parameter_group(
        DBParameterGroupName=parameter_group_name,
        Parameters=parameters
    )
    print("Parameter group modified successfully.")

def lambda_handler(event, context):
    create_parameter_group()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Parameter group created successfully!')
    }

print("Lambda function updated successfully.")

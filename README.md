# RDS-logs

# Step 1: Create an IAM Policy named rds-policy
add json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rds:DescribeDBInstances",
                "rds:ModifyDBInstance",
                "rds:RebootDBInstance"
            ],
            "Resource": "*"
        }
    ]
}
## IAM Policy

```json
{
    // This IAM policy allows specific actions on RDS instances.
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            // Allows describing RDS instances.
            "Action": [
                "rds:DescribeDBInstances",
                // Allows modifying RDS instances.
                "rds:ModifyDBInstance",
                // Allows rebooting RDS instances.
                "rds:RebootDBInstance"
            ],
            // Applies to all RDS instances.
            "Resource": "*"
        }
    ]
}

# Step 2: Create an IAM Role named rds-lambda
1. Selecting Lambda and attaching policies:
* AWSLambdaBasicExecutionRole
* AmazonRDSFullAccess
2. Adding the rds-policy to the role.

# Step 3: AWS Lambda Functions
# Lambda Function 1: create-parameter-group.py
   This Creates and modifies an RDS parameter group enable logs init and Apply the changes.

# Lambda Function 2: rds-modify-parameter-group.py
   This Lambda function attaches the parameter group to an RDS instance and reboots the instance.

# Result
now logs will be visible in loggroup with this name (/aws/rds/instance/database-1/postgresql) 

# Connections
![Connection-Status-Loaction](https://github.com/Prashanth5996/RDS-logs/assets/94959676/23ec3fc9-6475-4624-b530-f85a6a18bb1c)

# Select-Query
![Select-Query](https://github.com/Prashanth5996/RDS-logs/assets/94959676/48090d66-f080-4ec4-9055-286c73801998)

# Disconnections
![Disconnections](https://github.com/Prashanth5996/RDS-logs/assets/94959676/7ec7d733-3800-42b2-a2be-8119eba91693)



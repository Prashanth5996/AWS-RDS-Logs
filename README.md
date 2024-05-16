# RDS-logs

# Step 1: Create an IAM Policy named rds-policy
# 1. add json
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

# 3.now logs will be visible in loggroup with this name(/aws/rds/instance/database-1/postgresql) 


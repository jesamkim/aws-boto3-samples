# EventBridge 에서 CodePipeline을 실행하기 위한 Role 생성 예시

import json
import boto3

# Create an IAM client
iam = boto3.client('iam')


# Role 생성
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "events.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Create a new IAM role with the necessary permissions
response1 = iam.create_role(
    RoleName = eventbridge_role_name,
    AssumeRolePolicyDocument = json.dumps(trust_policy)
)

# Get the Amazon Resource Name (ARN) of the newly-created role
role_arn = response1['Role']['Arn']
print(role_arn)


# Policy 생성
eventbridge_invoke_codepipeline_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "codepipeline:StartPipelineExecution",
            "Resource": "*"
        }
    ]
}

response2 = iam.create_policy(
    PolicyName = eventbridge_policy_name,
    Path = '/',
    PolicyDocument = json.dumps(eventbridge_invoke_codepipeline_policy)
)

# Get the Amazon Resource Name (ARN) of the newly-created policy
policy_arn = response2['Policy']['Arn']
print(policy_arn)


# Role에 Policy Attach
response3 = iam.attach_role_policy(
    RoleName = eventbridge_role_name,
    PolicyArn = policy_arn
)
print(response3)

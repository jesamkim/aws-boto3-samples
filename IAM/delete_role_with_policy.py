# Rule 삭제 예시 (+ Policy 삭제)

# 앞에서 저장한 role_name, policy_arn 파라미터 로딩
# (혹은 따로 role_name과 policy_arn 확인)
%store -r policy_arn
%store -r role_name

import boto3
iam = boto3.client('iam')

# Role에서 Policy Detach
response = iam.detach_role_policy(
    RoleName = role_name,
    PolicyArn = policy_arn
)

# Role 삭제
response = iam.delete_role(
    RoleName = role_name
)

# Policy 삭제
response = iam.delete_policy(
    PolicyArn = policy_arn
)

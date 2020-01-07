import json
import logging

import boto3


def create_role(role_name, assumed_role_policy, policy, managed_policy_arns=None):
    logger = logging.getLogger(__name__)
    client = boto3.client('iam')
    managed_policy_arns = managed_policy_arns or []
    logger.info(
        "Creating role {} with accesspolicy \n {}".format(role_name, json.dumps(policy, sort_keys=False, indent=4)))

    # TODO: Fix this update role later
    try:
        client.create_role(

            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(assumed_role_policy),
            Description='This is the role for a batch task'
        )
    except Exception as e:
        logger.warning(
            "Error creating role {}, {}, the role could not be create. If the role already exists, then the managed policy and custom policy will be added to it..".format(
                role_name, e))

    # Managed policy arn here
    for p in managed_policy_arns:
        client.attach_role_policy(
            RoleName=role_name, PolicyArn=p)

    # Custom policy
    role_policy = boto3.resource('iam').RolePolicy(role_name, 'custom_policy')
    role_policy.put(
        PolicyDocument=json.dumps(policy)
    )

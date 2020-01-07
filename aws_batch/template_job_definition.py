def get_job_definition(account, region, container_name, job_def_name, job_param_s3uri_destination, memoryInMB, ncpus,
                       role_name):
    """
This is the job definition for this sample job.
    :param account:
    :param region:
    :param container_name:
    :param job_def_name:
    :param memoryInMB:
    :param ncpus:
    :param role_name:
    :return:
    """
    return {
        "jobDefinitionName": job_def_name,
        "type": "container",
        # These are the arguments for the job
        "parameters": {
            "outputdir": "/data",
            "s3destination": job_param_s3uri_destination,
            "log_level": "INFO"

        },
        # Specify container & jobs properties include entry point and job args that are referred to in parameters
        "containerProperties": {
            "image": container_name,
            "vcpus": ncpus,
            "memory": memoryInMB,
            "command": [
                "main.py",
                "Ref::outputdir",
                "--s3uri",
                "Ref::s3destination",
                "--log-level",
                "Ref::log_level"

            ],
            "jobRoleArn": "arn:aws:iam::{}:role/{}".format(account, role_name),
            "volumes": [
                {
                    "host": {
                        "sourcePath": job_def_name
                    },
                    "name": "/dev/shm"
                }
            ],
            "environment": [
                {
                    "name": "AWS_DEFAULT_REGION",
                    "value": region
                }
            ],
            "mountPoints": [
                {
                    "containerPath": "/data",
                    "readOnly": False,
                    "sourceVolume": "data"
                }
            ],
            "readonlyRootFilesystem": False,
            "privileged": True,
            "ulimits": [],
            "user": ""
        },
        "retryStrategy": {
            "attempts": 1
        }
    }

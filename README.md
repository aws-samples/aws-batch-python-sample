# AWS Batch Python sample template
A simple python quick start template to use with AWS Batch that helps you build a docker image through CI / CD . 

This demo batch downloads a sample json and uploads to s3 destination.


## Prerequistes
1. Install Python 3.6
2. Optional: Install virtual environment https://virtualenv.pypa.io/en/latest/installation/ or conda  https://conda.io/docs/installation.html

## Set up
1. Install python dependencies
```bash
pip install -r source/requirements.txt
```

## Run Sample locally

```bash
export PYTHONPATH=./source

# To get help
python ./source/main.py -h 

# Sample download data to current directory
python ./source/main.py .

# Sample download data to s3 path s3://mybucket/mydir/
python ./source/main.py . --s3 s3://mybucket/mydir/
```



## Run on AWS batch
1. Create an repository in ECR registry called "aws-batch-sample-python", as detailed here https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html

2. Setup AWS codebuild to build a docker container as detailed using cloudformation stack [codebuild_cloudformation.json](codebuild_cloudformation.json). This uses the [buildspec.yaml](buildspec.yaml). For more details on codebuild see https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html.  
   *Note* The ecr repositoryname to use is specified in the  [buildspec.yaml](buildspec.yaml)  file

3. Start a build in codebuild to push a new image into the ECS Repository "aws-batch-sample-python". When the build succeds, you will see a image in the repository

4. Register a job with AWS batch as detailed in [aws_batch/README.md](aws_batch/README.md) 



## License

This library is licensed under the MIT-0 License. See the LICENSE file.


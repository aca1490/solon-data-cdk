import os
from aws_cdk import App, Environment
from solon.main import MyStack

# for development, use account/region from cdk cli
dev_env = Environment(
  account=os.getenv('CDK_DEFAULT_ACCOUNT'),
  region=os.getenv('eu-west-1')
)

app = App()
MyStack(app, "solon-dev", env=dev_env)
# MyStack(app, "solon-prod", env=prod_env)

app.synth()
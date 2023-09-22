from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="aleksandar.stancic@helbiz.com",
    author_name="Aleksandar Stancic",
    cdk_version="2.1.0",
    module_name="solon",
    name="solon",
    version="0.1.0",
)

project.synth()
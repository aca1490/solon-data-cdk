from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="tuturutu80@gmail.com",
    author_name="Aleksandar Stancic",
    cdk_version="2.51.0",
    cdk_version_pinning=True,
    module_name="solon",
    name="solon",
    version="0.1.0",
)

project.synth()
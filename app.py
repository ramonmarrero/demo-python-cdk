#!/usr/bin/env python3

from aws_cdk import core

from demo_python_cdk.demo_python_cdk_stack import DemoPythonCdkStack


app = core.App()
DemoPythonCdkStack(app, "demo-python-cdk")

app.synth()

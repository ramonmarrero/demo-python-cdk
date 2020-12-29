#!/usr/bin/env python3

from aws_cdk import core

from LambdaStack.LambdaStack import CdkMediumStack


app = core.App()
CdkMediumStack(app, "demo-python-cdk")

app.synth()

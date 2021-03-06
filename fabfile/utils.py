#!/usr/bin/env python

import boto
import os
from boto.s3.connection import OrdinaryCallingFormat

"""
Utilities used by multiple commands.
"""

from fabric.api import prompt

def confirm(message):
    """
    Verify a users intentions.
    """
    answer = prompt(message, default="Not at all")

    if answer.lower() not in ('y', 'yes', 'buzz off', 'screw you'):
        exit()


def get_bucket(bucket_name):
    """
    Established a connection and gets s3 bucket
    """

    # if '.' in bucket_name:
    #     s3 = boto.connect_s3(calling_format=OrdinaryCallingFormat())
    # else:
    #     s3 = boto.connect_s3()

    if '.' in bucket_name:
        s3 = boto.s3.connect_to_region(os.environ['AWS_DEFAULT_REGION'],calling_format=OrdinaryCallingFormat())
    else:
        s3 = boto.connect_s3()

    return s3.get_bucket(bucket_name)

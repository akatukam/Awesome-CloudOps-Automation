##
##  Copyright (c) 2023 unSkript, Inc
##  All rights reserved.
##
from pydantic import BaseModel, Field
from typing import Optional, Tuple
from unskript.connectors.aws import aws_get_paginator
from unskript.legos.aws.aws_list_all_regions.aws_list_all_regions import aws_list_all_regions
import pprint


class InputSchema(BaseModel):
    region: Optional[str] = Field(
        default ='',
        title='Region',
        description='AWS Region.')


def aws_find_older_generation_ec2_instances_printer(output):
    if output is None:
        return
    pprint.pprint(output)


def aws_find_older_generation_ec2_instances(handle, region: str = "") -> Tuple:
    """aws_find_older_generation_ec2_instances Returns an array of instances.

        :type handle: object
        :param handle: Object returned from task.validate(...).

        :type region: string
        :param region: Region to filter instances.

        :rtype: Array of instances.
    """
    # Define the older generation instance types
    older_instance_types = ['t2', 'm1', 'm2', 'm3', 'm4', 'c1', 'c3']
    result = []
    all_regions = [region]
    if not region:
        all_regions = aws_list_all_regions(handle)

    for reg in all_regions:
        try:
            ec2Client = handle.client('ec2', region_name=reg)
            res = aws_get_paginator(ec2Client, "describe_instances", "Reservations")
            for reservation in res:
                for instance in reservation['Instances']:
                    instance_dict = {}
                    # Extract the instance ID, instance type
                    instance_id = instance['InstanceId']
                    instance_type = instance['InstanceType']
                    # Check if the instance is of older generation
                    if instance_type.split('.')[0].lower() in older_instance_types:
                        instance_dict["instance_id"] = instance_id
                        instance_dict["region"] = reg
                        result.append(instance_dict)
        except Exception as e:
            pass
    
    if len(result) != 0:
        return (False, result)
    else:
        return (True, None)
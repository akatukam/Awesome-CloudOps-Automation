##
##  Copyright (c) 2023 unSkript, Inc
##  All rights reserved.
##
from pydantic import BaseModel
from typing import List
import pprint


class InputSchema(BaseModel):
    pass

def netbox_list_devices_printer(output):
    if output is None:
        return
    pprint.pprint(output)


def netbox_list_devices(handle):
    """netbox_list_devices returns all netbox devices.
    
        :type handle: object
        :param handle: Object returned from task.validate(...).

        :rtype: List of Netbox devices.
    """
    result = handle.dcim.devices.all()
    return result

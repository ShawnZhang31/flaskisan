'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-10 16:11:16 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-10 16:17:06
 */
'''
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import sys

from flaskisan import exceptions
from flaskisan.cli import dispatch

import requests

def main():
    try:
        return dispatch(sys.argv[1:])
    except exceptions.flaskisanException as exc:
        return "{}: {}".format(exc.__class__.__name__, exc.args[0])

if __name__ == "__main__":
    sys.exit(main())
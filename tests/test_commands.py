'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-09 01:12:25 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-09 01:24:50
 */
'''
import pytest
from flaskisan.commands.new import new

def test_new_project_function():
    result = new('flask')
    expected = 0
    assert expected == respone
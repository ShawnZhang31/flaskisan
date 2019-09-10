'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-09 00:53:46 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-09 11:07:41
 */
'''
from __future__ import absolute_import, print_function
import os
import subprocess
import click
import git
from git.exc import GitCommandError
import shutil

from flaskisan import exceptions

flaskisan_repos = 'git@github.com:ShawnZhang31/flask-artisan.git'

@click.command()
@click.option('--name', default=None, help='工程名称')
@click.option('--v', default=None, help='flaskisan的版本')
def new(name, version):
    """创建flask工程
    参数：
        name:要创建的flaskisan工程的名称
        version:使用的flaskisan的版本号
    """
    if name is None:
        click.echo('必须为工程指定一个名称')
        return
    if version is None:
        click.echo('未指定flaskisan版本，以flaskisan最新版本为基础创建工程')
    
    repos = git.Repo.clone_from(url=flaskisan_repos, to_path=name)
    tags = sorted(repos.tags, key=lambda t: t.commit.committed_datetime)
    tag = None
    if version:
        for item in tags:
            if version == item.name:
                tag = item
            break
    if tag is None:
        tag = tags[-1]
        click.echo('使用 {0} 版本的flaskisan初始化工程'.format(tag.name))
    
    try:
        repos.git.checkout(tag)
    except GitCommandError as e:
        click.echo(str(e))
    shutil.rmtree(name+'/.git')

    click.echo(name+'工程初始化完毕，执行pipenv install 安装依赖库')
    
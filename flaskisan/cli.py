'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-22 16:20:46 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-22 16:59:20
 */
'''
import os
import sys
import click

CONTEXT_SETTINGS = dict(auto_envvar_prefix='flaskisan')

class Environment(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
    
    def log(self, msg, *args):
        """logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)
    
    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)
    
pass_environment = click.make_pass_decorator(Environment, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),'commands'))

class FlaskisanCli(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
                filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv
    
    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('flaskisan.commands.cmd_' + name,
                             None, None, ['cli'])
        except ImportError:
            return
        return mod.cli
    
@click.command(cls=FlaskisanCli, context_settings=CONTEXT_SETTINGS)
@click.option('--home', type=click.Path(exists=True, file_okay=False, resolve_path=True),
                help='改变执行命令的文件夹')
@click.option('-v', '--verbose', is_flag=True, help='启用verbose模式')
@pass_environment
def cli(ctx, verbose, home):
    """flaskisan命令行界面"""
    ctx.verbose = verbose
    if home is not None:
        ctx.home = home
    
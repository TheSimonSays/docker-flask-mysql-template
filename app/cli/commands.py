from app.cli import bp
import click


@bp.command('test')
@click.argument('name')
def test(name):
    print('Argument: {0}'.format(name))

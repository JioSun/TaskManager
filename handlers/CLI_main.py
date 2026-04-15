import click
from database.db_main import table_add, table_list, task_delete, task_done

@click.group()
def cli():
    pass

@cli.group()
def task():
    pass

@task.command()
@click.argument('text', type=str)
def add(text):
    table_add(text)
    task_id = table_list()[-1][0]
    click.echo(f'Task added with id = {task_id}')

@task.command()
def list():
    click.echo('List of tasks:')
    c = 0
    for t in table_list():
        task_id, text, _, status = t
        c += 1
        click.echo(f"{c}) Task: {text} | Status: {status} | id: {task_id}")

@task.command()
@click.argument('id', type=int)
def delete(id):
    task_delete(id)
    task_text = table_list()[id - 1][1]
    click.echo(f'Task: "{task_text}" deleted')

@task.command()
@click.argument('id', type=int)
def done(id):
    task_done(id)
    task_text = table_list()[id - 1][1]
    click.echo(f'Task: "{task_text}" done')




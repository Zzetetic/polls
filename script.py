#!/usr/bin/env python3
import os
import subprocess
import click


image_name = "polls:latest"
container_name = "polls"

@click.group()
def image():
    pass

@click.group()
def container():
    pass

@image.command()
def create_image():
    subprocess.run(['docker', 'build', '-t', f'{image_name}', '.'])   

@image.command()
def delete_image():
    subprocess.run(['docker', 'rmi', f'{image_name}'])   


@container.command(help="создать контейнер докер с именем focused_shirley на основе образа ссозданного с помощью команды create_image")
def create_container():
    subprocess.run(['docker', 'run', '-it', f'--mount=type=bind,source={os.getcwd()},target=/src', '--name', f'{container_name}', '-p', '8000:8000', f'{image_name}'])
 
@container.command()
def delete_container():
    subprocess.run(['docker', 'rm,', f'{container_name}'])
    

@container.command()
def start_container():
    subprocess.run(['docker', 'start', '-i', f'{container_name}'])

cli = click.CommandCollection(sources=[image, container])
 
if __name__ == '__main__':
    cli()

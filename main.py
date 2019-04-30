#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd7in5b
import time
from PIL import Image
import traceback
from display import display
import click
from pathlib import Path


@click.group()
def main():
    pass

@main.command()
@click.option("--name", prompt="Filename without .png")
def render(name):
    """Render selected image."""
    epd = epd7in5b.EPD()
    epd.init()
    display(name, epd)


@main.command()
def list():
    """Lists out images in `images/` directory."""
    for png in Path('images').glob('*.png'):
        print(str(png).replace('images', "").replace('/', '').strip('.png'))


if __name__ == "__main__":
    main()

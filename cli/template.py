#!/usr/bin/env python
"""
Template engine.
"""

import os
from jinja2 import Environment, PackageLoader, select_autoescape
from cli.settings import TEST_CONFIG

env = Environment(loader=PackageLoader('cli', 'templates'),
                  autoescape=select_autoescape(['html', 'xml', 'sql']))


def print_test():
    """
    Print test.
    """
    print("config -- ", TEST_CONFIG)


def to_sql():
    """
    Generate sql.
    """
    template = env.get_template('prd/account.sql')
    os.environ['APP_ENVIRONMENT'] = 'qas'
    print(template.render(env=os.environ))
    template.stream(env=os.environ).dump('tmp/account.sql')

#!/usr/bin/env python

from setuptools import setup

setup(name='tap-sendgrid',
      version='0.1.0',
      description='Singer.io tap for extracting data from the SendGrid API',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_sendgrid'],
      python_requires='>=3.9',
      install_requires=['singer-python>=6,<7',
                        'requests>=2.31,<3',
                        'pendulum>=3,<4',
                        ],
      entry_points='''
          [console_scripts]
          tap-sendgrid=tap_sendgrid:main
      ''',
      packages=['tap_sendgrid'],
      package_data={
          'tap_sendgrid/schemas': [
                "contacts.json",
                "global_suppressions.json",
                "groups_members.json",
                "groups_all.json",
                "invalids.json",
                "lists_all.json",
                "lists_members.json",
                "segments_all.json",
                "segments_members.json",
                "templates_all.json",
                "blocks.json",
                "bounces.json",
                "campaigns.json",
                "spam_reports.json",
                "global_suppressions_overwrite.json",
              ]
         },
      include_package_data=True
)

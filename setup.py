from setuptools import setup, find_packages
import os

version = '1.0.1'

setup(name='collective.braveportletsmanager',
      version=version,
      description="Custom Plone Portlets Manager that doesn't break even with broken or not available portlet assignments",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone portlet brave',
      author='SoftFormance',
      author_email='contact@softformance.com',
      url='https://github.com/softformance/collective.braveportletsmanager',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

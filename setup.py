import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ConsumerDebt',
      version='1.0.5',
      description=(''),
      long_description='# docassemble.MAVirtualCourt\r\n\r\n\r\n\r\n## Author\r\n\r\nQuinten Steenhuis\r\nCaroline Robinson\r\nKate Barry\r\nPlocket\r\nLily Yang\r\nMatthew Brooks\r\nLance Godard\r\nMaeve MacGlinchey\r\nMichael Cronin\r\nKendall Garner\r\nDavid Colarusso',
      long_description_content_type='text/markdown',
      author='Quinten Steenhuis',
      author_email='qsteenhuis@suffolk.edu',
      license='MIT',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.ALMassachusetts>=0.0.7', 'docassemble.ALToolbox>=0.0.11', 'docassemble.AssemblyLine>=2.1.4', 'docassemble.MACourts>=0.0.58.2', 'docassemble.MassAccess>=0.0.3.1'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ConsumerDebt/', package='docassemble.ConsumerDebt'),
     )


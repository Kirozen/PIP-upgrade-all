""" pip-upgrade-all.py """

__author__ = "Etienne Faisant"
__date__ = "2015-11-04"

__version__ = "1.0"

import pip


def upgrade_all():
    pip.main(['install', '--upgrade', 'pip'])
    for dist in pip.get_installed_distributions():
        pip.main(['install', '--upgrade', dist.project_name])


if __name__ == '__main__':
    upgrade_all()

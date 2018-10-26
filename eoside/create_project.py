import argparse

import eosfactory.core.logger as logger
import eosfactory.core.teos as teos

def project_from_template(
        name, template="", user_workspace=None, remove_existing=False, 
        visual_studio_code=False, verbosity=None):
    '''Given the template type and a name, create a contract workspace. 

    - **parameters**::

        name: The name of the new wallet, defaults to ``default``.
        template: The name of the template used.
        user_workspace: If set, the folder for the work-space. Defaults to the 
            value of the ``EOSIO_CONTRACT_WORKSPACE`` env. variable.
        remove_existing: If set, overwrite any existing workspace.
        visual_studio_code: If set, open the ``VSCode``, if available.
        verbosity: The logging configuration.
    '''

    logger.INFO('''
    ######### Create contract ``{}`` from template ``{}``.
    '''.format(name, template))

    contract_path_absolute = teos.template_create(
        name, template, user_workspace, remove_existing, visual_studio_code,
        throw_exists=False)

    return contract_path_absolute

parser = argparse.ArgumentParser(description='''
Given a workspace name and a template name (optional),
create a new workspace, compatible with Visual Studio Code.

Example:
    python3 create_project.py contract.name 01_hello_world
''')

parser.add_argument("name")
parser.add_argument("template", nargs="?", default="01_hello_world")

args = parser.parse_args()




project_from_template(args.name, template=args.template)
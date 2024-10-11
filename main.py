import sys

from dotenv import dotenv_values
from loguru import logger

import utils
from mig import create_file_name, new_file
from net import SSH
from settings.projects import db, project_exists

"""
main.py

This script serves as the entry point for the ISSMIG application, which is responsible for managing database migrations.
It ensures that the database schema is up-to-date and consistent across different environments by applying necessary
migrations and handling version control for the database schema.
"""

if __name__ == "__main__":
    # 0.A Load environment variables from the .env file
    config = dotenv_values(".env")
    ue = utils.Env(config)
    hostname: str = ue.get_param("HOSTNAME")
    username: str = ue.get_param("USERNAME")
    password: str = ue.get_param("PASSWORD")

    # 0.B Check for the required arguments
    tot_args: int = sys.argv.__len__()
    if tot_args < 4:
        logger.warning("Required arguments are: new_file|send|fetch|show_local|show_remote|list_local|list_remote <project> <issue>")
        sys.exit(1)

    action: str = sys.argv[1]
    if action not in ["new_file", "send", "fetch"]:
        logger.error("Invalid action - expected new_file|send|fetch|show_local|show_remote|list_local|list_remote")
        sys.exit(1)

    project: str = sys.argv[2]
    if not project_exists(project, db):
        logger.error("project doesnt exist")
        sys.exit(1)

    issue: str = sys.argv[3]
    if not issue.isnumeric():
        logger.error("issue must be a number")
        sys.exit(1)

    # 1. INPUT: new_file - create local resource
    if action == "new_file":
        file_name: str = create_file_name(db[project], issue)
        new_file(file_name)
        sys.exit(0)

    # 2. prepare connection
    ssh: SSH = SSH(hostname=hostname, username=username, password=password)

    # 3. INPUT: send - put file to remote server
    if action == "send":
        if tot_args != 5:
            logger.warning("Required arguments are: send <project> <issue> <file_name>")
            sys.exit(1)

        file_name = sys.argv[4]
        sent: bool = ssh.send_file(file_name)
        if sent:
            logger.success("File sent")
        else:
            logger.error("File not sent")

    # 4. INPUT: fetch - get the file
    if action == "fetch":
        if tot_args != 5:
            logger.warning("Required arguments are: fetch <project> <issue> <file_name>")
            sys.exit(1)

        file_name = sys.argv[4]
        fetched: bool = ssh.fetch_file(file_name)
        if fetched:
            logger.success("File received")
            sys.exit(0)

        else:
            logger.error("File not received")
            sys.exit(1)

import datetime
import os

from loguru import logger

from settings.default import LOCAL_DIR_OUT


def create_file_name(project_id: str, issue: str) -> str:
    """
    Generates a filename for a SQL file based on the project ID, issue, and the current timestamp.

    project_id(str): The identifier for the project.
    issue(str): The issue or description related to the project.

    str: A string representing the filename in the format 'project_id_issue_timestamp.sql'.

    Args:
        project_id (str): The identifier for the project.
        issue (str): The issue or description related to the project.

    Returns:
        str: The generated filename.
    """
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    res: str = f"{project_id}_{issue}_{now}.sql"

    return res


def new_file(f_name: str) -> int:
    """
    Creates a new file with the given name.
    Args:
        f_name (str): The name of the file to create.
    Exceptions:
        Exception: If there is an error during the file creation process.
    """
    res = 0
    full_path = f"{LOCAL_DIR_OUT}/{f_name}"

    try:
        with open(full_path, "w") as f:
            logger.debug(f"Created file {full_path}")
            res = f.write("")

    except Exception as err:
        logger.error(err)

    finally:
        return res


def list_files() -> list[str]:
    """
    Lists all files in the output directory.
    Returns:
        list[str]: A list of filenames in the output directory.
    """

    # List all files in the output directory, forcing the list to be a list of strings
    # in order to avoid issues with the type checker
    files_list: list[str] = list(os.listdir(LOCAL_DIR_OUT))

    return files_list

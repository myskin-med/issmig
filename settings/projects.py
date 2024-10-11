db: dict[str, str] = {
    "duale-platform-v1": "1",
}


def project_exists(in_key: str, target: dict[str, str]) -> bool:
    """
    Check if a project key exists in the target dictionary.

    Args:
        in_key (str): The key to check for existence in the target dictionary.
        target (dict[str, str]): The dictionary in which to check for the key.

    Returns:
        bool: True if the key exists in the dictionary, False otherwise.
    """

    return in_key in target.keys()

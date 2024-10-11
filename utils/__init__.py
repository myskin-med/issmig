from typing import Optional

from loguru import logger

from settings import default


class Env:
    """
    A class used to represent an environment configuration.

    Attributes:
        config (dict[str, Optional[str]]): A dictionary containing configuration parameters.

    Methods:
        get_param(p_name: str) -> str:
            Parses a parameter from the configuration dictionary.
    """

    def __init__(self, config: dict[str, Optional[str]]) -> None:
        """
        Initialize the instance with the given configuration.
        Args:
            config(dict[str, Optional[str]]): A dictionary containing configuration settings
        """

        self.config: dict[str, Optional[str]] = config

    def get_param(self, p_name: str) -> str:
        """
        Parses a parameter from a configuration dictionary.
        Args:
            config (dict[str, Optional[str]]): The configuration dictionary containing parameter values.
            p_name (str): The name of the parameter to parse.

        Returns:
            str: The value of the parameter if it exists and is not None, otherwise "unset".

        Raises:
            Exception: If the parameter is unset.
            Exception: If an error occurs during the parsing process.
        """

        try:
            res: str = default.UNSET_VAL

            cur_val: Optional[str] = self.config[p_name]

            if cur_val is not None:
                res = cur_val

            if res == default.UNSET_VAL:
                raise Exception(f"Parameter {p_name} is unset")

        except Exception as err:
            logger.error(err)

        finally:
            return res

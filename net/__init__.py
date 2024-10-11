import paramiko
import paramiko.client
import scp
from loguru import logger

from settings import default


class SSH:
    _client: paramiko.SSHClient

    def __init__(self, hostname: str, username: str, password: str) -> None:
        """
        Initializes the SSH client and connects to the specified hostname using the provided credentials.
        Args:
            hostname (str): The hostname or IP address of the SSH server.
            username (str): The username to authenticate with.
            password (str): The password to authenticate with.
        Raises:
            Exception: If there is an error during the connection attempt.
        Attributes:
            _client (paramiko.SSHClient): The SSH client instance.
        """

        client: paramiko.SSHClient = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(hostname=hostname, username=username, password=password)
        except Exception as err:
            logger.error(err)

        finally:
            self._client: paramiko.SSHClient = client

    def send_file(self, file_name: str) -> bool:
        """
        Sends a file to a remote directory using SCP.
        Args:
            file_name (str): The name of the file to be sent.
        Returns:
            bool: True if the file was successfully sent, False otherwise.
        Raises:
            Exception: If there is an error during the file transfer.
        """

        t = self._client.get_transport()
        res = False

        try:
            if t is not None:
                c_scp: scp.SCPClient = scp.SCPClient(transport=t)
                c_scp.put(f"{default.LOCAL_DIR_OUT}/{file_name}", f"{default.REMOTE_DIR_IN}/{file_name}")
                c_scp.close()

                res = True

        except Exception as err:
            logger.error(err)

        finally:
            return res

    def fetch_file(self, file_name: str) -> bool:
        """
        Fetches a file from a remote directory using SCP.
        Args:
            file_name (str): The name of the file to be retrieved.
        Returns:
            bool: True if the file was successfully retrieved, False otherwise.
        Raises:
            Exception: If there is an error during the file retrieval.
        """

        t = self._client.get_transport()
        res = False

        try:
            if t is not None:
                c_scp: scp.SCPClient = scp.SCPClient(transport=t)
                c_scp.get(f"{default.REMOTE_DIR_OUT}/{file_name}", f"{default.LOCAL_DIR_IN}/{file_name}")
                c_scp.close()

                res = True

        except Exception as err:
            logger.error(err)

        finally:
            return res

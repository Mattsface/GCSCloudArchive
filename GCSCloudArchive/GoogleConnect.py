
import boto
import gcs_oauth2_boto_plugin


class GoogleConnect(object):
    """
    Google Class to connect to API
    """

    # URI scheme for Google Cloud Storage.
    GOOGLE_STORAGE = 'gs'
    # URI scheme for accessing local files.
    LOCAL_FILE = 'file'




    def __init__(self):
        pass
from filestack import Client


class FileSharer:
    """
    Enables uploading PDFs to filestack cloud
    """
    def __init__(self, filepath, api_key="AeDf0UXiGRxqJrWMXoSmgz"):
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        """
        Upload a file to the filestack cloud and generate a url to access it
        :return: the file url
        """
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

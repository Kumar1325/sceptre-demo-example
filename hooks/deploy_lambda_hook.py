import base64
import boto3
import logging
import os
import botocore
from sceptre.hooks import Hook
from sceptre.connection_manager import ConnectionManager


class DeployLambdaHook(Hook):
    def __init__(self, *args, **kwargs):
        super(DeployLambdaHook, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)
        #self.connection_manager = ConnectionManager(self.argument.split()[3])

    def run(self):

        """
        run is the method called by Sceptre. It should carry out the work
        intended by this hook.

        self.argument is available from the base class and contains the
        argument defined in the sceptre config file (see below)

        The following attributes may be available from the base class:
        self.stack_config  (A dict of data from <stack_name>.yaml)
        self.environment_config  (A dict of data from config.yaml)
        self.connection_manager (A connection_manager)

        """
        self.logger.debug("Get account id.")
        s3 = boto3.client("s3")
        unresolved_bucket_name = self.argument.split()[0]
        key = self.argument.split()[1]
        if len(self.argument.split()) == 3:
            file_name = self.argument.split()[2]
        else:
            file_name = self.argument.split()[1]

        zip_file_location = os.path.join("dist", file_name)
        try:
            #sts = self.connection_manager.client("sts")
            #account_id = sts.get_caller_identity()["Account"]
            lambda_bucket_name = unresolved_bucket_name
            try:
                #s3 = self.connection_manager._get_client("s3")
                self.logger.debug("Try to put lambda zip file into bucket")
                print("Try to put lambda zip file into bucket")
                s3.put_object(
                    Bucket=lambda_bucket_name,
                    Key=key,
                    Body=open(zip_file_location, "rb"),
                    ServerSideEncryption="AES256",
                )
                print("Upload successful")
            except botocore.exceptions.ClientError as error:
                self.logger.debug("Unable to put lambda zip file into bucket")
                self.logger.debug(error)
                print(f"Upload failed: {error}")
        except botocore.exceptions.ClientError as error:
            self.logger.debug("Unable to obtain account id")
            self.logger.debug(error)
            print(f"Error: Upload failed: {error}")

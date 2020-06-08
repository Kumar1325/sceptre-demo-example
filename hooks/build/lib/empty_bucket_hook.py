import base64
import logging
import botocore
from sceptre.hooks import Hook


class EmptyBucketHook(Hook):
    def __init__(self, *args, **kwargs):
        super(EmptyBucketHook, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

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

        try:
            sts = self.connection_manager._boto_session.client("sts")
            account_id = sts.get_caller_identity()["Account"]
            config_bucket_name = "{}{}".format(account_id, self.argument)
            try:
                s3 = self.connection_manager._boto_session.resource("s3")
                self.logger.debug("Emptying bucket")
                bucket = s3.Bucket(config_bucket_name)
                bucket.objects.all().delete()
                self.logger.debug("Deleting bucket")
                bucket.delete()
            except botocore.exceptions.ClientError as error:
                self.logger.debug("Unable to empty or delete bucket")
                self.logger.debug(error)
        except botocore.exceptions.ClientError as error:
            self.logger.debug("Unable to obtain account id")
            self.logger.debug(error)

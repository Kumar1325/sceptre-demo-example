from setuptools import setup

setup(
    name='deploy_lambda_hook',
    py_modules=['deploy_lambda_hook', 'empty_bucket_hook'],
    entry_points={
        'sceptre.hooks': [
            'deploy_lambda_hook = deploy_lambda_hook:DeployLambdaHook',
            'empty_bucket_hook = empty_bucket_hook:EmptyBucketHook'
        ],
    }
)

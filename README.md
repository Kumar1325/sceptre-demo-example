# sceptre-demo-example
Using Sceptre to launch CFN templates

# Requirements
- Python Troposphre: troposphere==2.6.0
- Sceptre: sceptre==2.3.0
- Boto3: boto3==1.12.43

# Environment
Here you have two environments under /confg `Dev` and `Prod`
- Prod : evnironment is developed using the python files (With the help of Troposphere)
- Dev: environment is developed with normal CFT template (yaml files)

# Validating and Deploying
You should be on the root directory of the Repo
## Validating
`sceptre validate <env>`
## Deploying
`sceptre launch <evn>`

## Deleting/Destroying
`sceptre delete <env>`

## References
- https://github.com/cloudreach/sceptre-wordpress-example
- https://github.com/densikat-shinesolutions/sceptre-example
- https://sceptre.cloudreach.com/latest/docs/get_started.html
- https://sceptre.cloudreach.com/latest/docs/hooks.html
- https://sceptre.cloudreach.com/latest/docs/resolvers.html
- https://www.youtube.com/watch?v=g0AQWT9J88A

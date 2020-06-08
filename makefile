.PHONY: deploy_dev deploy_prod destroy_dev destroy_prod validate_dev validate_prod test

dist:
	@cd src && zip -r9 kumar-lambda.zip .
	@mkdir dist && mv src/kumar-lambda.zip dist

deploy_lambda: dist
	@echo "Deploying Lambda"
	@sceptre launch dev/lambda.yaml --yes

test:
	@echo "Not test case written as of now, you can add them"

validate_dev:
	@echo "Validating DEV environment"
	@sceptre validate dev
  
validate_prod:
	@ehco "Validating PROD environment"
	@sceptre validate prod
  
deploy_dev: validate_dev
	@echo "Deploying DEV environment"
	@sceptre launch dev --yes
  
deploy_prod: validate_prod
	@echo "Deploying PROD environment"
	@sceptre launch prod --yes
  
destroy_dev:
	@echo "Destroying DEV environment"
	@sceptre delete dev --yes
  
destroy_prod:
	@echo "Destroying PROD environment"
	@sceptre delete prod --yes

.PHONY: linting
linting: lint_pylint lint_flake8
	@echo "Applied Linting with flake8 and pylint"

.PHONY: lint_flake8
lint_flake8:
	@echo "Linting with Flake8"
	@flake8 templates/ > flake8.log || :

.PHONY: lint_pylint
lint_pylint:
	@echo "Linting with Pylint"
	@pylint templates/ > pylint.log || :

.PHONY: deploy_dev deploy_prod destroy_dev destroy_prod validate_dev validate_prod

validate_dev:
  @echo "Validating DEV environment"
  sceptre validate dev
  
validate_prod:
  @ehco "Validating PROD environment"
  sceptre validate prod
  
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

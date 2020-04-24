.PHONY: deploy_dev deploy_prod destroy_dev destroy_prod

deploy_dev:
  @echo "Deploying DEV environment"
  @sceptre launch dev --yes
  
deploy_prod:
  @echo "Deploying PROD environment"
  @sceptre launch prod --yes
  
destroy_dev:
  @echo "Destroying DEV environment"
  @sceptre delete dev --yes
  
destroy_prod:
  @echo "Destroying PROD environment"
  @sceptre delete prod --yes

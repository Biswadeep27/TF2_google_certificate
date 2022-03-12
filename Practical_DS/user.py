from FactoryDesign import DeployFactory

choice = input('what do you want:\n')

deploy = DeployFactory.get_deploy(choice)
deploy.deploy_mode()
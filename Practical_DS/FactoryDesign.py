from abc import ABCMeta, abstractstaticmethod

class ISparkSubmit(metaclass=ABCMeta):
	@abstractstaticmethod
	def deploy_mode():
		'''Interface Method'''


class Yarn(ISparkSubmit):

	def __init__(self):
		self.name = 'Master : YARN'

	def deploy_mode(self):
		print('The spark deploy mode is YARN')

class Standalone(ISparkSubmit):

	def __init__(self):
		self.name = 'Master : Standalone'

	def deploy_mode(self):
		print('The spark deploy mode is Standalone')

class Kubernetes(ISparkSubmit):

	def __init__(self):
		self.name = 'Master : K8S'

	def deploy_mode(self):
		print('The spark deploy mode is K8S')

class DeployFactory:

	@staticmethod
	def get_deploy(deploy_type):
		if deploy_type == 'yarn':
			return Yarn()
		if deploy_type == 'standalone':
			return Standalone()
		if deploy_type == 'k8s':
			return Kubernetes()
		print('invalid deploy mode')
		return -1

# choice = input('what do you want:')

# deploy = DeployFactory.get_deploy(choice)
# deploy.deploy_mode()
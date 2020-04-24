from troposphere import Template, Ref, FindInMap, Output, Join
from troposphere import Parameter, Tags
import troposphere.ec2 as ec2
from base import CloudformationAbstractBaseClass


class Ec2InstanceClass(CloudformationAbstractBaseClass):
	    
		def __init__(self, sceptre_user_data):
				super(self.__class__, self).__init__()
				self.template.set_description("""Wordpress EC@""")

				self.add_parameters()
				self.add_resources()

		def add_parameters(self):
				t = self.template

				self.AmiId = t.add_parameter(
					Parameter("AmiId", Description="Instnace ImageId", Type="String")
				)
				self.SubnetId = t.add_parameter(
					Parameter("SubnetId", Description="VPC SubnetId", Type="String")
				)
				self.SecurityGroup = t.add_parameter(
					Parameter(
						"SecurityGroup", Description="Instance Security Group", Type="String"
					)
				)

		def add_resources(self):
				self.Ec2Instance = self.template.add_resource(
					ec2.Instance(
						"Ec2Instance",
						SubnetId=Ref(self.SubnetId),
						InstanceType="t2.micro",
						ImageId=Ref(self.AmiId),
						SecurityGroupIds=[Ref(self.SecurityGroup)],
						Tags=Tags(
							Name=Join("", ["Ec2", Ref(self.Project)]),
							Environment=Ref(self.Environment),
							Project=Ref(self.Project),
							Owner=Ref(self.Owner),
							ExpirationDate=Ref(self.ExpirationDate)
						)
					)
				)


def sceptre_handler(sceptre_user_data):
    return Ec2InstanceClass(sceptre_user_data).template.to_yaml()


if __name__ == "__main__":
    print(sceptre_handler())

from troposphere import Template, Parameter, Ref, Output, GetAtt
from troposphere.awslambda import Function, Code

def sceptre_handler(sceptre_user_data):
  return SceptreResource(sceptre_user_data).template.to_json()

class SceptreResource(object):
  def __init__(self, sceptre_user_data):
    self.template = Template()

    name = self.template.add_parameter(Parameter("Name", Type="String"))
    role = self.template.add_parameter(Parameter("Role", Type="String"))

    sceptre_user_data["FunctionName"] = Ref(name)
    sceptre_user_data["Role"] = Ref(role)
    sceptre_user_data["Code"] = Code(**sceptre_user_data["Code"])
    function = self.template.add_resource(
      Function("Function", **sceptre_user_data)
    )

    self.template.add_output(Output("Arn", Value=GetAtt(function, "Arn")))

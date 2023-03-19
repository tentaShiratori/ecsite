import * as cdk from "aws-cdk-lib";
import { Template } from "aws-cdk-lib/assertions";
import * as Resource from "../../lib/resource-stack";
it("VPC", () => {
  const app = new cdk.App();
  const stack = new Resource.ResourceStack(app, "MyTestStack");
  const template = Template.fromStack(stack);
  template.resourceCountIs("AWS::EC2::VPC", 1);
  template.hasResourceProperties("AWS::EC2::VPC", {
    CidrBlock: "10.0.0.0/16",
    Tags: [{ Key: "Name", Value: "undefined-undefined-vpc" }],
  });
});

import { CfnVPC } from "aws-cdk-lib/aws-ec2";
import type { Construct } from "constructs";
import { Resource } from "./abstract/resource";
export class Vpc extends Resource {
  public vpc: CfnVPC;

  public createResources(scope: Construct): void {
    this.vpc = new CfnVPC(scope, "Vpc", {
      cidrBlock: "10.0.0.0/16",
      tags: [{ key: "Name", value: this.createResourceName(scope, "vpc") }],
    });
  }
}

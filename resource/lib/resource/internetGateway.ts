import {
  CfnInternetGateway,
  CfnVPCGatewayAttachment,
} from "aws-cdk-lib/aws-ec2";
import type { CfnVPC } from "aws-cdk-lib/aws-ec2";
import { Resource } from "./abstract/resource";
import type { Construct } from "constructs";

export class InternetGateway extends Resource {
  public igw: CfnInternetGateway;

  private readonly vpc: CfnVPC;

  constructor(vpc: CfnVPC) {
    super();
    this.vpc = vpc;
  }

  createResources(scope: Construct): void {
    this.igw = new CfnInternetGateway(scope, "InternetGateway", {
      tags: [{ key: "Name", value: this.createResourceName(scope, "igw") }],
    });

    new CfnVPCGatewayAttachment(scope, "VpcGatewayAttachment", {
      vpcId: this.vpc.ref,
      internetGatewayId: this.igw.ref,
    });
  }
}

import * as cdk from "aws-cdk-lib";
import type { Construct } from "constructs";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as ecs from "aws-cdk-lib/aws-ecs";
import * as ecr from "aws-cdk-lib/aws-ecr";
import * as elbv2 from "aws-cdk-lib/aws-elasticloadbalancingv2";
import * as imagedeploy from "cdk-docker-image-deployment";
import path from "path";
export class ResourceStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    const tag: string = scope.node.tryGetContext("tag");
    // VPCを作成
    const vpc = new ec2.Vpc(this, "Vpc", {
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: "public",
          subnetType: ec2.SubnetType.PUBLIC,
        },
      ],
    });

    const securityGroupELB = new ec2.SecurityGroup(this, "SecurityGroupELB", {
      vpc,
    });
    securityGroupELB.addIngressRule(
      ec2.Peer.ipv4("0.0.0.0/0"),
      ec2.Port.tcp(80)
    );

    const securityGroupAPP = new ec2.SecurityGroup(this, "SecurityGroupAPP", {
      vpc,
    });

    // ALB
    const alb = new elbv2.ApplicationLoadBalancer(this, "ALB", {
      vpc,
      securityGroup: securityGroupELB,
      internetFacing: true,
    });

    const listenerHTTP = alb.addListener("ListenerHTTP", {
      port: 80,
    });
    const targetGroup = new elbv2.ApplicationTargetGroup(this, "TG", {
      vpc: vpc,
      port: 3000,
      protocol: elbv2.ApplicationProtocol.HTTP,
      targetType: elbv2.TargetType.IP,
      healthCheck: {
        path: "/",
        healthyHttpCodes: "200",
      },
    });
    listenerHTTP.addTargetGroups("DefaultHTTPSResponse", {
      targetGroups: [targetGroup],
    });

    // ECS Cluster
    const cluster = new ecs.Cluster(this, "Cluster", {
      vpc,
    });

    // Fargate
    const fargateTaskDefinition = new ecs.FargateTaskDefinition(
      this,
      "TaskDef",
      {
        memoryLimitMiB: 1024,
        cpu: 512,
      }
    );
    fargateTaskDefinition.addContainer("NextAppContainer", {
      image: ecs.ContainerImage.fromAsset(path.join(__dirname, "../../admin")),
      logging: new ecs.AwsLogDriver({
        streamPrefix: "MyApp",
      }),
      portMappings: [{ containerPort: 3000 }],
    });
    const service = new ecs.FargateService(this, "Service", {
      cluster,
      taskDefinition: fargateTaskDefinition,
      desiredCount: 1,
      assignPublicIp: true,
      securityGroups: [securityGroupAPP],
    });
    service.attachToApplicationTargetGroup(targetGroup);
  }
}

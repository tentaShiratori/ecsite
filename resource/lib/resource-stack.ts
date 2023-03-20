import * as cdk from "aws-cdk-lib";
import type { Construct } from "constructs";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as ecs from "aws-cdk-lib/aws-ecs";
import * as elbv2 from "aws-cdk-lib/aws-elasticloadbalancingv2";
import path from "path";
export class ResourceStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
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
    const albs = this.createAlB(vpc);
    this.createBackendStack(vpc, albs);
    this.createAdminStack(vpc, albs);
  }

  private createAdminStack(
    vpc: ec2.IVpc,
    albs: {
      feAlb: elbv2.IApplicationLoadBalancer;
      beAlb: elbv2.IApplicationLoadBalancer;
    }
  ): void {
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

    const listenerHTTP = albs.feAlb.addListener("ListenerHTTP", {
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
      image: ecs.ContainerImage.fromAsset(path.join(__dirname, "../../admin"), {
        buildArgs: {
          // buildするときは
          NEXT_PUBLIC_BACKEND_URL: process.env.BACKEND_URL as string,
        },
      }),
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

  private createAlB(vpc: ec2.IVpc): {
    feAlb: elbv2.IApplicationLoadBalancer;
    beAlb: elbv2.IApplicationLoadBalancer;
  } {
    const securityGroupELB = new ec2.SecurityGroup(this, "BESecurityGroupELB", {
      vpc,
    });
    securityGroupELB.addIngressRule(
      ec2.Peer.ipv4("0.0.0.0/0"),
      ec2.Port.tcp(80)
    );

    const feAlb = new elbv2.ApplicationLoadBalancer(this, "ALB", {
      vpc,
      securityGroup: securityGroupELB,
      internetFacing: true,
    });

    const beAlb = new elbv2.ApplicationLoadBalancer(this, "BEALB", {
      vpc,
      securityGroup: securityGroupELB,
      internetFacing: true,
    });
    return { feAlb, beAlb };
  }

  private createBackendStack(
    vpc: ec2.IVpc,
    albs: {
      feAlb: elbv2.IApplicationLoadBalancer;
      beAlb: elbv2.IApplicationLoadBalancer;
    }
  ): void {
    const securityGroupAPP = new ec2.SecurityGroup(this, "BESecurityGroupAPP", {
      vpc,
    });

    const listenerHTTP = albs.beAlb.addListener("BEListenerHTTP", {
      port: 80,
    });
    const targetGroup = new elbv2.ApplicationTargetGroup(this, "BETG", {
      vpc: vpc,
      port: 8000,
      protocol: elbv2.ApplicationProtocol.HTTP,
      targetType: elbv2.TargetType.IP,
      healthCheck: {
        path: "/",
        healthyHttpCodes: "200",
      },
    });
    listenerHTTP.addTargetGroups("BEDefaultHTTPSResponse", {
      targetGroups: [targetGroup],
    });

    // ECS Cluster
    const cluster = new ecs.Cluster(this, "BECluster", {
      vpc,
    });

    // Fargate
    const fargateTaskDefinition = new ecs.FargateTaskDefinition(
      this,
      "BETaskDef",
      {
        memoryLimitMiB: 1024,
        cpu: 512,
      }
    );
    fargateTaskDefinition.addContainer("DjangoAppContainer", {
      image: ecs.ContainerImage.fromAsset(path.join(__dirname, "../../back")),
      logging: new ecs.AwsLogDriver({
        streamPrefix: "BEApp",
      }),
      portMappings: [{ containerPort: 8000 }],
      environment: {
        APP_ENV: "production",
        ALLOWED_HOSTS: `${albs.beAlb.loadBalancerDnsName} ${albs.feAlb.loadBalancerDnsName}`,
      },
    });
    const service = new ecs.FargateService(this, "BEService", {
      cluster,
      taskDefinition: fargateTaskDefinition,
      desiredCount: 1,
      assignPublicIp: true,
      securityGroups: [securityGroupAPP],
    });
    service.attachToApplicationTargetGroup(targetGroup);
  }
}

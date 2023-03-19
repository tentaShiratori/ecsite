import * as cdk from "aws-cdk-lib";
import * as ecs from "aws-cdk-lib/aws-ecs";
import * as elbv2 from "aws-cdk-lib/aws-elasticloadbalancingv2";
import * as ecr from "aws-cdk-lib/aws-ecr";
import * as iam from "aws-cdk-lib/aws-iam";
import * as logs from "aws-cdk-lib/aws-logs";
import type { Construct } from "constructs";
import * as ec2 from "aws-cdk-lib/aws-ec2";

export class ResourceStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "Vpc", {
      ipAddresses: ec2.IpAddresses.cidr("10.0.0.0/16"),
      maxAzs: 2,
      subnetConfiguration: [
        {
          name: "PublicSubnet",
          subnetType: ec2.SubnetType.PUBLIC,
        },
        {
          name: "PrivateSubnet",
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
        },
      ],
      gatewayEndpoints: {
        S3Endpoint: {
          service: ec2.GatewayVpcEndpointAwsService.S3,
        },
      },
    });
    // Create ECR Repository
    const repository = new ecr.Repository(this, "NextjsRepository", {
      repositoryName: "nextjs",
    });

    // Create ECS Cluster
    const cluster = new ecs.Cluster(this, "NextjsCluster", {
      vpc,
      clusterName: "nextjs-cluster",
    });

    // Create IAM Role for ECS Task Execution
    const taskRole = new iam.Role(this, "NextjsTaskRole", {
      assumedBy: new iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
    });
    taskRole.addToPolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: ["logs:CreateLogStream", "logs:PutLogEvents"],
        resources: ["arn:aws:logs:*:*:*"],
      })
    );

    // Create ECS Task Definition
    const taskDefinition = new ecs.FargateTaskDefinition(
      this,
      "NextjsTaskDefinition",
      {
        family: "nextjs-task",
        cpu: 256,
        memoryLimitMiB: 512,
        taskRole,
        executionRole: taskRole,
      }
    );

    // Add container to the task definition
    const container = taskDefinition.addContainer("nextjs-container", {
      image: ecs.ContainerImage.fromEcrRepository(repository),
      environment: {
        NODE_ENV: "production",
        PORT: "3000",
      },
      logging: ecs.LogDriver.awsLogs({
        streamPrefix: "nextjs",
        logRetention: logs.RetentionDays.ONE_MONTH,
      }),
    });

    // Expose port 3000
    container.addPortMappings({
      containerPort: 3000,
    });

    // Create Application Load Balancer
    new elbv2.ApplicationLoadBalancer(this, "NextjsLoadBalancer", {
      vpc: cluster.vpc,
      internetFacing: true,
    });

    // Create Security Group for the Application Load Balancer
    const securityGroup = new ec2.SecurityGroup(
      this,
      "NextjsLoadBalancerSecurityGroup",
      {
        vpc: cluster.vpc,
        allowAllOutbound: true,
      }
    );
    securityGroup.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(80));
  }
}

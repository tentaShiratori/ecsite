import * as cdk from "aws-cdk-lib";
import type { Construct } from "constructs";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as ecs from "aws-cdk-lib/aws-ecs";
import * as ecr from "aws-cdk-lib/aws-ecr";
import * as elbv2 from "aws-cdk-lib/aws-elasticloadbalancingv2";
import { ApplicationProtocol } from "aws-cdk-lib/aws-elasticloadbalancingv2";
export class ResourceStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // VPCを作成
    const vpc = new ec2.Vpc(this, "MyVpc", {
      maxAzs: 2,
    });

    // ECSクラスターを作成
    const cluster = new ecs.Cluster(this, "MyCluster", {
      vpc: vpc,
    });

    // ECRリポジトリを作成
    const repo = new ecr.Repository(this, "nextjs");

    // タスク定義を作成
    const taskDefinition = new ecs.FargateTaskDefinition(this, "MyTaskDef");

    // コンテナを作成
    const container = taskDefinition.addContainer("MyContainer", {
      image: ecs.ContainerImage.fromEcrRepository(repo),
      memoryLimitMiB: 512,
      logging: new ecs.AwsLogDriver({
        streamPrefix: "MyApp",
      }),
    });

    // ポート3000でコンテナを公開
    container.addPortMappings({
      containerPort: 3000,
    });

    // タスクを実行するサービスを作成
    const service = new ecs.FargateService(this, "MyService", {
      cluster: cluster,
      taskDefinition: taskDefinition,
      desiredCount: 2,
      assignPublicIp: true,
    });
    const lb = new elbv2.ApplicationLoadBalancer(this, "LB", {
      vpc,
      internetFacing: true,
    });

    const listener = lb.addListener("Listener", {
      port: 80,
    });

    listener.addTargets("ECS", {
      protocol: ApplicationProtocol.HTTP,
      port: 3000,
      targets: [service],
    });
  }
}

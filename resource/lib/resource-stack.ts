import * as cdk from "aws-cdk-lib";
import type { Construct } from "constructs";
import { Function, Runtime, Code } from "aws-cdk-lib/aws-lambda";
import { LambdaRestApi, EndpointType } from "aws-cdk-lib/aws-apigateway";

export class ResourceStack extends cdk.Stack {
  // eslint-disable-next-line @typescript-eslint/no-useless-constructor
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // defines an AWS Lambda resource
    const hello = new Function(this, "HelloHandler", {
      runtime: Runtime.NODEJS_18_X, // execution environment
      code: Code.fromAsset("src/"), // code loaded from the "lambda" directory
      handler: "lambda/hello.handler", // file is "hello", function is "handler"
    });

    // defines an API Gateway REST API resource backed by our "hello" function.
    new LambdaRestApi(this, "Endpoint", {
      handler: hello,
      endpointTypes: [EndpointType.EDGE],
    });
  }
}

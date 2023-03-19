import type { Construct } from "constructs";

export abstract class Resource {
  abstract createResources(scope: Construct): void;

  protected createResourceName(scope: Construct, originalName: string): string {
    const systemName: string = scope.node.tryGetContext("systemName");
    const envType: string = scope.node.tryGetContext("envType");
    const resourceNamePrefix = `${systemName}-${envType}-`;

    return `${resourceNamePrefix}${originalName}`;
  }
}

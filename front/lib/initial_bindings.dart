import 'package:front/driver/product_repository_imple.dart';
import 'package:get/get.dart';
import 'package:openapi/api.dart';

import 'domain/product_repository.dart';

class InitialBindings implements Bindings {
  @override
  void dependencies() {
    Get.lazyPut(() => ApiClient(basePath: "http://10.0.2.2:8000"));
    Get.lazyPut(() => ProductsApi(Get.find<ApiClient>()));
    Get.lazyPut<ProductRepository>(
        () => ProductRepositoryImple(api: Get.find()));
  }
}

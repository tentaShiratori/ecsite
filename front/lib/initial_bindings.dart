import 'package:front/driver/product_repository_imple.dart';
import 'package:front/mocks/repository/mock_product_repository.dart';
import 'package:front/pages/app_nav_controller.dart';
import 'package:front/pages/home/home_controller.dart';
import 'package:front/pages/home/home_nav_controller.dart';
import 'package:front/pages/home/product_detail/product_detail.dart';
import 'package:front/pages/home/product_detail/product_detail_controller.dart';
import 'package:get/get.dart';
import 'package:openapi/api.dart';

import 'domain/product_repository.dart';

class InitialBindings implements Bindings {
  @override
  void dependencies() {
    Get.lazyPut(() => ApiClient(basePath: "http://10.0.2.2:8000"));
    Get.lazyPut(() => ProductsApi(Get.find<ApiClient>()));
    // Get.lazyPut<ProductRepository>(
    //     () => ProductRepositoryImple(api: Get.find()));
    Get.lazyPut<ProductRepository>(() => MockProductRepository());
    Get.lazyPut(() => AppNavController());
    Get.lazyPut(() => HomeNavController(),fenix: true);
    Get.lazyPut(() => HomeController(productRepository: Get.find()),fenix: true);
    Get.lazyPut(() => ProductDetailController(productRepository: Get.find()),fenix: true);
  }
}



import 'package:get/get.dart';
import 'package:openapi/api.dart';

void initDeps() {
    Get.lazyPut(()=> DefaultApi(ApiClient(basePath: "http://192.168.10.102:8080")));
}
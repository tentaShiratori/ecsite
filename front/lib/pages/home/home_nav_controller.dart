import 'package:flutter/material.dart';
import 'package:front/pages/home/product_detail/product_detail.dart';
import 'package:front/pages/home/product_list/product_list.dart';
import 'package:front/pages/others/others.dart';
import 'package:get/get.dart';

class HomeNavController extends GetxController {
  var currentIndex = 0.obs;
  static String productList = "/products";
  static String productDetail = "/products/:id";

  static String getProductDetail(int id) =>
      productDetail.replaceAll(":id", id.toString());

  Route? onGenerateRoute(RouteSettings settings) {
    print(settings.name);
    if (settings.name == productList) {
      return GetPageRoute(
        settings: settings,
        page: () => ProductList(),
        transition: Transition.rightToLeft,
      );
    }

    if (settings.name!.startsWith(productDetail.replaceAll(":id", ""))) {
      var id = settings.name!.substring(productDetail.replaceAll(":id", "").length) ?? "";
      return GetPageRoute(
        settings: settings,
        page: () => ProductDetail(id: int.parse(id)),
        transition: Transition.rightToLeft,
      );
    }

    return null;
  }

  void toProductDetail(int id) {
    Get.toNamed(getProductDetail(id), id: 2);
  }
}

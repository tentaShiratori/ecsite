import 'package:flutter/material.dart';
import 'package:front/domain/product_repository.dart';
import 'package:front/pages/home/product_detail/product_detail.dart';
import 'package:front/pages/home/product_list/product_list.dart';
import 'package:front/pages/others/others.dart';
import 'package:get/get.dart';


class HomeController extends GetxController {
  final ProductRepository productRepository;

  HomeController({required this.productRepository});

  var currentIndex = 0.obs;
  final pages = <String>['/browse', '/history', '/settings'];

  void changePage(int index) {
    Get.toNamed(pages[index], id: 2);
  }


  Route? onGenerateRoute(RouteSettings settings) {
    if (settings.name == '/browse')
      return GetPageRoute(
        settings: settings,
        page: () => ProductList(),
        transition: Transition.rightToLeft,
      );

    if (settings.name == '/history')
      return GetPageRoute(
        settings: settings,
        page: () => ProductDetail(),
        transition: Transition.rightToLeft,
      );

    if (settings.name == '/settings')
      return GetPageRoute(
        settings: settings,
        page: () => Others(),
        transition: Transition.noTransition,
      );

    return null;
  }

  void toNext(String path) {
    Get.toNamed(path,id: 2);
  }
}

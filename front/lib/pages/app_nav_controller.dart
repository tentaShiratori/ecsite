import 'package:flutter/material.dart';
import 'package:front/pages/account/account.dart';
import 'package:front/pages/others/others.dart';
import 'package:get/get.dart';

import 'cart/cart.dart';
import 'home/home.dart';

class AppNavController extends GetxController {

  AppNavController();

  var currentIndex = 0.obs;

  final pages = <String>['/browse', '/history', '/settings',"/others"];

  void changePage(int index) {
    currentIndex.value = index;
    Get.offNamed(pages[index], id: 1);
  }

  Route? onGenerateRoute(RouteSettings settings) {
    if (settings.name == '/browse')
      return GetPageRoute(
        settings: settings,
        page: () => Home(),
        transition: Transition.noTransition,
      );

    if (settings.name == '/history')
      return GetPageRoute(
        settings: settings,
        page: () => Account(),
        transition: Transition.noTransition,
      );

    if (settings.name == '/settings')
      return GetPageRoute(
        settings: settings,
        page: () => Cart(),
        transition: Transition.noTransition,
      );
    if (settings.name == '/others')
      return GetPageRoute(
        settings: settings,
        page: () => Others(),
        transition: Transition.noTransition,
      );

    return null;
  }
}

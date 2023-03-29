import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:front/pages/app_nav_controller.dart';
import 'package:get/get.dart';
import './widgets/my_bottom_navigation_bar.dart';
import '../domain/product_repository.dart';

class App extends HookWidget {
  final String title;

  const App({super.key, required this.title});

  @override
  Widget build(BuildContext context) {
    var controller = Get.find<AppNavController>();
    return Scaffold(
      body: Navigator(
        key: Get.nestedKey(1),
        initialRoute: '/browse',
        onGenerateRoute: controller.onGenerateRoute,
      ),
      bottomNavigationBar: Obx(
        () => MyBottomNavigationBar(
            currentIndex: controller.currentIndex.value,
            onTap: controller.changePage),
      ),
    );
  }
}

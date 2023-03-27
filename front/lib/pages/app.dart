import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:front/pages/app_controller.dart';
import 'package:get/get.dart';
import './widgets/my_bottom_navigation_bar.dart';
import '../domain/product_repository.dart';

class App extends HookWidget {
  final String title;

  const App({super.key, required this.title});

  @override
  Widget build(BuildContext context) {
    var controller = Get.find<AppController>();
    return Scaffold(
      body: Navigator(
        key: Get.nestedKey(1),
        initialRoute: '/browse',
        onGenerateRoute: controller.onGenerateRoute,
      ),
      bottomNavigationBar: MyBottomNavigationBar(onTap: controller.changePage),
      // Obx(
      //   () => BottomNavigationBar(
      //     items: [
      //       const BottomNavigationBarItem(
      //         icon: Icon(Icons.search),
      //         label: 'Browse',
      //       ),
      //       const BottomNavigationBarItem(
      //         icon: Icon(Icons.history),
      //         label: 'History',
      //       ),
      //       BottomNavigationBarItem(
      //         icon: Stack(
      //           children: [
      //             Icon(Icons.shopping_cart),
      //             Positioned(
      //                 top: 0,
      //                 right: 8.0,
      //                 child: Center(
      //                   child: Text(
      //                     1.toString(),
      //                   ),
      //                 ))
      //           ],
      //         ),
      //         label: 'Settings',
      //       ),
      //       const BottomNavigationBarItem(
      //         icon: Icon(Icons.settings),
      //         label: 'Others',
      //       ),
      //     ],
      //     currentIndex: controller.currentIndex.value,
      //     selectedItemColor: Colors.pink,
      //     unselectedItemColor: Colors.grey,
      //     onTap: controller.changePage,
      //   ),
      // ),
    );
  }
}

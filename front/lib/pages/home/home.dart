import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:get/get.dart';

import '../../lib/navigation_observer/is_first_navigation_observer.dart';
import 'home_nav_controller.dart';

class Home extends HookWidget {
  Home({Key? key}) : super(key: key);
  var nestedKey = Get.nestedKey(2);

  @override
  Widget build(BuildContext context) {
    var navController = Get.find<HomeNavController>();
    var isFirst = useState(false);
    return Scaffold(
      appBar: AppBar(
        leading: isFirst.value
            ? BackButton(
                onPressed: () {
                  Get.back(id: 2);
                },
              )
            : null,
        title: Text("aaa"),
      ),
      body: Navigator(
          observers: [IsFirstNavigationObserver(isFirst: isFirst)],
          key: nestedKey,
          initialRoute: HomeNavController.productList,
          onGenerateRoute: navController.onGenerateRoute),
    );
  }
}

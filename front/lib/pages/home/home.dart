import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:front/pages/home/home_controller.dart';
import 'package:get/get.dart';

import '../../lib/navigation_observer/is_first_navigation_observer.dart';

class Home extends HookWidget {
  Home({Key? key}) : super(key: key);
  var nestedKey = Get.nestedKey(2);

  @override
  Widget build(BuildContext context) {
    var controller = Get.find<HomeController>();
    var can = useState(false);
    return Scaffold(
      appBar: AppBar(
        leading: can.value
            ? BackButton(
                onPressed: () {
                  Get.back(id: 2);
                },
              )
            : null,
        title: Text("aaa"),
      ),
      body: Navigator(
          observers: [IsFirstNavigationObserver(isFirst: can)],
          key: nestedKey,
          initialRoute: '/browse',
          onGenerateRoute: controller.onGenerateRoute),
    );
  }
}

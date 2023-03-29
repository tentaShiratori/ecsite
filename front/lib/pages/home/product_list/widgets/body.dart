import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:front/pages/home/home_controller.dart';
import 'package:get/get.dart';
import 'package:skeletons/skeletons.dart';

import '../../home_nav_controller.dart';

class Body extends HookWidget {
  const Body({super.key});

  @override
  Widget build(BuildContext context) {
    var controller = Get.find<HomeController>();
    var navController = Get.find<HomeNavController>();
    useEffect(() {
      controller.load();
    });
    return SingleChildScrollView(
        child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
          Obx(() => Column(
                  children: controller.products.map((product) {
                return GestureDetector(
                    behavior: HitTestBehavior.translucent,
                    onTap: () {
                      navController.toProductDetail(product.pk);
                    },
                    child: Column(children: [
                      Container(
                        width: Get.width,
                        height: 230,
                        child: CachedNetworkImage(
                          placeholder: (context, url) => SkeletonAvatar(),
                          imageUrl: product.image,
                        ),
                      ),
                      Text(product.name)
                    ]));
              }).toList()))
        ]));
  }
}

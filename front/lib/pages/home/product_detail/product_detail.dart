
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:front/pages/home/home_controller.dart';
import 'package:get/get.dart';

class ProductDetail extends HookWidget {
  const ProductDetail({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var controller = Get.find<HomeController>();
    return Scaffold(body: Column(
      children: [
        Text("aaa"),
        GestureDetector(
          onTap: () {
            controller.toNext("/history");
          },
          child: Text("Push"),
        )
      ],
    ));
  }
}

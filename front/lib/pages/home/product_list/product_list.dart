import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:front/pages/home/home_controller.dart';
import 'package:front/pages/home/product_list/widgets/body.dart';
import 'package:get/get.dart';

class ProductList extends HookWidget {
  const ProductList({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var controller = Get.find<HomeController>();
    return Scaffold(
        body: Body());
  }
}

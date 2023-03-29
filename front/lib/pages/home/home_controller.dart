import 'package:flutter/material.dart';
import 'package:front/domain/product_repository.dart';
import 'package:front/pages/home/product_detail/product_detail.dart';
import 'package:front/pages/home/product_list/product_list.dart';
import 'package:front/pages/others/others.dart';
import 'package:get/get.dart';


class HomeController extends GetxController {
  final ProductRepository productRepository;

  HomeController({required this.productRepository});
  var products = [].obs;

  void load()async {
      var result = await productRepository.list();
      products.assignAll(result);
  }
}

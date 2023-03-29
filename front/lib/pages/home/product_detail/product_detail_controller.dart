import 'package:flutter/material.dart';
import 'package:front/domain/product.dart';
import 'package:front/domain/product_repository.dart';
import 'package:front/pages/home/product_detail/product_detail.dart';
import 'package:front/pages/home/product_list/product_list.dart';
import 'package:front/pages/others/others.dart';
import 'package:get/get.dart';


class ProductDetailController extends GetxController {
  final ProductRepository productRepository;

  ProductDetailController({required this.productRepository});

  var product = Rx<Product?>(null);
  void load()async {
      var result = await productRepository.get();
      product.value = result;
  }
}

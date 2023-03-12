import 'dart:ffi';

class Product {
  final String image;
  final String name;
  final double price;
  final String description;

  const Product(
      {required String image,
      required this.name,
      required this.price,
      required this.description})
      : image = "http://10.0.2.2:8000" + image;
}

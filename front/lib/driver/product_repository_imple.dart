import 'package:front/domain/product.dart';
import 'package:front/domain/product_repository.dart';
import 'package:get/get.dart';
import 'package:openapi/api.dart' as openapi;

class ProductRepositoryImple extends GetxService implements ProductRepository {
  final openapi.ProductsApi api;

  ProductRepositoryImple({required this.api});

  @override
  Future<List<Product>> list() async {
    var products = await api.listProducts();
    if (products == null) return [];
    return products
        .map((e) => Product(
            pk:0,
            image: e.image,
            name: e.name,
            price: e.price.toDouble(),
            description: e.description))
        .toList();
  }

  @override
  Future<Product> get() {
    // TODO: implement get
    throw UnimplementedError();
  }
}

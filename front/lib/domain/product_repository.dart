import 'package:front/domain/product.dart';

abstract class ProductRepository {
  Future<List<Product>> list();
}

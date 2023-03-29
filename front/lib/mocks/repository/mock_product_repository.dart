import 'package:front/domain/product.dart';
import 'package:front/domain/product_repository.dart';
import 'package:front/mocks/entity/mock_product.dart';
import 'package:get/get.dart';

class MockProductRepository extends GetxService implements ProductRepository {
  MockProductRepository();

  Future<List<Product>> list() async {
    await new Future.delayed(new Duration(seconds: 3));
    List<Product> list = [];
    for (var i = 0; i < 20; i++) {
      list.add(MockProduct.generate());
    }
    return list;
  }

  Future<Product> get() async {
    return MockProduct.generate();
  }
}

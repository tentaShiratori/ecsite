import 'package:front/domain/product.dart';
import 'package:faker/faker.dart';
import 'dart:math';

var pk = 1;

class MockProduct extends Product {
  MockProduct(
      {required super.pk,
      required super.image,
      required super.name,
      required super.price,
      required super.description});

  static MockProduct generate() {
    var faker = Faker();
    var random = Random();
    return MockProduct(
        pk: pk++,
        image: faker.internet.uri("http"),
        name: faker.food.cuisine(),
        price: random.nextInt(50) + 50,
        description: faker.lorem.random.numberOfLength(100));
  }
}

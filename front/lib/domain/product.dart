class Product {
  final int pk;
  final String image;
  final String name;
  final double price;
  final String description;

  Product(
      {
        required this.pk,
        required String image,
      required this.name,
      required this.price,
      required this.description})
      : image = image.replaceFirst(RegExp(r"localhost"), "10.0.2.2");
}

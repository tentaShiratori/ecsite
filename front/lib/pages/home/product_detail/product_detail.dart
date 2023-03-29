import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:front/pages/home/product_detail/product_detail_controller.dart';
import 'package:get/get.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:skeletons/skeletons.dart';

class ProductDetail extends HookWidget {
  final int id;

  const ProductDetail({Key? key, required this.id}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var controller = Get.find<ProductDetailController>();
    useEffect((){
      controller.load();
    });
    return Scaffold(
      body: Obx(
        () => controller.product.value != null ? Column(
          children: [
            Container(
              width: Get.width,
              height: 230,
              child: CachedNetworkImage(
                placeholder: (context, url) => SkeletonAvatar(),
                imageUrl: controller.product.value!.image,
              ),
            ),
            Text(controller.product.value!.name),
            TextButton(onPressed: (){}, child: Text("カートに入れる"))
          ],
        ):Text("読み込み中"),
      ),
    );
  }
}

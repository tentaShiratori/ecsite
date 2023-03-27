// import 'package:cached_network_image/cached_network_image.dart';
// import 'package:flutter/material.dart';
// import 'package:flutter_hooks/flutter_hooks.dart';
// import 'package:front/pages/app_controller.dart';
// import 'package:get/get.dart';
// import 'package:skeletons/skeletons.dart';
//
// import '../../domain/product_repository.dart';
// import '../../route_helper.dart';
//
// class Body extends HookWidget {
//   const Body({super.key});
//
//   @override
//   Widget build(BuildContext context) {
//     var controller = Get.find<AppController>();
//     useEffect(() {
//       controller.load();
//     });
//     return SingleChildScrollView(
//         child: Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             children: <Widget>[
//           Obx(() => Column(
//                   children: controller.products.map((product) {
//                 return GestureDetector(
//                     onTap: () {
//                       Get.toNamed(RouteHelper.getProductsRoute(product.pk));
//                     },
//                     child: Column(children: [
//                       Container(
//                         width: Get.width,
//                         height: 230,
//                         child: CachedNetworkImage(
//                           placeholder: (context, url) => SkeletonAvatar(),
//                           imageUrl: product.image,
//                         ),
//                       ),
//                       Text(product.name)
//                     ]));
//               }).toList()))
//         ]));
//   }
// }

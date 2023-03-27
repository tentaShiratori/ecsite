import 'package:front/pages/app.dart';
import 'package:get/get.dart';

class RouteHelper{
  static const initial = "/";
  static const splash ="/splash";
  static const productDetail = "/products/:id";
  static String getInitialRoute()=>"$initial";
  static String getSplashRoute()=>"$splash";
  static String getProductsRoute(int pageId)=>productDetail.replaceAll(":id",pageId.toString());
  static List<GetPage> routes=[
    GetPage(name:initial,page:(){
      return App(title: "hello",);
    }),
    // GetPage(name: productDetail, page: (){
    //   var id = Get.parameters["id"] ?? "";
    //   return ProductDetail(id: int.parse(id));
    // })
  ];

}
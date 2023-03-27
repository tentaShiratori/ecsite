import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:get/get.dart';
import 'package:skeletons/skeletons.dart';

class Others extends HookWidget {

  const Others({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("aaa"),
        ),
        body: Column(children: [
          Container(
              width: Get.width,
              height: 200,
              child: CachedNetworkImage(
                placeholder: (context, url) => SkeletonAvatar(),
                imageUrl: "",
              )),
          Text("others")
        ]));
  }
}

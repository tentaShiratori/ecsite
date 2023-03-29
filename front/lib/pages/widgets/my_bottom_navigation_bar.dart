import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:get/get.dart';

class MyBottomNavigationBar extends HookWidget {
  final int currentIndex;
  final void Function(int value) onTap;

  const MyBottomNavigationBar({Key? key,required this.currentIndex,required this.onTap}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
        height: 60,
        decoration: BoxDecoration(
          border: Border.all(color: Colors.grey),
        ),
        child: Stack(
          children: [
            Positioned(
              left: Get.width / 8 - 30 + Get.width / 4 * currentIndex,
              child: Container(
                width: 60,
                height: 6,
                decoration: const BoxDecoration(
                  color: Colors.pink,
                  borderRadius: BorderRadius.only(
                    bottomLeft: Radius.circular(6),
                    bottomRight: Radius.circular(6),
                  ),
                ),
              ),
            ),
            Row(
              children: ["Home", "Account", "Cart", "Others"]
                  .asMap()
                  .entries
                  .map((entry) {
                var i = entry.key;
                var item = entry.value;
                return Expanded(
                  child: GestureDetector(
                    behavior: HitTestBehavior.translucent,
                    onTap: () {
                      onTap(i);
                    },
                    child: Stack(
                      children: [
                        Center(
                          child: Text(item),
                        )
                      ],
                    ),
                  ),
                );
              }).toList(),
            ),
          ],
        ));
  }
}

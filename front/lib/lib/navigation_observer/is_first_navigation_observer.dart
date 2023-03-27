import 'package:flutter/material.dart';

class IsFirstNavigationObserver extends NavigatorObserver {
  final ValueNotifier<bool> isFirst;
  IsFirstNavigationObserver({required this.isFirst});

  @override
  void didPush(Route<dynamic> route, Route<dynamic>? previousRoute) {
    isFirst.value = !route.isFirst;
    super.didPush(route, previousRoute);
  }

  @override
  void didPop(Route<dynamic> route, Route<dynamic>? previousRoute) {
    isFirst.value =  !(previousRoute?.isFirst==true);
  }
}
import 'package:flutter/material.dart';
import 'package:get/get.dart';

import 'initial_bindings.dart';
import 'pages/home.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: const Home(title: 'Flutter Demo Home Page'),
        initialBinding: InitialBindings());
  }
}





















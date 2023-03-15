import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:get/get.dart';

import '../domain/product_repository.dart';

class Home extends HookWidget {
  final String title;

  const Home({super.key, required this.title});

  @override
  Widget build(BuildContext context) {
    var productRepository = Get.find<ProductRepository>();
    var counter = useState(0);
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '${counter.value}',
              style: Theme.of(context).textTheme.headline4,
            ),
            FutureBuilder(
                future: productRepository.list(),
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return const Text("読み込み中");
                  }
                  var data = snapshot.data;
                  if (snapshot.hasData && data != null) {
                    return ListView.builder(
                      shrinkWrap: true,
                      itemCount: data.length,
                      itemBuilder: (context, index) {
                        return Column(children: [
                          Image(
                            image: NetworkImage(data[index].image),
                          ),
                          Text(data[index].name)
                        ]);
                      },
                    );
                  }
                  return const Text("データが存在しません");
                })
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          counter.value++;
        },
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}

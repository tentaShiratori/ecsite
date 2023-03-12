# openapi.api.DefaultApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProduct**](DefaultApi.md#createproduct) | **POST** / | 
[**listProducts**](DefaultApi.md#listproducts) | **GET** / | 


# **createProduct**
> Product createProduct(product)





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = DefaultApi();
final product = Product(); // Product | 

try {
    final result = api_instance.createProduct(product);
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->createProduct: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listProducts**
> List<Product> listProducts()





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = DefaultApi();

try {
    final result = api_instance.listProducts();
    print(result);
} catch (e) {
    print('Exception when calling DefaultApi->listProducts: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List<Product>**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


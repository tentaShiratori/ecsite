# openapi.api.ProductsApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProduct**](ProductsApi.md#createproduct) | **POST** /products/ | 
[**destroyProduct**](ProductsApi.md#destroyproduct) | **DELETE** /products/{id}/ | 
[**listProducts**](ProductsApi.md#listproducts) | **GET** /products/ | 
[**retrieveProduct**](ProductsApi.md#retrieveproduct) | **GET** /products/{id}/ | 
[**updateProduct**](ProductsApi.md#updateproduct) | **PUT** /products/{id}/ | 


# **createProduct**
> Product createProduct(product)





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = ProductsApi();
final product = Product(); // Product | 

try {
    final result = api_instance.createProduct(product);
    print(result);
} catch (e) {
    print('Exception when calling ProductsApi->createProduct: $e\n');
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

# **destroyProduct**
> destroyProduct(id)





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = ProductsApi();
final id = id_example; // String | 

try {
    api_instance.destroyProduct(id);
} catch (e) {
    print('Exception when calling ProductsApi->destroyProduct: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listProducts**
> List<Product> listProducts()





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = ProductsApi();

try {
    final result = api_instance.listProducts();
    print(result);
} catch (e) {
    print('Exception when calling ProductsApi->listProducts: $e\n');
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

# **retrieveProduct**
> Product retrieveProduct(id)





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = ProductsApi();
final id = id_example; // String | 

try {
    final result = api_instance.retrieveProduct(id);
    print(result);
} catch (e) {
    print('Exception when calling ProductsApi->retrieveProduct: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateProduct**
> Product updateProduct(id, product)





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = ProductsApi();
final id = id_example; // String | 
final product = Product(); // Product | 

try {
    final result = api_instance.updateProduct(id, product);
    print(result);
} catch (e) {
    print('Exception when calling ProductsApi->updateProduct: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **product** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


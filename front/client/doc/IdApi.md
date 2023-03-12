# openapi.api.IdApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destroyProduct**](IdApi.md#destroyproduct) | **DELETE** /{id}/ | 
[**partialUpdateProduct**](IdApi.md#partialupdateproduct) | **PATCH** /{id}/ | 
[**retrieveProduct**](IdApi.md#retrieveproduct) | **GET** /{id}/ | 
[**updateProduct**](IdApi.md#updateproduct) | **PUT** /{id}/ | 


# **destroyProduct**
> destroyProduct(id)





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = IdApi();
final id = id_example; // String | A unique integer value identifying this product.

try {
    api_instance.destroyProduct(id);
} catch (e) {
    print('Exception when calling IdApi->destroyProduct: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A unique integer value identifying this product. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partialUpdateProduct**
> Product partialUpdateProduct(id, product)





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = IdApi();
final id = id_example; // String | A unique integer value identifying this product.
final product = Product(); // Product | 

try {
    final result = api_instance.partialUpdateProduct(id, product);
    print(result);
} catch (e) {
    print('Exception when calling IdApi->partialUpdateProduct: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A unique integer value identifying this product. | 
 **product** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveProduct**
> Product retrieveProduct(id)





### Example
```dart
import 'package:openapi/api.dart';

final api_instance = IdApi();
final id = id_example; // String | A unique integer value identifying this product.

try {
    final result = api_instance.retrieveProduct(id);
    print(result);
} catch (e) {
    print('Exception when calling IdApi->retrieveProduct: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A unique integer value identifying this product. | 

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

final api_instance = IdApi();
final id = id_example; // String | A unique integer value identifying this product.
final product = Product(); // Product | 

try {
    final result = api_instance.updateProduct(id, product);
    print(result);
} catch (e) {
    print('Exception when calling IdApi->updateProduct: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A unique integer value identifying this product. | 
 **product** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


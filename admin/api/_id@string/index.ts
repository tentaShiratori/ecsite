/* eslint-disable */
import type * as Types from '../@types'

export type Methods = {
  get: {
    status: 200
    resBody: Types.Product
  }

  put: {
    status: 200
    resBody: Types.Product
    reqFormat: FormData
    reqBody: Types.Product
  }

  patch: {
    status: 200
    resBody: Types.Product
    reqFormat: FormData
    reqBody: Types.Product
  }

  delete: {
    status: 204
  }
}

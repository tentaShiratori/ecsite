/* eslint-disable */
import type * as Types from "../@types";

export type Methods = {
  get: {
    status: 200;
    resBody: Types.Product[];
  };

  post: {
    status: 201;
    resBody: Types.Product;
    reqFormat: FormData;
    reqBody: Types.Product;
  };
};

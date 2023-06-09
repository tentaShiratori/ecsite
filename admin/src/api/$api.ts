import type { AspidaClient, BasicHeaders } from "aspida";
import type { Methods as Methods0 } from "./products";
import type { Methods as Methods1 } from "./products/_id@string";

const api = <T>({ baseURL, fetch }: AspidaClient<T>) => {
  const prefix = (baseURL === undefined ? "" : baseURL).replace(/\/$/, "");
  const PATH0 = "/products";
  const GET = "GET";
  const POST = "POST";
  const PUT = "PUT";
  const DELETE = "DELETE";

  return {
    products: {
      _id: (val1: string) => {
        const prefix1 = `${PATH0}/${val1}`;

        return {
          get: (option?: { config?: T | undefined } | undefined) =>
            fetch<
              Methods1["get"]["resBody"],
              BasicHeaders,
              Methods1["get"]["status"]
            >(prefix, prefix1, GET, option).json(),
          $get: (option?: { config?: T | undefined } | undefined) =>
            fetch<
              Methods1["get"]["resBody"],
              BasicHeaders,
              Methods1["get"]["status"]
            >(prefix, prefix1, GET, option)
              .json()
              .then((r) => r.body),
          put: (option: {
            body: Methods1["put"]["reqBody"];
            config?: T | undefined;
          }) =>
            fetch<
              Methods1["put"]["resBody"],
              BasicHeaders,
              Methods1["put"]["status"]
            >(prefix, prefix1, PUT, option, "FormData").json(),
          $put: (option: {
            body: Methods1["put"]["reqBody"];
            config?: T | undefined;
          }) =>
            fetch<
              Methods1["put"]["resBody"],
              BasicHeaders,
              Methods1["put"]["status"]
            >(prefix, prefix1, PUT, option, "FormData")
              .json()
              .then((r) => r.body),
          delete: (option?: { config?: T | undefined } | undefined) =>
            fetch<void, BasicHeaders, Methods1["delete"]["status"]>(
              prefix,
              prefix1,
              DELETE,
              option
            ).send(),
          $delete: (option?: { config?: T | undefined } | undefined) =>
            fetch<void, BasicHeaders, Methods1["delete"]["status"]>(
              prefix,
              prefix1,
              DELETE,
              option
            )
              .send()
              .then((r) => r.body),
          $path: () => `${prefix}${prefix1}`,
        };
      },
      get: (option?: { config?: T | undefined } | undefined) =>
        fetch<
          Methods0["get"]["resBody"],
          BasicHeaders,
          Methods0["get"]["status"]
        >(prefix, PATH0, GET, option).json(),
      $get: (option?: { config?: T | undefined } | undefined) =>
        fetch<
          Methods0["get"]["resBody"],
          BasicHeaders,
          Methods0["get"]["status"]
        >(prefix, PATH0, GET, option)
          .json()
          .then((r) => r.body),
      post: (option: {
        body: Methods0["post"]["reqBody"];
        config?: T | undefined;
      }) =>
        fetch<
          Methods0["post"]["resBody"],
          BasicHeaders,
          Methods0["post"]["status"]
        >(prefix, PATH0, POST, option, "FormData").json(),
      $post: (option: {
        body: Methods0["post"]["reqBody"];
        config?: T | undefined;
      }) =>
        fetch<
          Methods0["post"]["resBody"],
          BasicHeaders,
          Methods0["post"]["status"]
        >(prefix, PATH0, POST, option, "FormData")
          .json()
          .then((r) => r.body),
      $path: () => `${prefix}${PATH0}`,
    },
  };
};

export type ApiInstance = ReturnType<typeof api>;
export default api;

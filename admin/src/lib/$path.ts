export const pagesPath = {
  products: {
    create: {
      $url: (url?: { hash?: string }) => ({
        pathname: "/products/create" as const,
        hash: url?.hash,
      }),
    },
  },
  $url: (url?: { hash?: string }) => ({
    pathname: "/" as const,
    hash: url?.hash,
  }),
};

export type PagesPath = typeof pagesPath;

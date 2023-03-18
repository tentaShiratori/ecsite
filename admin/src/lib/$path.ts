export const pagesPath = {
  products: {
    new: {
      $url: (url?: { hash?: string }) => ({
        pathname: "/products/new" as const,
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

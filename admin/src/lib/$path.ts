export const pagesPath = {
  "auth": {
    "sign_in": {
      $url: (url?: { hash?: string }) => ({ pathname: '/auth/sign_in' as const, hash: url?.hash })
    },
    "sign_up": {
      $url: (url?: { hash?: string }) => ({ pathname: '/auth/sign_up' as const, hash: url?.hash })
    }
  },
  "products": {
    "new": {
      $url: (url?: { hash?: string }) => ({ pathname: '/products/new' as const, hash: url?.hash })
    }
  },
  $url: (url?: { hash?: string }) => ({ pathname: '/' as const, hash: url?.hash })
}

export type PagesPath = typeof pagesPath

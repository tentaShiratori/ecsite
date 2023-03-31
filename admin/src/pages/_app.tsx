import "@/styles/globals.css";
import type { AppProps } from "next/app";
import { ChakraProvider, Toast } from "@chakra-ui/react";
import awsconfig from "../aws-exports";
import { Amplify } from "aws-amplify";
Amplify.configure(awsconfig);
export default function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <Component {...pageProps} />
    </ChakraProvider>
  );
}

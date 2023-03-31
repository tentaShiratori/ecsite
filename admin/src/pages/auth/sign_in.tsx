import { Auth } from "aws-amplify";
import { SubmitHandler, useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { defaultApi } from "@/lib/api";
import {
  Input,
  Modal,
  ModalOverlay,
  Spinner,
  useToast,
} from "@chakra-ui/react";
import { css } from "@emotion/react";
import Link from "next/link";
import { pagesPath } from "@/lib/$path";
import { useEffect } from "react";
const schema = z.object({
  email: z.string(),
  password: z.string(),
});

type Inputs = z.infer<typeof schema>;

async function signIn(username: string, password: string) {
  try {
    const { user } = await Auth.signIn({
      username,
      password,
    });
    console.log(user);
  } catch (error) {
    console.log("error signing up:", error);
  }
}

export default function SignIn() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<Inputs>({ resolver: zodResolver(schema) });
  const toast = useToast();
  const onSubmit: SubmitHandler<Inputs> = async (d) => {
    try {
      await signIn(d.email, d.password);
      toast({ title: "Product created.", status: "success" });
    } catch (e) {
      toast({
        title: "Oops!",
        description: "Something Error",
        status: "error",
      });
    }
  };
  useEffect(() => {
    Auth.currentSession().then((res) => {
      let accessToken = res.getAccessToken();
      let jwt = accessToken.getJwtToken();

      //You can print them to see the full objects
      console.log(`myAccessToken: ${JSON.stringify(accessToken)}`);
      console.log(`myJwt: ${jwt}`);
    });
  }, []);
  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label htmlFor="email">Email</label>
          <Input id="email" type="text" {...register("email")} />
          {errors.email?.message}
        </div>
        <div>
          <label htmlFor="password">password</label>
          <Input id="password" type="password" {...register("password")} />
          {errors.password?.message}
        </div>
        <input type="submit" />
      </form>

      <Link href={pagesPath.products.new.$url()}>移動</Link>
    </div>
  );
}

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
const schema = z.object({
  email: z.string(),
  password: z.string(),
});

type Inputs = z.infer<typeof schema>;

async function signUp(username: string, password: string) {
  try {
    const { user } = await Auth.signUp({
      username,
      password,
      autoSignIn: {
        // optional - enables auto sign in after user is confirmed
        enabled: true,
      },
    });
    console.log(user);
  } catch (error) {
    console.log("error signing up:", error);
  }
}

export default function SignUp() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<Inputs>({ resolver: zodResolver(schema) });
  const toast = useToast();
  const onSubmit: SubmitHandler<Inputs> = async (d) => {
    try {
      await signUp(d.email, d.password);
      toast({ title: "Product created.", status: "success" });
    } catch (e) {
      toast({
        title: "Oops!",
        description: "Something Error",
        status: "error",
      });
    }
  };
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
      <Link href={pagesPath.auth.sign_in.$url()}>移動</Link>
    </div>
  );
}

import { SubmitHandler, useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { defaultApi } from "@/lib/api";
import {
  Input,
  Modal,
  ModalContent,
  ModalOverlay,
  Spinner,
  useToast,
} from "@chakra-ui/react";
import { css } from "@emotion/react";
const schema = z.object({
  name: z.string(),
  description: z.string(),
  price: z.number(),
  image: z.custom<FileList>().transform((file) => file[0]),
});

type Inputs = z.infer<typeof schema>;

export default function New() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<Inputs>({ resolver: zodResolver(schema) });
  const toast = useToast();
  const onSubmit: SubmitHandler<Inputs> = async (d) => {
    try {
      await defaultApi.products.$post({ body: d as any });
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
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label htmlFor="name">Name</label>
        <Input id="name" type="text" {...register("name")} />
        {errors.name?.message}
      </div>
      <div>
        <label htmlFor="description">Description</label>
        <Input id="description" type="text" {...register("description")} />
        {errors.description?.message}
      </div>
      <div>
        <label htmlFor="price">Price</label>
        <Input
          id="price"
          type="text"
          {...register("price", { valueAsNumber: true })}
        />
        {errors.price?.message}
      </div>
      <div>
        <label htmlFor="image">Image</label>
        <Input id="image" type="file" {...register("image")} />
        {errors.image?.message}
      </div>
      <input type="submit" disabled={isSubmitting} value="送信" />
      <Modal isOpen={isSubmitting} onClose={() => {}}>
        <ModalOverlay />
        <Spinner
          css={css`
            position: absolute;
            top: 0;
            bottom: 0;
            right: 0;
            left: 0;
            margin: auto;
          `}
        />
      </Modal>
    </form>
  );
}

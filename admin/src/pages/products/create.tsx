import { SubmitHandler, useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { defaultApi } from "@/lib/api";
import { Input } from "@chakra-ui/react";
import axios from "axios";

const schema = z.object({
  name: z.string(),
  description: z.string(),
  price: z.number(),
  image: z.custom<FileList>().transform((file) => file[0]),
});

type Inputs = z.infer<typeof schema>;

function plaintToFormData(plain: any) {
  const formData = new FormData();
  Object.entries(plain).forEach(([key, value]) => {
    if (typeof value === "number") {
      formData.append(key, value + "");
      return;
    }
    formData.append(key, value as any);
  });
  return formData;
}

export default function Create() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>({ resolver: zodResolver(schema) });
  const onSubmit: SubmitHandler<Inputs> = (d) => {
    const formData = plaintToFormData(d);
    defaultApi.products.$post({ body: d as any }).then((res) => {
      console.log(res);
    });
  };
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label htmlFor="name">Name</label>
        <Input type="text" {...register("name")} />
        {errors.name?.message}
      </div>
      <div>
        <label htmlFor="description">Description</label>
        <Input type="text" {...register("description")} />
        {errors.description?.message}
      </div>
      <div>
        <label htmlFor="price">Price</label>
        <Input type="text" {...register("price", { valueAsNumber: true })} />
        {errors.price?.message}
      </div>
      <div>
        <label htmlFor="image">Image</label>
        <Input type="file" {...register("image")} />
        {errors.image?.message}
      </div>
      <input type="submit" />
    </form>
  );
}

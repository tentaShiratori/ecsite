import { render, screen, waitFor } from "@testing-library/react";
import New from "@/pages/products/new";
import userEvent from "@testing-library/user-event";

const spies: any = {
  toast: jest.fn(),
};

jest.mock("@chakra-ui/react", () => {
  const actual = jest.requireActual("@chakra-ui/react");
  return {
    ...actual,
    useToast: () => spies.toast,
  };
});
jest.mock("../../lib/api", () => {
  return { defaultApi: { products: { $post: () => Promise.resolve() } } };
});

describe("Products/New", () => {
  it("should create products", async () => {
    render(<New />);
    await userEvent.type(screen.getByLabelText("Name"), "hello");
    await userEvent.type(screen.getByLabelText("Description"), "world");
    await userEvent.type(screen.getByLabelText("Price"), "1.22");
    const file = new File(["a", "b", "c"], "test.csv", { type: "text/csv" });
    await userEvent.upload(screen.getByLabelText("Image"), file);
    await userEvent.click(screen.getByText("送信"));
    await waitFor(() =>
      expect(spies.toast).toHaveBeenCalledWith({
        title: "Product created.",
        status: "success",
      })
    );
  });
});

import { render, screen } from "@testing-library/react";
import Home from "@/pages/index";
import userEvent from "@testing-library/user-event";
import { pagesPath } from "@/lib/$path";
import mockRouter from "next-router-mock";
import { MemoryRouterProvider } from "next-router-mock/MemoryRouterProvider";

jest.mock("next/router", () => require("next-router-mock"));
describe("Home", () => {
  it("render link", async () => {
    mockRouter.push("/initial-path");

    render(<Home />, { wrapper: MemoryRouterProvider });
    const link = screen.getByText("商品を作成する");
    expect(link).toBeInTheDocument();
    await userEvent.click(link);
    expect(mockRouter.asPath).toBe(pagesPath.products.new.$url().pathname);
  });
});

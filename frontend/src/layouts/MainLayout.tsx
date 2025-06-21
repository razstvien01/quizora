import Footer from "@/components/Footer";
import Header from "@/components/Header";
import type { ReactNode } from "react";

type MainLayoutProps = {
  children: ReactNode;
};

export default function MainLayout({ children }: MainLayoutProps) {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow px-4 py-8">{children}</main>
      <Footer />
    </div>
  );
}

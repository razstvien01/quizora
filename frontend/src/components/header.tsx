"use client";

import { Menu } from "lucide-react";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";

export default function SiteHeader() {
  const [open, setOpen] = useState(false);

  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
    setOpen(false);
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-14 items-center">
        <div className="mr-6 flex items-center space-x-2">
          <span className="text-2xl font-bold">Quizora</span>
        </div>

        {/* Desktop Navigation */}
        <nav className="hidden md:flex md:flex-1 md:items-center md:justify-between">
          <div className="flex items-center space-x-6 text-sm font-medium">
            <button
              onClick={() => scrollToSection("features")}
              className="transition-colors hover:text-foreground/80"
            >
              Features
            </button>
            <button
              onClick={() => scrollToSection("pricing")}
              className="transition-colors hover:text-foreground/80"
            >
              Pricing
            </button>
            <button
              onClick={() => scrollToSection("community")}
              className="transition-colors hover:text-foreground/80"
            >
              Community
            </button>
          </div>
          <Button>Get Started</Button>
        </nav>

        {/* Mobile Navigation */}
        <Sheet open={open} onOpenChange={setOpen}>
          <SheetTrigger asChild>
            <Button variant="ghost" size="icon" className="md:hidden">
              <Menu className="h-5 w-5" />
              <span className="sr-only">Toggle menu</span>
            </Button>
          </SheetTrigger>
          <SheetContent side="right">
            <nav className="flex flex-col space-y-4">
              <button
                onClick={() => scrollToSection("features")}
                className="text-left text-sm font-medium transition-colors hover:text-foreground/80"
              >
                Features
              </button>
              <button
                onClick={() => scrollToSection("pricing")}
                className="text-left text-sm font-medium transition-colors hover:text-foreground/80"
              >
                Pricing
              </button>
              <button
                onClick={() => scrollToSection("community")}
                className="text-left text-sm font-medium transition-colors hover:text-foreground/80"
              >
                Community
              </button>
              <Button className="w-full">Get Started</Button>
            </nav>
          </SheetContent>
        </Sheet>
      </div>
    </header>
  );
}

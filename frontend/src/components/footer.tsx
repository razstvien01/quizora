import { Github, Mail, Twitter } from "lucide-react";
import { Separator } from "@/components/ui/separator";

export default function SiteFooter() {
  return (
    <footer className="border-t bg-background">
      <div className="container py-8 md:py-12">
        <div className="grid grid-cols-2 gap-8 md:grid-cols-4">
          <div className="col-span-2 md:col-span-1">
            <p className="mt-2 text-xs text-muted-foreground">
              Made with ❤️ by{" "}
              <span className="font-semibold text-foreground">AhShits</span>
            </p>
          </div>

          <div>
            <h3 className="text-sm font-semibold">Product</h3>
            <ul className="mt-4 space-y-2 text-sm">
              <li>
                <button className="text-muted-foreground hover:text-foreground">
                  Features
                </button>
              </li>
              {/* <li>
                <button className="text-muted-foreground hover:text-foreground">
                  Pricing
                </button>
              </li> */}
              <li>
                <button className="text-muted-foreground hover:text-foreground">
                  Demo
                </button>
              </li>
            </ul>
          </div>

          <div>
            <h3 className="text-sm font-semibold">Support</h3>
            <ul className="mt-4 space-y-2 text-sm">
              <li>
                <button className="text-muted-foreground hover:text-foreground">
                  Help Center
                </button>
              </li>
              <li>
                <button className="text-muted-foreground hover:text-foreground">
                  Contact
                </button>
              </li>
              <li>
                <button className="text-muted-foreground hover:text-foreground">
                  Privacy
                </button>
              </li>
            </ul>
          </div>

          <div>
            <h3 className="text-sm font-semibold">Connect</h3>
            <div className="mt-4 flex space-x-4">
              <a
                href="https://twitter.com/quizora"
                className="text-muted-foreground hover:text-foreground"
              >
                <Twitter className="h-4 w-4" />
                <span className="sr-only">Twitter</span>
              </a>
              <a
                href="https://github.com/quizora"
                className="text-muted-foreground hover:text-foreground"
              >
                <Github className="h-4 w-4" />
                <span className="sr-only">GitHub</span>
              </a>
              <a
                href="mailto:support@quizora.com"
                className="text-muted-foreground hover:text-foreground"
              >
                <Mail className="h-4 w-4" />
                <span className="sr-only">Email</span>
              </a>
            </div>
          </div>
        </div>

        <Separator className="my-6" />

        <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
          <p className="text-center text-sm text-muted-foreground md:text-left">
            © {new Date().getFullYear()} Quizora. All rights reserved.
          </p>
          <div className="flex items-center space-x-4 text-sm text-muted-foreground">
            <button className="hover:text-foreground">Terms</button>
            <button className="hover:text-foreground">Privacy</button>
          </div>
        </div>
      </div>
    </footer>
  );
}

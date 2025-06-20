import { Helmet } from "react-helmet-async";

export default function NotFound() {
  return (
    <>
      <Helmet>
        <title>404 - Page Not Found | Quizora</title>
        <meta
          name="description"
          content="The page you are looking for does not exist."
        />
        <meta property="og:title" content="404 - Page Not Found" />
        <meta
          property="og:description"
          content="The page you are looking for does not exist."
        />
        <meta property="og:type" content="website" />
      </Helmet>

      <div className="flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-6xl font-bolD">404</h1>
          <p className="text-xl mt-4">Oops! Page not found.</p>
        </div>
      </div>
    </>
  );
}

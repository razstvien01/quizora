import MainLayout from "@/layouts/MainLayout";
import { Helmet } from "react-helmet-async";

function Home() {
  return (
    <>
      <Helmet>
        <title>Home | Quizora</title>
        <meta name="description" content="Welcome to the Quizora home page." />
      </Helmet>
      <MainLayout>
        <h1 className="text-3xl font-bold">Welcome to Quizora</h1>
        <p className="mt-4">This is the home page.</p>
      </MainLayout>
    </>
  );
}

export default Home;

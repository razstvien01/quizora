import { Helmet } from "react-helmet-async";

function Home() {
  return (
    <>
      <Helmet>
        <title>Home | Quizora</title>
        <meta name="description" content="Welcome to the Quizora home page."/>
      </Helmet>
      <h1>
        Welcome to Quizora!
      </h1>
    </>
  )
}

export default Home;

import Footer from "@/components/footer";
import Header from "@/components/header";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { benefits } from "@/constants/benefits";
import { features } from "@/constants/features";
import { stats } from "@/constants/stats";
import { useAuthRedirect } from "@/hooks/useAuthRedirect";
import {
  ArrowRight,
  CheckCircle,
  Download,
  Globe,
  Play,
  Star,
  Zap,
} from "lucide-react";
import { Helmet } from "react-helmet-async";

function Home() {
  useAuthRedirect();

  return (
    <>
      <Helmet>
        <title>
          Quizora - AI-Enhanced Learning Platform | Prepare Smarter for Exams
        </title>
        <meta
          name="description"
          content="Quizora is a modern, AI-enhanced learning platform that helps learners prepare smarter for exams through adaptive learning, dynamic mock exams, and intelligent study aids."
        />
        <meta
          name="keywords"
          content="AI learning, mock exams, adaptive learning, study platform, exam preparation"
        />
      </Helmet>
      <div className="flex min-h-screen flex-col">
        <Header />
        <main className="flex-1">
          {/* Hero Section */}
          <section className="container space-y-6 pb-8 pt-6 md:pb-12 md:pt-10 lg:py-32">
            <div className="mx-auto flex max-w-[58rem] flex-col items-center space-y-4 text-center">
              <Badge variant="secondary" className="rounded-2xl px-4 py-1.5">
                🚀 Empowering students through personalized learning experiences
              </Badge>
              <h1 className="font-heading text-3xl sm:text-5xl md:text-6xl lg:text-7xl">
                Prepare Smarter for Exams with{" "}
                <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                  AI-Enhanced Learning
                </span>
              </h1>
              <p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-xl sm:leading-8">
                Quizora combines adaptive learning, dynamic mock exams, and
                intelligent study aids to help you achieve better results in
                less time.
              </p>
              <div className="flex flex-col gap-4 sm:flex-row">
                <Button variant="default" size="lg" className="h-11 px-8">
                  <Play className="mr-2 h-4 w-4" />
                  Start Learning Free
                </Button>
                <Button variant="outline" size="lg" className="h-11 px-8">
                  <Download className="mr-2 h-4 w-4" />
                  Download App
                </Button>
              </div>
            </div>
          </section>

          {/* Stats Section */}
          <section className="container py-8 md:py-12 lg:py-24">
            <Card className="border-0 bg-muted/50">
              <CardContent className="p-6 md:p-10">
                <div className="grid grid-cols-2 gap-8 md:grid-cols-4">
                  {stats.map((stat, index) => (
                    <div key={index} className="text-center">
                      <div className="text-2xl font-bold text-primary md:text-4xl">
                        {stat.number}
                      </div>
                      <div className="text-sm text-muted-foreground">
                        {stat.label}
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </section>

          {/* Features Section */}
          <section
            id="features"
            className="container space-y-6 py-8 md:py-12 lg:py-24"
          >
            <div className="mx-auto flex max-w-[58rem] flex-col items-center space-y-4 text-center">
              <h2 className="font-heading text-3xl leading-[1.1] sm:text-3xl md:text-6xl">
                Powerful Features for Smarter Learning
              </h2>
              <p className="max-w-[85rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7">
                Everything you need to excel in your studies, powered by
                cutting-edge AI technology
              </p>
            </div>
            <div className="mx-auto grid justify-center gap-4 sm:grid-cols-2 md:max-w-[64rem] md:grid-cols-3">
              {features.map((feature, index) => (
                <Card key={index} className="relative overflow-hidden">
                  <CardHeader>
                    <div className="flex items-center space-x-2">
                      <feature.icon className={`h-6 w-6 ${feature.color}`} />
                      <CardTitle className="text-xl">{feature.title}</CardTitle>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <CardDescription className="text-base">
                      {feature.description}
                    </CardDescription>
                  </CardContent>
                </Card>
              ))}
            </div>
          </section>

          {/* Benefits Section */}
          <section className="container py-8 md:py-12 lg:py-24">
            <Card className="border-0 bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-950/20 dark:to-purple-950/20">
              <CardContent className="p-6 md:p-10">
                <div className="mx-auto max-w-4xl">
                  <div className="text-center space-y-4 mb-8">
                    <h2 className="font-heading text-3xl leading-[1.1] sm:text-3xl md:text-6xl">
                      Why Choose Quizora?
                    </h2>
                    <p className="text-xl text-muted-foreground">
                      Join thousands of students who have transformed their
                      learning experience
                    </p>
                  </div>
                  <div className="grid gap-4 md:grid-cols-2">
                    {benefits.map((benefit, index) => (
                      <div key={index} className="flex items-start space-x-3">
                        <CheckCircle className="h-5 w-5 text-green-500 mt-1 flex-shrink-0" />
                        <span className="text-base">{benefit}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </CardContent>
            </Card>
          </section>

          {/* How It Works Section */}
          <section className="container space-y-6 py-8 md:py-12 lg:py-24">
            <div className="mx-auto flex max-w-[58rem] flex-col items-center space-y-4 text-center">
              <h2 className="font-heading text-3xl leading-[1.1] sm:text-3xl md:text-6xl">
                How Quizora Works
              </h2>
              <p className="max-w-[85rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7">
                Get started in three simple steps
              </p>
            </div>
            <div className="mx-auto grid justify-center gap-4 sm:grid-cols-2 md:max-w-[64rem] md:grid-cols-3">
              <Card>
                <CardHeader className="text-center">
                  <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-blue-500 text-white">
                    <span className="text-2xl font-bold">1</span>
                  </div>
                  <CardTitle>Take Assessment</CardTitle>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-center">
                    Complete an initial assessment to help our AI understand
                    your current knowledge level
                  </CardDescription>
                </CardContent>
              </Card>

              <Card>
                <CardHeader className="text-center">
                  <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-purple-500 text-white">
                    <span className="text-2xl font-bold">2</span>
                  </div>
                  <CardTitle>Get Personalized Plan</CardTitle>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-center">
                    Receive a customized study plan with targeted mock exams and
                    learning materials
                  </CardDescription>
                </CardContent>
              </Card>

              <Card>
                <CardHeader className="text-center">
                  <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-green-500 text-white">
                    <span className="text-2xl font-bold">3</span>
                  </div>
                  <CardTitle>Track Progress</CardTitle>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-center">
                    Monitor your improvement with detailed analytics and
                    adaptive recommendations
                  </CardDescription>
                </CardContent>
              </Card>
            </div>
          </section>

          {/* Testimonials Section */}
          <section className="container py-8 md:py-12 lg:py-24">
            <Card className="border-0 bg-muted/50">
              <CardContent className="p-6 md:p-10">
                <div className="mx-auto flex max-w-[58rem] flex-col items-center space-y-4 text-center mb-8">
                  <h2 className="font-heading text-3xl leading-[1.1] sm:text-3xl md:text-6xl">
                    What Students Say
                  </h2>
                  <p className="text-xl text-muted-foreground">
                    Real success stories from our learning community
                  </p>
                </div>

                <div className="mx-auto grid justify-center gap-4 sm:grid-cols-2 md:max-w-[64rem] md:grid-cols-3">
                  <Card>
                    <CardContent className="pt-6">
                      <div className="flex mb-4">
                        {[...Array(5)].map((_, i) => (
                          <Star
                            key={i}
                            className="h-4 w-4 fill-yellow-400 text-yellow-400"
                          />
                        ))}
                      </div>
                      <p className="mb-4 text-sm">
                        "Quizora's AI-powered study suggestions helped me
                        improve my test scores by 30%. The adaptive learning
                        really works!"
                      </p>
                      <div className="flex items-center space-x-3">
                        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-blue-500 text-white">
                          <span className="text-sm font-semibold">SM</span>
                        </div>
                        <div>
                          <div className="text-sm font-semibold">
                            Sarah Martinez
                          </div>
                          <div className="text-xs text-muted-foreground">
                            Medical Student
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>

                  <Card>
                    <CardContent className="pt-6">
                      <div className="flex mb-4">
                        {[...Array(5)].map((_, i) => (
                          <Star
                            key={i}
                            className="h-4 w-4 fill-yellow-400 text-yellow-400"
                          />
                        ))}
                      </div>
                      <p className="mb-4 text-sm">
                        "The gamification features keep me motivated. I love
                        competing on the leaderboards with my classmates!"
                      </p>
                      <div className="flex items-center space-x-3">
                        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-green-500 text-white">
                          <span className="text-sm font-semibold">JD</span>
                        </div>
                        <div>
                          <div className="text-sm font-semibold">
                            James Davis
                          </div>
                          <div className="text-xs text-muted-foreground">
                            Engineering Student
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>

                  <Card>
                    <CardContent className="pt-6">
                      <div className="flex mb-4">
                        {[...Array(5)].map((_, i) => (
                          <Star
                            key={i}
                            className="h-4 w-4 fill-yellow-400 text-yellow-400"
                          />
                        ))}
                      </div>
                      <p className="mb-4 text-sm">
                        "The community marketplace is amazing. I can access
                        practice exams from students worldwide!"
                      </p>
                      <div className="flex items-center space-x-3">
                        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-purple-500 text-white">
                          <span className="text-sm font-semibold">AL</span>
                        </div>
                        <div>
                          <div className="text-sm font-semibold">Anna Lee</div>
                          <div className="text-xs text-muted-foreground">
                            Law Student
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </div>
              </CardContent>
            </Card>
          </section>

          {/* CTA Section */}
          <section className="container space-y-6 py-8 md:py-12 lg:py-24">
            <div className="mx-auto flex max-w-[58rem] flex-col items-center space-y-4 text-center">
              <h2 className="font-heading text-3xl leading-[1.1] sm:text-3xl md:text-6xl">
                Ready to Transform Your Learning?
              </h2>
              <p className="max-w-[85rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7">
                Join thousands of students who are already studying smarter with
                Quizora's AI-powered platform
              </p>
              <div className="flex flex-col gap-4 sm:flex-row">
                <Button size="lg" className="h-11 px-8">
                  <Zap className="mr-2 h-4 w-4" />
                  Get Started Free
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Button>
                <Button variant="outline" size="lg" className="h-11 px-8">
                  <Globe className="mr-2 h-4 w-4" />
                  View Demo
                </Button>
              </div>
            </div>
          </section>
        </main>
        <Footer />
      </div>
    </>
  );
}

export default Home;

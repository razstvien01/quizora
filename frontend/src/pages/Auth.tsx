"use client";

import LoginForm from "@/components/auth/login-form";
import RegisterForm from "@/components/auth/register-form";
import { useState } from "react";
import { Helmet } from "react-helmet-async";

function Auth() {
  const [isLogin, setIsLogin] = useState(true);

  return (
    <>
      <Helmet>
        <title>{isLogin ? "Sign In" : "Sign Up"} | Quizora</title>
        <meta
          name="description"
          content={
            isLogin
              ? "Sign in to your Quizora account to continue your learning journey"
              : "Create your free Quizora account and start studying smarter today"
          }
        />
      </Helmet>

      <div className="flex items-center justify-center bg-gradient-to-br p-4">
        <div className="w-full max-w-md">
          {isLogin ? (
            <LoginForm onSwitchToRegister={() => setIsLogin(false)} />
          ) : (
            <RegisterForm onSwitchToLogin={() => setIsLogin(true)} />
          )}
        </div>

        {/* Background decoration */}
        <div className="fixed inset-0 -z-10 overflow-hidden">
          <div className="absolute -top-40 -right-32 w-80 h-80 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob"></div>
          <div className="absolute -bottom-40 -left-32 w-80 h-80 bg-blue-300 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-2000"></div>
          <div className="absolute top-40 left-40 w-80 h-80 bg-pink-300 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-4000"></div>
        </div>
      </div>
    </>
  );
}

export default Auth;

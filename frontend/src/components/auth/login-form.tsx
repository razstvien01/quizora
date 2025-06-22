"use client";

import type React from "react";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Checkbox } from "@/components/ui/checkbox";
import { Separator } from "@/components/ui/separator";
import { Badge } from "@/components/ui/badge";
import {
  Eye,
  EyeOff,
  Mail,
  Lock,
  GraduationCap,
  Github,
  Chrome,
  ArrowRight,
} from "lucide-react";

interface LoginFormProps {
  onSwitchToRegister: () => void;
}

export default function LoginForm({ onSwitchToRegister }: LoginFormProps) {
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    rememberMe: false,
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isLoading, setIsLoading] = useState(false);

  const handleInputChange = (field: string, value: string | boolean) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
    // Clear error when user starts typing
    if (errors[field]) {
      setErrors((prev) => ({ ...prev, [field]: "" }));
    }
  };

  const validateForm = () => {
    const newErrors: Record<string, string> = {};

    if (!formData.email.trim()) {
      newErrors.email = "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = "Please enter a valid email";
    }
    if (!formData.password) {
      newErrors.password = "Password is required";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!validateForm()) return;

    setIsLoading(true);
    // Simulate API call
    await new Promise((resolve) => setTimeout(resolve, 2000));
    setIsLoading(false);

    // Handle successful login here
    console.log("Login successful:", formData);
  };

  const handleSocialLogin = (provider: string) => {
    console.log(`Login with ${provider}`);
  };

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader className="space-y-1 text-center">
        <div className="flex items-center justify-center mb-4">
          <div className="flex items-center space-x-2">
            <GraduationCap className="h-8 w-8 text-primary" />
            <span className="text-2xl font-bold">Quizora</span>
          </div>
        </div>
        <CardTitle className="text-2xl">Welcome back</CardTitle>
        <CardDescription>
          Sign in to your account to continue your learning journey
        </CardDescription>
        <Badge variant="secondary" className="mx-auto">
          🚀 Ready to ace your exams?
        </Badge>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Social Login */}
        <div className="grid grid-cols-2 gap-4">
          <Button
            variant="outline"
            onClick={() => handleSocialLogin("Google")}
            className="w-full"
          >
            <Chrome className="mr-2 h-4 w-4" />
            Google
          </Button>
          <Button
            variant="outline"
            onClick={() => handleSocialLogin("GitHub")}
            className="w-full"
          >
            <Github className="mr-2 h-4 w-4" />
            GitHub
          </Button>
        </div>

        <div className="relative">
          <div className="absolute inset-0 flex items-center">
            <Separator className="w-full" />
          </div>
          <div className="relative flex justify-center text-xs uppercase">
            <span className="bg-background px-2 text-muted-foreground">
              Or continue with email
            </span>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          {/* Email */}
          <div className="space-y-2">
            <Label htmlFor="email">Email</Label>
            <div className="relative">
              <Mail className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
              <Input
                id="email"
                type="email"
                placeholder="john@example.com"
                value={formData.email}
                onChange={(e) => handleInputChange("email", e.target.value)}
                className={`pl-10 ${errors.email ? "border-red-500" : ""}`}
              />
            </div>
            {errors.email && (
              <p className="text-sm text-red-500">{errors.email}</p>
            )}
          </div>

          {/* Password */}
          <div className="space-y-2">
            <div className="flex items-center justify-between">
              <Label htmlFor="password">Password</Label>
              <button
                type="button"
                className="text-sm text-primary hover:underline"
                onClick={() => console.log("Forgot password")}
              >
                Forgot password?
              </button>
            </div>
            <div className="relative">
              <Lock className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
              <Input
                id="password"
                type={showPassword ? "text" : "password"}
                placeholder="••••••••"
                value={formData.password}
                onChange={(e) => handleInputChange("password", e.target.value)}
                className={`pl-10 pr-10 ${
                  errors.password ? "border-red-500" : ""
                }`}
              />
              <Button
                type="button"
                variant="ghost"
                size="sm"
                className="absolute right-0 top-0 h-full px-3 py-2 hover:bg-transparent"
                onClick={() => setShowPassword(!showPassword)}
              >
                {showPassword ? (
                  <EyeOff className="h-4 w-4 text-muted-foreground" />
                ) : (
                  <Eye className="h-4 w-4 text-muted-foreground" />
                )}
              </Button>
            </div>
            {errors.password && (
              <p className="text-sm text-red-500">{errors.password}</p>
            )}
          </div>

          {/* Remember Me */}
          <div className="flex items-center space-x-2">
            <Checkbox
              id="remember"
              checked={formData.rememberMe}
              onCheckedChange={(checked) =>
                handleInputChange("rememberMe", checked as boolean)
              }
            />
            <Label
              htmlFor="remember"
              className="text-sm leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
            >
              Remember me for 30 days
            </Label>
          </div>

          <Button type="submit" className="w-full" disabled={isLoading}>
            {isLoading ? (
              "Signing in..."
            ) : (
              <>
                Sign in
                <ArrowRight className="ml-2 h-4 w-4" />
              </>
            )}
          </Button>
        </form>

        <div className="text-center text-sm">
          Don't have an account?{" "}
          <button
            onClick={onSwitchToRegister}
            className="underline hover:text-primary font-medium"
          >
            Sign up for free
          </button>
        </div>

        {/* Demo Account */}
        <div className="pt-4 border-t">
          <div className="text-center">
            <p className="text-sm text-muted-foreground mb-2">
              Try Quizora with a demo account
            </p>
            <Button
              variant="outline"
              size="sm"
              onClick={() => {
                setFormData({
                  email: "demo@quizora.com",
                  password: "demo123456",
                  rememberMe: false,
                });
              }}
            >
              Use Demo Account
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

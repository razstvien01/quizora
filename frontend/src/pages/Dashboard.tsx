import { Button } from "@/components/ui/button";
import { useAuthRedirect } from "@/hooks/useAuthRedirect";
import { useAuthActions } from "@/lib/auth";

function Dashboard() {
  useAuthRedirect({ requireAuth: true });

  const { user, handleLogout } = useAuthActions();

  return (
    <div className="p-8">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Welcome, {user?.name}!</h1>
        <Button onClick={() => handleLogout()}>Logout</Button>
      </div>
      <p className="mt-4">This is your Quizora dashboard. 🎓</p>
    </div>
  );
}

export default Dashboard;

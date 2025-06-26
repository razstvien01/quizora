import { useAuthRedirect } from "@/hooks/useAuthRedirect";
import { useAuth0 } from "@auth0/auth0-react";

function Dashboard() {
  useAuthRedirect({ requireAuth: true });

  const { user } = useAuth0();

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold">Welcome, {user?.name}!</h1>
      <p className="mt-4">This is your Quizora dashboard. 🎓</p>
    </div>
  );
}

export default Dashboard;

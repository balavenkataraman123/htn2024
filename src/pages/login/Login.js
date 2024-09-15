import "./Login.css";
import { LoginForm } from "../../components";
import { useAuth } from "../../hooks/useAuth";
import { Navigate } from "react-router-dom";

const Login = () => {
  const [user, loading] = useAuth();

  if (user) {
   return <Navigate to="/" />;
  }

  return (
    <div className="login">
      <h1>Login</h1>
      <LoginForm />
    </div>
  );
};

export default Login;

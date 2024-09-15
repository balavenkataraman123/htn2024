import "./Login.css";
import { LoginForm } from "../../components";
import useAuth from "../../hooks/useAuth";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const user = useAuth();
  const navigate = useNavigate();

  if (user) {
    navigate("/");
  }
  
  return (
    <div className="login">
      <h1>Login</h1>
      <LoginForm />
    </div>
  );
};

export default Login;

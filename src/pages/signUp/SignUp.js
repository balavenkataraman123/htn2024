import "./SignUp.css";
import { SignUpForm } from "../../components";
import { useAuth } from "../../hooks/useAuth";
import { Navigate } from "react-router-dom";

const SignUp = () => {
  const [user, loading] = useAuth();

  if (user) {
    return <Navigate to="/" />;
  }

  return (
    <div className="sign-up">
      <SignUpForm />
    </div>
  );
};

export default SignUp;

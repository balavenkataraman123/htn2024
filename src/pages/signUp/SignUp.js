import "./SignUp.css";
import { SignUpForm } from "../../components";
import { useAuth } from "../../hooks/useAuth";
import { useNavigate } from "react-router-dom";

const SignUp = () => {
  const user = useAuth();
  const navigate = useNavigate();

  if (user) {
    navigate("/");
  }
  
  return (
    <div className="sign-up">
      <SignUpForm />
    </div>
  );
};

export default SignUp;

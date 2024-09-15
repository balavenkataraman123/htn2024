import React from "react";
import { useAuth } from "../../hooks/useAuth";
import { logout } from "../../firebase/auth";
import "./Profile.css";
import { Navigate } from "react-router-dom";

function Profile() {
  const user = useAuth();

  const handleLogout = async () => {
    try {
      await logout();
      console.log("User signed out!");
    } catch (error) {
      console.error("Error signing out:", error);
    }
  };

  if (!user) return <Navigate to="/landing" />

  return (
    <div>
      <h2>Welcome, {user.email}</h2>
      <button onClick={handleLogout}>Log Out</button>
    </div>
  );
}

export default Profile;

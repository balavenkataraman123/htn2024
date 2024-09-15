import React from "react";
import { useAuth } from "../../hooks/useAuth";
import { logout } from "../../firebase/auth";
import "./Profile.css";

function Profile() {
  const [user, loading] = useAuth();

  const handleLogout = async () => {
    try {
      await logout();
      console.log("User signed out!");
    } catch (error) {
      console.error("Error signing out:", error);
    }
  };

  if (loading) return <p>Loading...</p>;

  if (!user) return <p>You are logged out. Please <a href="/login">log in</a></p>;

  return (
    <div>
      <h2>Welcome, {user.email}</h2>
      <button onClick={handleLogout}>Log Out</button>
    </div>
  );
}

export default Profile;

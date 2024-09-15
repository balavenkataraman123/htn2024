import app from "./firebaseConfig";
import { getAuth } from "firebase/auth";

import {
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signOut,
} from "firebase/auth";

// Get the auth object from the firebase app
const auth = getAuth(app);

// Log-in function
export const login = (email, password) => {
  return signInWithEmailAndPassword(auth, email, password);
};

// Sign-up function
export const register = (email, password) => {
  return createUserWithEmailAndPassword(auth, email, password);
};

// Log-out function
export const logout = () => {
  return signOut(auth);
};

export { auth };

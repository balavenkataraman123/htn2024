// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyBKbb7_qXjY1REwNWgz0wFaVJFXwCxYIAE",
  authDomain: "ted-talks-htn.firebaseapp.com",
  projectId: "ted-talks-htn",
  storageBucket: "ted-talks-htn.appspot.com",
  messagingSenderId: "719826206123",
  appId: "1:719826206123:web:7158858d5bdf74206c66ee",
  measurementId: "G-HF70405RWD"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export default app;
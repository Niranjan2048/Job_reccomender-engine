document.querySelector('.img-btn').addEventListener('click', function()
	{
		document.querySelector('.cont').classList.toggle('s-signup')
	}
);
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCymQui1BmSZlUQcbz5EJzMzFVZB0CtUtk",
  authDomain: "job-recommender-d701e.firebaseapp.com",
  databaseURL: "https://job-recommender-d701e-default-rtdb.firebaseio.com",
  projectId: "job-recommender-d701e",
  storageBucket: "job-recommender-d701e.appspot.com",
  messagingSenderId: "836570295145",
  appId: "1:836570295145:web:2595205b74a38dd405ebf8",
  measurementId: "G-7JC5V4D8YD"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

var provider = new firebase.auth.GoogleAuthProvider();

firebase.auth().signInWithPopup(provider).then(function(result) {
	// This gives you a Google Access Token. You can use it to access the Google API.
	var token = result.credential.accessToken;
	// The signed-in user info.
	var user = result.user;
	// ...
  }).catch(function(error) {
	// Handle Errors here.
	var errorCode = error.code;
	var errorMessage = error.message;
	// The email of the user's account used.
	var email = error.email;
	// The firebase.auth.AuthCredential type that was used.
	var credential = error.credential;
	// ...
  });

  firebase.auth().signOut().then(function() {
	// Sign-out successful.
  }).catch(function(error) {
	// An error happened.
  });
import { initializeApp } from 'firebase/app';
import { getFirestore, connectFirestoreEmulator } from 'firebase/firestore';
import { getAuth, connectAuthEmulator } from 'firebase/auth';

// App's Firebase configuration
const firebaseConfig = {
    apiKey: '',
    authDomain: '',
    databaseURL: '',
    projectId: '',
    storageBucket: '',
    messagingSenderId: '',
    appId: ''
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore and connect to Firestore emulator for local testing (remove in production)
const db = getFirestore();
connectFirestoreEmulator(db, 'localhost', 8080);

// Initialize Authentication and connect to the Authentication emulator for local testing (remove in production)
const auth = getAuth();
connectAuthEmulator(auth, 'http://localhost:9099');

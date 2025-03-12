import express from 'express';
import cors from 'cors';
import universitiesRoutes from './routes/universities.routes';  // Import the universities routes

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Use the universities routes
app.use('/api', universitiesRoutes);

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
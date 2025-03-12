import pgPromise from 'pg-promise';
import dotenv from 'dotenv';

// Load environment variables from the .env file
dotenv.config();

// Initialize pg-promise
const pgp = pgPromise();

// Create the database connection URL using environment variables
const db = pgp({
  host: process.env.DB_HOST,
  port: Number(process.env.DB_PORT),
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
});

// Export the database connection
export default db;
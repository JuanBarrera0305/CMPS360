import { Request, Response } from 'express';  // Import Express types
import db from '../config/db';  // Import the database connection

// Define the getUniversities function with correct typing
export const getUniversities = async (req: Request, res: Response): Promise<void> => {
  try {
    // Replace the dummy data with a database call
    const data = await db.any('SELECT * FROM universities');
    res.status(200).json(data);  // Return the data as a JSON response
  } catch (error: any) {
    res.status(500).json({ message: 'Error fetching universities', error: error.message });
  }
};

import { Router } from 'express';
import { getUniversities } from '../controllers/universities.controller';

const router = Router();

// GET /api/universities
router.get('/universities', getUniversities);

export default router;

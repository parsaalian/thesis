import { getQuizQuestionAPI } from '~/services/question';

export const GENERATE_QUIZ_QUESTIONS = 'GENERATE_QUIZ_QUESTIONS';

export function generateQuizQuestionsAction() {
    return {
        type: GENERATE_QUIZ_QUESTIONS,
    }
}
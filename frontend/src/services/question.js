import axios from 'axios';
import BASE_ADDR from '.';

const QUESTION_PRACTICE = `${BASE_ADDR}/question/practice`;
const QUESTION_QUIZ = `${BASE_ADDR}/question/quiz`;

export function getPracticeQuestionAPI() {
    return axios.get(QUESTION_PRACTICE);
}

export function getQuizQuestionAPI() {
    return axios.get(QUESTION_QUIZ);
}
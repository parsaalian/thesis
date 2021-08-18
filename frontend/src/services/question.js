import axios from 'axios';
import BASE_ADDR from '.';

const QUESTION_PRACTICE = `${BASE_ADDR}/quiz/practice`;
const QUESTION_QUIZ = `${BASE_ADDR}/quiz/question`;

export function getPracticeQuestionAPI(token) {
    return axios.get(QUESTION_PRACTICE, {
        headers: {
            Authorization: `Bearer ${token}`,
        }
    });
}

export function getQuizQuestionAPI(token) {
    return axios.get(QUESTION_QUIZ);
}
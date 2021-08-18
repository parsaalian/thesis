import LoginPage from './Login';
import QuestionPage from './Question';

const routes = [{
        path: '/',
        component: LoginPage,
    },
    {
        path: '/question',
        component: QuestionPage,
    }
]

export default routes;
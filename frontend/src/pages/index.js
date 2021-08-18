import LoginPage from './Login';
import PracticePage from './Practice';
import QuestionPage from './Question';

const routes = [{
        path: '/',
        component: LoginPage,
    },
    {
        path: '/practice',
        component: PracticePage,
    },
    {
        path: '/question',
        component: QuestionPage,
    }
]

export default routes;
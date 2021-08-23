import LoginPage from './Login';
import DashboardPage from './Dashboard';
import PracticePage from './Practice';
import QuestionPage from './Question';

const routes = [{
        path: '/',
        component: LoginPage,
    },
    {
        path: '/dashboard',
        component: DashboardPage,
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
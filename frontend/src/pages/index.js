import LoginPage from './Login';
import DashboardPage from './Dashboard';
import DashboardCoursesPage from './Dashboard/Courses';
import DashboardGamesPage from './Dashboard/Games';
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
        path: '/dashboard/courses',
        component: DashboardCoursesPage
    },
    {
        path: '/dashboard/games',
        component: DashboardGamesPage
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
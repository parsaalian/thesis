import DashboardSideNav from '../../../components/composite/DashbordSideNav';
import { faBookmark, faHome, faUniversity, faDiceFive, faTrophy } from '@fortawesome/free-solid-svg-icons';

const links = [
    {
        href: 'dashboard',
        text: 'Home',
        icon: faHome,
        key: 'Home'
    },
    {
        href: 'dashboard/courses',
        text: 'Courses',
        icon: faUniversity,
        key: 'Courses'
    },
    {
        href: 'dashboard/games',
        text: 'Games',
        icon: faDiceFive,
        key: 'Games'
    },
    {
        href: 'dashboard/bookmarks',
        text: 'Bookmarks',
        icon: faBookmark,
        key: 'Bookmarks'
    },
    {
        href: 'dashboard/leaderboard',
        text: 'Leaderboard',
        icon: faTrophy,
        key: 'Leaderboard'
    }
]

function NavLinks({ selected }) {
    return <DashboardSideNav selected={selected} links={links}></DashboardSideNav>;
}

export default NavLinks;
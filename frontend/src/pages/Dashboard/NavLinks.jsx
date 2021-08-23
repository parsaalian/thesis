import DashboardSideNav from '../../components/composite/DashbordSideNav';
import { faHome, faUniversity } from '@fortawesome/free-solid-svg-icons';

const links = [
    {
        href: 'dashboard',
        text: 'Home',
        icon: faHome
    },
    {
        href: 'dashboard/courses',
        text: 'Courses',
        icon: faUniversity,
    }
]

function NavLinks({ selected }) {
    return <DashboardSideNav selected={selected} links={links}></DashboardSideNav>;
}

export default NavLinks;
import React from 'react';
import Nav from 'react-bootstrap/Nav';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import DashboardSideNavLink from '../../simple/DashboardSideNav/Link';
import DashboardSideNavContainer from '../../simple/DashboardSideNav/Container';


function DashboardSideNav({ links, selected }) {
    return (
        <DashboardSideNavContainer>
            <Nav defaultActiveKey={selected} variant="pills" className="flex-column">
                {links.map((link) => {
                    return (
                        <DashboardSideNavLink key={link.href} eventKey={link.href} href={link.href}>
                            <FontAwesomeIcon icon={link.icon} /> &nbsp;&nbsp;&nbsp; {link.text}
                        </DashboardSideNavLink>
                    )
                })}
            </Nav>
        </DashboardSideNavContainer>
    )
}

export default DashboardSideNav;
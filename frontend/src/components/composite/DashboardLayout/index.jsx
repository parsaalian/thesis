import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import DashboardTopNav from '../DashboardTopNav';
import DashboardNavLinks from '../DashboardNavLinks';


function DashboardLayout({ children, page }) {
    return (
        <Container fluid>
            <Row>
                <Col md={3} lg={2} style={{ padding: 0 }}>
                    <DashboardNavLinks selected={page} />
                </Col>
                <Col md={9} lg={10}>
                    <DashboardTopNav page={page} />
                    <Container fluid>
                        {children}
                    </Container>
                </Col>
            </Row>
        </Container>
    )
}

export default DashboardLayout;
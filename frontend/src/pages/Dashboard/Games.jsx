import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import DashboardLayout from '../../components/composite/DashboardLayout';

class DashboardGamesPage extends Component {
    render() {
        return (
            <DashboardLayout page="Games">
                <h5>Play Games</h5>
                <Container>
                    <Row className="py-4">
                        <Col md={3} lg={3}>
                            <Card className="text-center" style={{ boxShadow: '0px 1px 21px 0px rgba(0,0,0,0.3)' }}>
                                <Card.Img src="/assets/images/trend.webp" />
                                <Card.Body>
                                    <Card.Title>Trend Analysis</Card.Title>
                                </Card.Body>
                            </Card>
                        </Col>
                    </Row>
                </Container>
            </DashboardLayout>
        );
    }
}

export default DashboardGamesPage;
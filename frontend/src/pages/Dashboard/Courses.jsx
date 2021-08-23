import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import DashboardLayout from '../../components/composite/DashboardLayout';

class DashboardCoursesPage extends Component {
    render() {
        return (
            <DashboardLayout page="Courses">
                <h5>Learn Patterns</h5>
                <Container>
                    <Row className="py-4">
                        <Col md={3} lg={3}>
                            <Card className="text-center" style={{ boxShadow: '0px 1px 21px 0px rgba(0,0,0,0.3)' }}>
                                <Card.Img src="/assets/images/candlestick.jpeg" />
                                <Card.Body>
                                    <Card.Title>Candlestick Patterns</Card.Title>
                                </Card.Body>
                            </Card>
                        </Col>
                        <Col md={3} lg={3}>
                            <Card className="text-center" style={{ boxShadow: '0px 1px 21px 0px rgba(0,0,0,0.3)' }}>
                                <Card.Img src="/assets/images/chart.jpeg" />
                                <Card.Body>
                                    <Card.Title>Chart Patterns</Card.Title>
                                </Card.Body>
                            </Card>
                        </Col>
                        <Col md={3} lg={3}>
                            <Card className="text-center" style={{ boxShadow: '0px 1px 21px 0px rgba(0,0,0,0.3)' }}>
                                <Card.Img src="/assets/images/indicators.jpeg" />
                                <Card.Body>
                                    <Card.Title>Indicators</Card.Title>
                                </Card.Body>
                            </Card>
                        </Col>
                    </Row>
                </Container>
            </DashboardLayout>
        );
    }
}

export default DashboardCoursesPage;
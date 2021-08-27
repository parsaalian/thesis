import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Table from 'react-bootstrap/Table';
import DashboardLayout from '../../components/composite/DashboardLayout';
import { uniqueNamesGenerator, names } from 'unique-names-generator';

const config = {
  dictionaries: [names]
}

class DashboardLeaderboardPage extends Component {
    render() {
        let rows = [];
        for (let i = 0; i < 20; i++) {
            rows = [...rows, {
                name: uniqueNamesGenerator(config),
                point: Math.round(Math.random() * 10000)
            }]
        }

        rows = rows.sort((a, b) => (a.point > b.point) ? -1 : ((b.point > a.point) ? 1 : 0));

        return (
            <DashboardLayout page="Leaderboard">
                <Container>
                    <Row className="py-4">
                        
                    </Row>
                    <Row>
                        <Table responsive>
                            <tbody>
                                {rows.map((row, i) => {
                                    return (
                                        <tr>
                                            <td>{i + 1}</td>
                                            <td>{row.name}</td>
                                            <td>{row.point}</td>
                                        </tr>
                                    )
                                })}
                            </tbody>
                        </Table>
                    </Row>
                </Container>
            </DashboardLayout>
        );
    }
}

export default DashboardLeaderboardPage;
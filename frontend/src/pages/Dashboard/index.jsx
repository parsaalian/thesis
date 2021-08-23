import React, { Component } from 'react';
import DashboardLayout from '../../components/composite/DashboardLayout';
import NavLinks from './NavLinks';

class DashboardPage extends Component {
    render() {
        return (
            <DashboardLayout
                navbar={<NavLinks selected="/dashboard" />}
            >
                hey
            </DashboardLayout>
        );
    }
}

export default DashboardPage;
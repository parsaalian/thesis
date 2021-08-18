import { isEmpty } from 'lodash';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import QuestionLayout from '../../components/composite/QuestionLayout';
import { historyToCandlestick } from '../../utils/question';
import Chart, { defaultOptions } from '../../containers/TradingViewChart';
import { getPracticeQuestionAPI } from '../../services/question';

class PracticePage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            question: {}
        }
    }

    componentDidMount() {
        const { access } = this.props;
        getPracticeQuestionAPI(access).then(
            (response) => {
                const { data: question } = response;
                this.setState({
                    question
                });
            }
        );
    }

    render() {
        const { question } = this.state;
        if (isEmpty(question)) {
            return <></>;
        }
        const { history } = question;
        const candlestickSeries = historyToCandlestick(history);
        console.log(question);
        return (
            <QuestionLayout>
                <Chart
                    options={defaultOptions}
                    candlestickSeries={candlestickSeries}
                    height={640}
                />
            </QuestionLayout>
        );
    }
}

function mapStateToProps(state) {
    const { access } = state.account;
    return {
        access,
    }
}

export default connect(mapStateToProps, null)(PracticePage);
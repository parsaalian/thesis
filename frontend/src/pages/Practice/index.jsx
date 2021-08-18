import { isEmpty } from 'lodash';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import QuestionLayout from '../../components/composite/QuestionLayout';
import Question from '../../components/composite/Question';
import ArticleTabs from '../../components/composite/ArticleTabs';
import Chart, { defaultOptions } from '../../containers/TradingViewChart';
import { historyToCandlestick } from '../../utils/question';
import { getPracticeQuestionAPI } from '../../services/question';

class PracticePage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            practice: {},
            showArticles: false,
        }
        this.answerQuestion = this.answerQuestion.bind(this);
    }

    componentDidMount() {
        const { access } = this.props;
        getPracticeQuestionAPI(access).then(
            (response) => {
                const { data: practice } = response;
                this.setState({
                    practice
                });
            }
        );
    }

    answerQuestion(choice) {
        // submitAnswerToServer(choice)
        this.setState({
            showArticles: true,
        });
    }

    render() {
        const { practice, showArticles } = this.state;
        if (isEmpty(practice)) {
            return <></>;
        }
        const { history, question, articles } = practice;
        const candlestickSeries = historyToCandlestick(history);
        return (
            <QuestionLayout>
                <Chart
                    options={defaultOptions}
                    candlestickSeries={candlestickSeries}
                    height={640}
                />
                <Question question={question} onAnswer={this.answerQuestion} />
                {
                    showArticles && articles.length > 0 && <ArticleTabs articles={articles} />
                }
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
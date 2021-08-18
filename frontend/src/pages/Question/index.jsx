import React, { Component } from 'react';
import QuestionLayout from '../../components/composite/QuestionLayout';
import Chart from '../../containers/TradingViewChart';
import ArticleTabs from '../../components/composite/ArticleTabs';
import { getQuizQuestionAPI } from '../../services/question';


function quizResponseToCandlestick(response) {
    return response.map((entry) => ({
        time: entry.date,
        high: entry.max_price,
        low: entry.min_price,
        open: entry.first_price,
        close: entry.last_price
    }));
}


class QuestionPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            articles: {},
            candlestickSeries: [],
        }
    }

    componentDidMount() {
        getQuizQuestionAPI().then((res) => {
            console.log(res.data)
            const candlestick = quizResponseToCandlestick(res.data.history);
            this.setState({
                candlestickSeries: [{
                    data: candlestick
                }],
                articles: res.data.articles,
            })
        });
    }

    render() {
        const { articles, candlestickSeries } = this.state;
        if (candlestickSeries.length === 0) {
            return <></>
        }
        return (
            <QuestionLayout>
                <Chart
                    options={{
                        alignLabels: true,
                        timeScale: {
                            rightOffset: 12,
                            barSpacing: 3,
                            fixLeftEdge: true,
                            fixRightEdge: true,
                            lockVisibleTimeRangeOnResize: true,
                            rightBarStaysOnScroll: true,
                            borderVisible: false,
                            borderColor: "#fff000",
                            visible: true,
                            timeVisible: true,
                            secondsVisible: false,
                            autoScale: true,
                        }
                    }}
                    candlestickSeries={candlestickSeries}
                    height={640}
                />
                {
                    articles.length > 0 && <ArticleTabs articles={articles} />
                }
                
            </QuestionLayout>
        );
    }
}

export default QuestionPage;
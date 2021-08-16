import React, { Component } from 'react';
import MDX from '@mdx-js/runtime'
import Chart from '../../containers/TradingViewChart';
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


const components = {
    img: (props) => <img width="100%" {...props} />
}


class QuestionPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            article: {},
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
                article: res.data.articles[0],
            })
        });
    }

    render() {
        const { article, candlestickSeries } = this.state;
        if (candlestickSeries.length === 0) {
            return <></>
        }
        return (
            <>
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
                    article !== undefined  && (
                        <>
                            <a href={article.href} target="_blank" rel="noreferrer">{article.title}</a>
                            <MDX components={components} children={article.body} />
                        </>
                    )
                }
                
            </>
        );
    }
}

export default QuestionPage;
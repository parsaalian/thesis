import axios from 'axios';
import React, { Component } from 'react';
import Chart from '../../containers/TradingViewChart';

class QuestionPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            candlestickSeries: [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/quiz/question').then(
            (response) => {
                console.log(response)
                this.setState({
                    candlestickSeries: [{
                        data:response.data.history.map((row) => ({
                            time: row.date,
                            open: row.first_price,
                            close: row.last_price,
                            low: row.min_price,
                            high: row.max_price,
                            }
                        ))
                    }]
                });
            }
        )
    }

    render() {
        console.log(this.state.candlestickSeries);
        if (this.state.candlestickSeries.length === 0) {
            return <></>;
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
                    candlestickSeries={this.state.candlestickSeries}
                    height={320}
                ></Chart>
            </>
        );
    }
}

export default QuestionPage;
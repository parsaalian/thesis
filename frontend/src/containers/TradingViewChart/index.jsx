// adapted from https://github.com/Kaktana/kaktana-react-lightweight-charts/blob/master/src/kaktana-react-lightweight-charts.js
import React, { Component } from 'react';
import { createChart } from 'lightweight-charts';
import { mergeDeepLeft } from 'ramda';

const addSeriesFunctions = {
    candlestick: "addCandlestickSeries",
    line: "addLineSeries",
    area: "addAreaSeries",
    bar: "addBarSeries",
    histogram: "addHistogramSeries",
};

const colors = [
    "#008FFB",
    "#00E396",
    "#FEB019",
    "#FF4560",
    "#775DD0",
    "#F86624",
    "#A5978B",
];

const darkTheme = {
    layout: {
        backgroundColor: "#131722",
        lineColor: "#2B2B43",
        textColor: "#D9D9D9",
    },
    grid: {
        vertLines: {
            color: "#363c4e",
        },
        horzLines: {
            color: "#363c4e",
        },
    },
};

const lightTheme = {
    layout: {
        backgroundColor: "#FFFFFF",
        lineColor: "#2B2B43",
        textColor: "#191919",
    },
    grid: {
        vertLines: {
            color: "#e1ecf2",
        },
        horzLines: {
            color: "#e1ecf2",
        },
    },
};

class TradingViewChart extends Component {
    constructor(props) {
        super(props);
        this.chartDivRef = React.createRef();
        this.chart = null;
        this.series = [];

        this.addSeries = this.addSeries.bind(this);
    }

    componentDidMount() {
        this.chart = createChart(this.chartDivRef.current);
        this.handleUpdateChart();
    }

    removeSeries = () => {
        this.series.forEach((serie) => this.chart.removeSeries(serie));
        this.series = [];
    };

    addSeries(newSeries, type) {
        const addFunction = addSeriesFunctions[type];
        let color =
            (newSeries.options && newSeries.options.color) ||
            colors[this.series.length % colors.length];
        const series = this.chart[addFunction]({
            color,
            ...newSeries.options,
        });
        let data = this.handleLinearInterpolation(
            newSeries.data,
            newSeries.linearInterpolation
        );
        series.setData(data);
        if (newSeries.markers) {
            series.setMarkers(newSeries.markers);
        }
        if (newSeries.priceLines) {
            newSeries.priceLines.forEach((line) => series.createPriceLine(line));
        }
        return series;
    }

    handleSeries = () => {
        let series = this.series;
        let props = this.props;
        props.candlestickSeries &&
            props.candlestickSeries.forEach((serie) => {
                series.push(this.addSeries(serie, "candlestick"));
            });

        props.lineSeries &&
            props.lineSeries.forEach((serie) => {
                series.push(this.addSeries(serie, "line"));
            });

        props.areaSeries &&
            props.areaSeries.forEach((serie) => {
                series.push(this.addSeries(serie, "area"));
            });

        props.barSeries &&
            props.barSeries.forEach((serie) => {
                series.push(this.addSeries(serie, "bar"));
            });

        props.histogramSeries &&
            props.histogramSeries.forEach((serie) => {
                series.push(this.addSeries(serie, "histogram"));
            });
    };

    handleLinearInterpolation = (data, candleTime) => {
        if (!candleTime || data.length < 2 || !data[0].value) return data;
        let first = data[0].time;
        let last = data[data.length - 1].time;
        let newData = new Array(Math.floor((last - first) / candleTime));
        newData[0] = data[0];
        let index = 1;
        for (let i = 1; i < data.length; i++) {
            newData[index++] = data[i];
            let prevTime = data[i - 1].time;
            let prevValue = data[i - 1].value;
            let { time, value } = data[i];
            for (
                let interTime = prevTime;
                interTime < time - candleTime;
                interTime += candleTime
            ) {
                // interValue get from the Taylor-Young formula
                let interValue =
                    prevValue +
                    (interTime - prevTime) *
                        ((value - prevValue) / (time - prevTime));
                newData[index++] = { time: interTime, value: interValue };
            }
        }
        // return only the valid values
        return newData.filter((x) => x);
    };

    handleUpdateChart = () => {
        let { chart, chartDiv } = this;
        let props = this.props;
        let options = this.props.darkTheme ? darkTheme : lightTheme;
        options = mergeDeepLeft(options, {
            width: props.autoWidth
                ? chartDiv.current.parentNode.clientWidth
                : props.width,
            height: props.autoHeight
                ? chartDiv.current.parentNode.clientHeight
                : props.height || 500,
            ...props.options,
        });
        chart.applyOptions(options);

        this.handleSeries();

        this.chart.timeScale().fitContent();
    };

    render() {
        return (
            <div ref={this.chartDivRef}></div>
        )
    }
}

export const defaultOptions = require('./defaultOptions').default;

export default TradingViewChart;
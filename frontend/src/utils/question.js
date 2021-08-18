export function historyToCandlestick(history) {
    return [{
        data: history.map((entry) => ({
            time: entry.date,
            high: entry.max_price,
            low: entry.min_price,
            open: entry.first_price,
            close: entry.last_price
        }))
    }];
}
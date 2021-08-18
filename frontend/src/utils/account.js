export function requestOrRefresh(
    requestFunction,
    refreshFunction,
    successCallback,
    errorCallback,
    redirectToLogin,
) {
    requestFunction().then(
        (response) => successCallback(response),
        (error) => {
            if (error.code === 'token_not_valid') {
                refreshFunction().then(
                    () => requestFunction().then(
                        (response) => successCallback(response),
                        (error) => errorCallback(error),
                    ),
                    () => redirectToLogin(),
                )
            } else {
                errorCallback(error);
            }
        }
    )
}
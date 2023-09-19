const clearAlertAfterSpecifiedTime = (alertInstance, timeInSeconds = 5) => {
    setInterval(() => {
        alertInstance.clear();
    }, timeInSeconds * 1000);
}

export default clearAlertAfterSpecifiedTime;
const getLastValidIntervalRangeByStartDate = (startDate) => {
    return axios.get(`/api/v1/interval-validation/${startDate}`);
}
const mapDateTextToDateObject = (dateText) => {
    const [day, month, year] = dateText.split('/');
    return new Date(year, month - 1, day);
}


const validateInterval = (startDate, endDate) => {
    const startDateObject = mapDateTextToDateObject(startDate);
    const endDateObject = mapDateTextToDateObject(endDate);
    
    if (startDateObject > endDateObject) {
        throw new Error('A data de início não pode ser maior que a data de fim');
    }

    return true;
}

export default validateInterval;
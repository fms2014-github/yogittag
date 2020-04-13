export default (value = '') => {
    value = '' + value
    //날짜를 YYYY-MM-DD HH:mm로 변경한다.
    var values = value.split(':')
    var dateValue = values.length >= 2 ? values[0] + ':' + values[1] : value
    return dateValue
}

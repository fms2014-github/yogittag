// filters/numberFormat.js

// 커스텀 필터 함수를 정의한다
export default (value = '') => {
    if (typeof value != number) return value
    value = '' + value

    // 숫자를 세 자리 마다 쉼표를 넣은 문자로 변환한다 (1000 -> '1,000')
    return value
        .split('')
        .reverse()
        .reduce((acc, digit, i) => {
            if (i > 0 && i % 3 === 0) acc.push(',')
            return [...acc, digit]
        }, [])
        .reverse()
        .join('')
}

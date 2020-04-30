<template>
    <div id="minigame-wrap" class="close-minigame">
        <div class="minigame-nav" @click="minigameButton">
            <span class="material-icons" v-if="isMinigmae">double_arrow</span>
            <span v-if="!isMinigmae">
                미
                <br />니
                <br />게
                <br />임
                <br />
            </span>
        </div>
        <div id="minigame">
            <h3 align="center">음식 카테고리 월드컵</h3>
            <h4
                align="center"
                :style="setTime < 10.0 ? 'color: red;' : ''"
            >남은 시간 : {{ setTime >= 0 ? setTime.toFixed(1) : '' }}</h4>
            <button
                class="selected"
                @click="selected(0)"
                v-show="ready && index <= 4"
                :style="'background:' + dataList[index][0].color"
            >{{ dataList[index][0].text }}</button>
            <button
                class="selected"
                @click="selected(1)"
                v-show="ready && index <= 4"
                :style="'background:' + dataList[index][1].color"
            >{{ dataList[index][1].text }}</button>
            <div id="answer" v-if="index > 4">
                <h4>
                    추천해주는
                    <br />음식 카테고리는??
                </h4>
                <b>{{ answer }}</b> 입니다.
            </div>
            <button v-show="!ready" id="ready" @click="start">{{ setTime == 30 ? '시작' : '다시 시작' }}</button>
        </div>
    </div>
</template>

<script>
var timer
var stoptimer
var mql = window.matchMedia('screen and (max-width: 480px)')
if (mql.matches) {
    window.onload = () => {
        let setTime = document.querySelector('#minigame h4').innerText
        console.log(setTime.replace(/[^0-9]./g, ''))
        if (
            Number(setTime.replace(/[^0-9]./g, '')) < 30 &&
            Number(setTime.replace(/[^0-9]./g, '')) > 0
        ) {
            document.querySelector('#ready').style.verticalAlign = 'middle'
            document.querySelector('#ready').style.width = '80px'
        }
    }
    // document.querySelector('#ready').style.width
} else {
    window.onload = () => {
        document.querySelector('#ready').style.removeProperty('vertical-align')
        document.querySelector('#ready').style.removeProperty('width')
    }
}
mql.addListener(() => {
    if (mql.matches) {
        let setTime = document.querySelector('#minigame h4').innerText
        console.log(setTime.replace(/[^0-9]./g, ''))
        if (
            Number(setTime.replace(/[^0-9]./g, '')) < 30 &&
            Number(setTime.replace(/[^0-9]./g, '')) > 0
        ) {
            document.querySelector('#ready').style.verticalAlign = 'middle'
            document.querySelector('#ready').style.width = '80px'
        }
    } else {
        document.querySelector('#ready').style.removeProperty('vertical-align')
        document.querySelector('#ready').style.removeProperty('width')
    }
})

export default {
    data() {
        return {
            ready: false,
            index: 0,
            dataList: [
                [
                    {
                        text: "부드러운",
                        color: "#FFEBCD",
                        category: ["국밥", "김밥", "피자", "물회", "고기", "카페", "국수", "찜닭", "초밥", "파스타", "냉면", "해물찜", "짜장면", "짬뽕", "떡볶이", "순대", "치킨"]
                    },
                    {
                        text: "딱딱한",
                        color: "#B8860B",
                        category: ["돈까스", "치킨", "조개구이", "닭발", "탕수육"]
                    }
                ],
                [
                    {
                        text: "국물있는",
                        color: "#E9967A",
                        category: ["국밥", "물회", "카페", "찜닭", "국수", "냉면", "파스타", "해물찜", "짬뽕", "떡볶이", "조개구이"]
                    },
                    {
                        text: "국물없는",
                        color: "#8FBC8F",
                        category: ["김밥", "피자", "고기", "카페", "초밥", "짜장면", "순대", "돈까스", "치킨", "닭발", "탕수육"]
                    }
                ],
                [
                    {
                        text: "든든한",
                        color: "#ADD8E6",
                        category: ["국밥", "물회", "찜닭", "해물찜", "고기", "돈까스", "치킨", "탕수육"]
                    },
                    {
                        text: "간단한",
                        color: "#E0FFFF",
                        category: ["카페", "국수", "냉면", "파스타", "짬뽕", "떡볶이", "김밥", "피자", "초밥", "짜장면", "순대", "조개구이", "닭발"]
                    }
                ],
                [
                    {
                        text: "면/빵",
                        color: "#FFB6C1",
                        category: ["카페", "국수", "냉면", "파스타", "짬뽕", "떡볶이", "피자", "짜장면", "순대", "치킨", "탕수육", "닭발"]
                    },
                    {
                        text: "밥",
                        color: "#D3D3D3",
                        category: ["국밥", "물회", "찜닭", "해물찜", "고기", "돈까스", "치킨", "탕수육", "떡볶이", "김밥", "피자", "초밥", "닭발"]
                    }
                ],
                [
                    {
                        text: "뜨거운",
                        color: "#FF4500",
                        category: ["카페", "국수", "파스타", "짬뽕", "떡볶이", "짜장면", "순대", "치킨", "탕수육", "피자", "닭발", "조개구이", "국밥", "찜닭", "해물찜", "고기", "돈까스"]
                    },
                    {
                        text: "차가운",
                        color: "#4169E1",
                        category: ["카페", "국수", "냉면", "순대", "물회", "초밥"]
                    }
                ],
                [
                    {
                        text: null,
                        color: null
                    },
                    {
                        text: null,
                        color: null
                    }
                ]
            ],
            categoryList: {
                중국집: ["짜장면", "짬뽕", "탕수육", "중식", "중국집"],
                분식: ["떡볶이", "순대", "김밥", "라면", "튀김", "분식", "어묵", "오뎅"],
                해물: ["조개구이", "해물", "코다리", "아구"],
                고기: ["삼겹", "갈매기", "항정", "고기", "정육"],
                초밥: ["초밥", "스시"],
                피자: ["피자"],
                치킨: ["치킨", "후라이드"],
                카페: ["카페"],
                돈까스: ["돈까스"],
                국수: ["국수"],
                파스타: ["파스타"],
                냉면: ["평양", "함흥", "냉면"],
                국밥: ["국밥"],
                물회: ["물회"],
            },
            selectedList: Object,
            answer: 'abcdefg',
            setTime: 30.0,
            isMinigmae: false,
        }
    },
    mounted() {
    },
    watch: {
        index: function (v) {
            if (v > 4) {
                clearInterval(timer)
                this.timeOut()
                if (mql.matches) {
                    let setTime = document.querySelector('#minigame h4').innerText
                    console.log(setTime.replace(/[^0-9]./g, ''))
                    if (
                        Number(setTime.replace(/[^0-9]./g, '')) < 30 &&
                        Number(setTime.replace(/[^0-9]./g, '')) > 0
                    ) {
                        document.querySelector('#ready').style.verticalAlign = 'middle'
                        document.querySelector('#ready').style.width = '80px'
                    }
                    // document.querySelector('#ready').style.width
                } else {
                    document.querySelector('#ready').style.removeProperty('vertical-align')
                    document.querySelector('#ready').style.removeProperty('width')

                    let tmp = []
                    let cnt = Math.max(...Object.values(this.selectedList))
                    for (let [key, value] of Object.entries(this.selectedList)) {
                        if (value == cnt) {
                            tmp.push(key)
                        }
                    }

                    let searchList = []
                    this.answer = tmp[Math.floor(Math.random() * tmp.length)]
                    for (var [key, value] of Object.entries(this.categoryList)) {
                        for (v of value) {
                            if (this.answer == v) {
                                searchList = value
                            }
                        }
                    }
                }
            }
        },
        setTime: function (v) {
            if (v <= 0) {
                clearInterval(timer)
                this.timeOut()
            }
        },
    },
    methods: {
        selected(idx) {
            this.dataList[this.index][idx].category.forEach((c) => {
                if (c in this.selectedList) {
                    this.selectedList[c] += 1
                } else {
                    this.selectedList[c] = 1
                }
            })
            this.index++
        },
        start() {
            if (this.setTime != 30) {
                this.index = 0
                this.selectedList = {}
                this.setTime = 30
            }
            this.ready = true
            timer = setInterval(() => {
                this.setTime -= 0.01
            }, 10)
        },
        timeOut() {
            this.ready = false
        },
        minigameButton() {
            this.isMinigmae = !this.isMinigmae
            this.index = 0
            this.selectedList = {}
            this.setTime = 30
            this.ready = false
            clearInterval(timer)
            document.querySelector('#ready').style.removeProperty('vertical-align')
            document.querySelector('#ready').style.removeProperty('width')
            document.getElementById('minigame-wrap').classList.toggle('close-minigame')
        },
    },
}
</script>

<style lang="scss" scoped>
#minigame-wrap {
    display: flex;
    position: sticky;
    left: 100%;
    bottom: 50px;
    width: 100%;
    max-width: 330px;
    border-radius: 8px 0 0 8px;
    box-shadow: 0 0 3px 1px rgba(100, 100, 100, 0.7);
    z-index: 10;
    overflow: hidden;
    #minigame {
        display: inline-block;
        background-color: white;
        width: calc(100% - 16px);
        padding: 12px;
    }
    .minigame-nav {
        display: inline-flex;
        align-items: center;
        background-color: white;
        padding: 8px 6px;
        border-radius: 8px 0 0px 8px;
        cursor: pointer;
        .material-icons {
            font-size: 1.3rem;
        }
    }
    #ready {
        width: calc(100% - 20px);
        margin: 10px;
        padding: 8px 16px;
        border-radius: 8px;
        background-color: rgb(240, 169, 16);
        color: white;
        outline: none;
    }
    .selected {
        width: calc(50% - 20px);
        height: 15vh;
        margin: 10px;
        padding: 8px 16px;
        border-radius: 8px;
        box-shadow: 0 0 4px 2px rgba(128, 128, 128, 0.7);
        outline: none;
        font-size: 20px;
    }
    #answer {
        width: calc(100% - 20px);
        margin: 10px;
        padding: 8px 16px;
        border-radius: 8px;
        box-shadow: 0 0 3px 1px rgba(128, 128, 128, 0.7);
        text-align: center;
        h4 {
            margin: 0 0 6px 0;
            font-weight: 100;
        }
    }
}

.close-minigame {
    width: 32px !important;
    height: 127px;
}

@media (max-width: 480px) {
    #minigame-wrap {
        position: absolute;
        bottom: 0px;
        width: 100%;
        max-width: 100%;
        border-radius: 0px;
        #answer {
            display: inline-block;
            vertical-align: middle;
            width: calc(100% - 120px);
        }
    }
}
</style>

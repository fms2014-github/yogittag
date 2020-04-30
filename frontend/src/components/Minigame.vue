<template>
    <div id="minigame-wrap" class="close-minigame">
        <div class="minigame-nav" @click="minigameButton">
            <span class="material-icons" v-if="isMinigmae">
                <img height="33px;" src="@/assets/img/double_arrow.png" alt=">>" />
            </span>
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
            <h4 align="center">남은 시간 : {{ setTime >= 0 ? setTime.toFixed(1) : '' }}</h4>
            <button
                class="selected"
                @click="selected(choiseA)"
                v-show="ready && index <= 10"
            >{{ choiseA }}</button>
            <button
                class="selected"
                @click="selected(choiseB)"
                v-show="ready && index <= 10"
            >{{ choiseB }}</button>
            <div id="answer" v-if="index > 10">
                <h4>
                    추천해주는
                    <br />음식 카테고리는??
                </h4>
                <b>{{ answer }}</b> 입니다.
            </div>
            <button v-show="!ready" id="ready" @click="start">{{ setTime == 60 ? '시작' : '다시 시작' }}</button>
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
            Number(setTime.replace(/[^0-9]./g, '')) < 60 &&
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
            Number(setTime.replace(/[^0-9]./g, '')) < 60 &&
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
                'data 0',
                'data 1',
                'data 2',
                'data 3',
                'data 4',
                'data 5',
                'data 6',
                'data 7',
                'data 8',
                'data 9',
            ],
            choiseA: '',
            choiseB: '',
            selectedList: [],
            answer: 'abcdefg',
            setTime: 60.0,
            isMinigmae: false,
        }
    },
    mounted() {
        this.choiseA = this.dataList[this.index++]
        this.choiseB = this.dataList[this.index++]
    },
    watch: {
        index: function (v) {
            if (v > 10) {
                clearInterval(timer)
                this.timeOut()
                if (mql.matches) {
                    let setTime = document.querySelector('#minigame h4').innerText
                    console.log(setTime.replace(/[^0-9]./g, ''))
                    if (
                        Number(setTime.replace(/[^0-9]./g, '')) < 60 &&
                        Number(setTime.replace(/[^0-9]./g, '')) > 0
                    ) {
                        document.querySelector('#ready').style.verticalAlign = 'middle'
                        document.querySelector('#ready').style.width = '80px'
                    }
                    // document.querySelector('#ready').style.width
                } else {
                    document.querySelector('#ready').style.removeProperty('vertical-align')
                    document.querySelector('#ready').style.removeProperty('width')
                }
            }
        },
        setTime: function (v) {
            if (v <= 0) {
                console.log(v)
                clearInterval(timer)
                this.timeOut()
            }
        },
    },
    methods: {
        selected(v) {
            console.log(v)
            this.selectedList.push(v)
            this.choiseA = this.dataList[this.index++]
            this.choiseB = this.dataList[this.index++]
        },
        start() {
            if (this.setTime != 60) {
                this.index = 0
                this.choiseA = this.dataList[this.index++]
                this.choiseB = this.dataList[this.index++]
                this.selectedList = []
                this.setTime = 60
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
            this.choiseA = this.dataList[this.index++]
            this.choiseB = this.dataList[this.index++]
            this.selectedList = []
            this.setTime = 60
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
@font-face {
    font-family: 'Dovemayo-Medium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_four@1.0/Dovemayo-Medium.woff')
        format('woff');
    font-weight: normal;
    font-style: normal;
}

* {
    font-family: 'Dovemayo-Medium';
}

#minigame-wrap {
    display: flex;
    position: absolute;
    right: 0px;
    bottom: 48px;
    width: 100%;
    max-width: 280px;
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
    }
    .selected {
        width: calc(50% - 20px);
        margin: 10px;
        padding: 8px 16px;
        border-radius: 8px;
        box-shadow: 0 0 4px 2px rgba(128, 128, 128, 0.7);
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

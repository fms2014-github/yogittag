<template>
    <div id="faq-qna" class="radius-button">
        <button title="Help" id="faq-qna-button" @click="egg">
            <span class="material-icons">
                help
            </span>
        </button>
    </div>
</template>

<script>
export default {
    methods: {
        egg(){
            alert('QnA 서비스 준비중입니다.\n저희 서비스에 관심가져주셔서 감사합니다.')
        }
    }
}
</script>

<style lang="scss" scoped>
#faq-qna {
    position: absolute;
    top: 18px;
    right: 18px;
    z-index: 10;
}
</style>

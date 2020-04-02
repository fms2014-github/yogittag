<template>
    <div id="user-registrate">
        <div id="registrate-form">
            <h2 id="registrate-title">
                약간의 정보만 입력하면 <br />
                더 많은 기능을 사용할 수 있어요
            </h2>
            <div id="registrate-email-input">
                <label for="registrate-email">Email</label
                ><input id="registrate-email" type="email" />
            </div>
            <div id="password-input">
                <label for="registrate-password">password</label
                ><input id="registrate-password" type="password" />
            </div>
            <div id="password-input-repeat">
                <label for="registrate-password-repeat">password check</label
                ><input id="registrate-password-repeat" type="password" />
            </div>
            <div id="nickname-input">
                <label for="registrate-nickname">nickname</label
                ><input id="registrate-nickname" type="text" />
            </div>
            <button id="registrate-button" @click="registrateFinish">가입 완료</button>
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import '../assets/css/button.scss'
export default {
    methods: {
        ...mapMutations('app', ['registrateFinish']),
    },
}
</script>

<style lang="scss" scoped>
#user-registrate {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0px;
    left: 0px;
    width: 100vw;
    height: 100vh;
    background-color: rgba(255, 255, 255, 0.4);
    z-index: 9;
    #registrate-form {
        min-width: 300px;
        width: 30%;
        max-width: 450px;
        padding: 16px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 0 4px 2px rgba(128, 128, 128, 0.7);
        #registrate-title {
            text-align: center;
            margin-bottom: 26px;
        }
        #registrate-email-input,
        #password-input,
        #password-input-repeat,
        #nickname-input {
            label[for='registrate-email'],
            label[for='registrate-password'],
            label[for='registrate-password-repeat'],
            label[for='registrate-nickname'] {
                display: inline-block;
                width: 100%;
                height: 28px;
                font-size: 1.4rem;
                margin: 8px 0;
            }
            #registrate-email,
            #registrate-password,
            #registrate-password-repeat,
            #registrate-nickname {
                width: 100%;
                height: 32px;
                padding: 8px;
                border: {
                    width: 1px;
                    style: solid;
                    color: rgb(200, 200, 200);
                    radius: 4px;
                }
                font-size: 1.2rem;
            }
        }
        #registrate-button {
            margin: 32px 0px 8px 0px;
            width: 100%;
            height: 48px;
            border-radius: 8px;
            color: white;
            background-color: rgb(241, 177, 0);
        }
    }
}
</style>

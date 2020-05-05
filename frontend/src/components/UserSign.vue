<template>
    <div id="user-sign">
        <div id="login-form">
            <h2 id="login-title">
                소셜 로그인
            </h2>
            <button id="google-login-button" @click="googlelogin">
                <img src="../assets/icons/btn_google_signin_dark_normal_web@2x.png" />
            </button>
            <button id="naver-login-button" @click="naverlogin">
                <img src="../assets/icons/naver_login_button_Green.png" />
            </button>
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import axiosApi from '../api/axiosScript.js'
import '../assets/css/button.scss'
export default {
    data() {
        return {}
    },
    methods: {
        googlelogin() {
            window.location.href =
                'https://accounts.google.com/o/oauth2/v2/auth?client_id=25608544222-lfe7jdkikoef92jgt45mvhe83ts98n80.apps.googleusercontent.com&redirect_uri=http://i02d105.p.ssafy.io/google-auth&response_type=code&scope=https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile+openid&access_type=offline&prompt=consent'
        },
        naverlogin() {
            window.location.href =
                'https://nid.naver.com/oauth2.0/authorize?client_id=ISrEReGthtZMH67maTLZ&response_type=code&redirect_uri=http://i02d105.p.ssafy.io/naver-auth'
        },
    },
}
</script>

<style lang="scss" scoped>
#user-sign {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0px;
    left: 0px;
    width: 100vw;
    height: 100vh;
    background-color: rgba(255, 255, 255, 0.4);
    z-index: 8;
    #login-form {
        min-width: 280px;
        width: 30%;
        max-width: 350px;
        padding: 16px;
        background-color: rgb(255, 249, 231);
        border-radius: 10px;
        box-shadow: 0 0 4px 2px rgba(128, 128, 128, 0.7);
        text-align: center;
        #google-login-button {
            margin: 8px;
            & img {
                width: 250px;
                border-radius: 8px;
                color: white;
            }
        }
        #naver-login-button {
            margin: 8px;
            padding: 0 3px;
            & img {
                width: 242px;
                border-radius: 8px;
                color: white;
            }
        }
        #login-title {
            font-size: 1.6rem;
            text-align: center;
            margin-bottom: 26px;
        }
    }
}
</style>

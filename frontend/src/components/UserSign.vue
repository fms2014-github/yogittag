<template>
    <div id="user-sign">
        <div id="login-form">
            <h2 id="login-title">
                로그인을 하시면 <br />
                더 많은 기능을 사용할 수 있어요
            </h2>
            <div id="email-input">
                <label for="email">Email</label><input id="email" type="email" />
            </div>
            <div id="password-input">
                <label for="password">password</label><input id="password" type="password" />
            </div>
            <button id="login-button">로그인</button>
            <hr />
            <div id="login-prablem">
                <span id="forget-account">이메일이나 비밀번호가 기억나지 않으신가요?</span>
                <button id="find-account-button">계정 찾기</button>
                <span id="not-registered">새로오신 분인가요?</span>
                <button id="not-registered-button">회원 가입</button>
            </div>
        </div>
    </div>
</template>

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
        min-width: 300px;
        width: 30%;
        max-width: 450px;
        padding: 16px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 0 4px 2px rgba(128, 128, 128, 0.7);
        #login-title {
            text-align: center;
            margin-bottom: 26px;
        }
        #email-input,
        #password-input {
            label[for='email'],
            label[for='password'] {
                display: inline-block;
                width: 100%;
                height: 28px;
                font-size: 1.4rem;
                margin: 8px 0;
            }
            #email,
            #password {
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
        #login-button {
            background-color: rgb(0, 153, 255);
        }
        hr {
            margin: 8px 0px;
            border: {
                width: 1px;
                style: solid;
                color: rgb(200, 200, 200);
            }
        }
        #login-prablem {
            #forget-account {
                font: {
                    color: rgb(200, 200, 200);
                    size: 0.7rem;
                }
            }
            #find-account-button {
                background-color: rgb(35, 207, 0);
            }
            #not-registered {
                font: {
                    color: rgb(200, 200, 200);
                    size: 0.7rem;
                }
            }
            #not-registered-button {
                background-color: rgb(241, 177, 0);
            }
        }
    }
}
#login-button,
#find-account-button,
#not-registered-button {
    margin: 8px 0px;
    width: 100%;
    height: 48px;
    border-radius: 8px;
    color: white;
}
</style>

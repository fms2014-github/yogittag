<template>
    <div id="user-profile">
        <div id="user-profile-wrap">
            <img id="profile-image" src="https://via.placeholder.com/200" />
            <div id="user-infomation">
                <label for="user-name">이름 </label>: <input id="user-name" type="text" /><br />
                <label for="user-email">이메일 </label>:
                <input id="user-email" type="text" readonly /><br />
                <label for="user-birth">생일 </label>: <input id="user-birth" type="text" /><br />
                <label for="user-gender">성별 </label>:
                <input id="user-gender" type="text" readonly /><br />
                <label for="user-reg-day">가입일 </label>:
                <input id="user-reg-day" type="text" readonly /><br />
            </div>
            <div id="user-favorites">
                <h3 id="user-favorites-title">회원님이 좋아하는 음식 분류</h3>
            </div>
            <div id="user-history">
                <div id="writed-review">
                    <h3>회원님이 작성한 리뷰</h3>
                </div>
                <div id="lasted-searched-data">
                    <h3>최근 검색한 가게</h3>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
#user-profile {
    position: absolute;
    top: 0px;
    left: 0px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
    background-color: rgba(255, 255, 255, 0.4);
    z-index: 8;
    #user-profile-wrap {
        display: flex;
        flex-wrap: wrap;
        background-color: rgb(255, 255, 255);
        min-width: 300px;
        width: 40vw;
        max-width: 680px;
        padding: 16px;
        border-radius: 10px;
        box-shadow: 0 0 4px 2px rgba(128, 128, 128, 0.7);
        #profile-image {
            width: 200px;
            height: 200px;
            margin: 0 20px 20px 0;
            border-radius: 50%;
        }
        #user-infomation {
            width: calc(100% - 220px);
            margin-bottom: 30px;
            font-size: 1.3rem;
            label {
                display: inline-block;
                width: 18%;
                height: 32px;
                margin: 4px;
                font-size: 1.3rem;
            }
            input {
                display: inline-block;
                width: calc(80% - 26px);
                height: 32px;
                margin: 4px;
                font-size: 1.3rem;
            }
        }
        #user-favorites {
            width: 100%;
        }
        #user-history {
            width: 100%;
            #writed-review,
            #lasted-searched-data {
                display: inline-block;
                width: 50%;
                h3 {
                    display: inline-block;
                }
            }
        }
    }
}
</style>

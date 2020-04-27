<template>
    <div id="profile-edit-wrap">
        <div id="profile-edit">
            <h3>회원 정보 수정</h3>
            <div class="profile-edit-input">
                <label for="edit-name">이름</label
                ><input v-model="edit.name" id="edit-name" type="text" />
            </div>
            <div class="profile-edit-input">
                <label for="edit-nickname">닉네임</label
                ><input v-model="edit.nickname" id="edit-nickname" type="text" />
            </div>
            <div class="profile-edit-input">
                <label for="edit-gender">성별</label
                ><select v-model="edit.gender" id="edit-gender"
                    ><option value="" disabled selected>선택해주세요</option>
                    <option value="남">남</option
                    ><option value="여">여</option></select
                >
            </div>
            <div class="profile-edit-input">
                <label for="edit-birth">생일</label
                ><input v-model="edit.birthday" id="edit-birth" type="date" />
            </div>
            <div class="profile-edit-input">
                <label for="edit-profile-image">프로필 이미지</label
                ><input
                    id="edit-profile-image"
                    name="profilePicture"
                    type="file"
                    accept="image/*"
                    @change="onChange"
                />
            </div>
            <div class="profile-edit-input">
                <label for="edit-cover-image">커버 이미지</label
                ><input
                    id="edit-cover-image"
                    name="coverPicture"
                    type="file"
                    accept="image/*"
                    @change="onChange"
                />
            </div>
            <button class="edit" id="submit" @click="submit">수정</button>
            <button class="edit" id="cancel">취소</button>
        </div>
    </div>
</template>

<script>
import axios from '../api/axiosScript'
export default {
    data() {
        return {
            edit: {
                name: '',
                nickName: '',
                gender: '',
                birthday: '',
                profilePicture: '',
                coverPicture: '',
            },
        }
    },
    methods: {
        submit() {
            axios.updateUser(
                this.edit,
                (res) => {
                    console.log(res)
                },
                (err) => {
                    console.log(err)
                },
            )
        },
        async onChange(e) {
            console.log('aaa', e.target.files)
            let imageLink = await axios.imageUpload(e.target.files[0])
            this.edit[e.target.name] = imageLink
        },
    },
}
</script>

<style lang="scss" scoped>
$border-color: rgb(133, 133, 133);
#profile-edit-wrap {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
    z-index: 20;
    position: relative;
    top: 0px;
    #profile-edit {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 3px 1px rgba(128, 128, 128, 0.7);
        text-align: center;
        .profile-edit-input {
            margin: 4px 0;
            label {
                padding: 5px;
                width: 120px;
                border-radius: 7px 0 0 7px;
                border: {
                    style: solid;
                    width: 1px;
                    color: $border-color;
                }
            }
            input,
            select {
                padding: 5px;
                width: calc(100% - 120px);
                border-radius: 0 7px 7px 0;
                border: {
                    style: solid;
                    width: 1px 1px 1px 0px;
                    color: $border-color;
                }
            }
            input[type='date'] {
                font-size: 0.95rem;
            }
            input[type='file'] {
                font-size: 0.75rem;
                vertical-align: top;
            }
        }
        .edit {
            width: 112px;
            height: 32px;
            margin: 0 8px;
            border: {
                style: solid;
                width: 1px;
                color: $border-color;
                radius: 7px;
            }
        }
    }
}
</style>

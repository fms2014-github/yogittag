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
            <button v-if="!isFullSize" class="edit" id="submit" @click="submit">수정</button>
            <button v-if="!isFullSize" class="edit" id="cancel" @click="cancel">취소</button>
            <button v-if="isFullSize" class="edit" id="submit" @click="submit">정보 추가</button>
            <button v-if="isFullSize" class="edit" id="cancel" @click="cancel">나중에</button>
        </div>
    </div>
</template>

<script>
import axios from '../api/axiosScript'
import { mapMutations } from 'vuex'
export default {
    props: ['isFullSize'],
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
        ...mapMutations('app', ['switchIsEdit']),
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
        cancel() {
            if (!this.isFullSize) {
                this.switchIsEdit()
            } else {
                this.$router.push('/')
            }
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
    position: fixed;
    top: 50%;
    transform: translateY(-50%);
    #profile-edit {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 3px 1px rgba(128, 128, 128, 0.7);
        text-align: center;
        font-size: 0.95rem;
        .profile-edit-input {
            margin: 8px 0;
            padding: 4px 0;
            border: {
                style: solid;
                width: 0 0 4px 0;
                color: rgb(230, 230, 230);
            }
            label {
                padding: 5px;
                width: 120px;
                margin: 0px;
                border: {
                    style: solid;
                    width: 0 1px 0 0;
                    color: rgb(230, 230, 230);
                }
            }
            input,
            select {
                padding: 5px;
                width: calc(100% - 120px);
            }
            input[type='date'] {
                font-size: 0.95rem;
            }
            input[type='file'] {
                font-size: 0.79rem;
                vertical-align: top;
            }
        }
        .edit {
            width: 110px;
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

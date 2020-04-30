<template>
    <div class="site">
        <header class="masthead" style="text-align: center;">
            <img height="250px;" src="../assets/img/main_logo.png" alt="요기딱" />
        </header>
        <main id="content" class="main-area">
            <section class="splash">
                <div class="splash-content">
                    <!-- PROFILE (MIDDLE-CONTAINER) -->
                    <div class="content-profile-page">
                        <div class="profile-user-page profile-card">
                            <div class="img-user-profile">
                                <img
                                    class="profile-bgHome"
                                    src="https://blog.hmgjournal.com/images_n/contents/180404_food01.jpg"
                                />
                                <img
                                    class="avatar"
                                    src="https://user-images.githubusercontent.com/22102664/79730972-97fd9700-832c-11ea-886f-225cf0c89832.PNG"
                                    alt="allan"
                                />
                            </div>
                            <button>Follow</button>
                            <div class="user-profile-data">
                                <h1>Seohyun</h1>
                                <button id="profile-edit-button" @click="profileEdit">
                                    <span class="material-icons">
                                        settings
                                    </span>
                                </button>
                                <p style="margin: 10px;">한식 | 중식 | 양식</p>
                            </div>
                            <ul class="data-user">
                                <li>
                                    <a>
                                        <strong>61.780</strong>
                                        <span>Posts</span>
                                    </a>
                                </li>
                                <li>
                                    <a>
                                        <strong>33.480</strong>
                                        <span>Followers</span>
                                    </a>
                                </li>
                                <li>
                                    <a>
                                        <strong>3.546</strong>
                                        <span>Following</span>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <!-- .splash-content -->
            </section>
            <section class="more">
                <div class="more-content">
                    <h2 class="content-title">리뷰 정보 추가하기</h2>
                    <div class="row">
                        <small-card
                            v-for="item in testCardDate"
                            :key="item.id"
                            :routing="item.routing"
                            :img="item.img"
                            :gender="item.gender"
                            :title="item.title"
                            :reg_time="item.reg_time"
                            :content="item.content"
                            :score="item.score"
                        />
                    </div>
                    <button v-b-modal.modal id="registerButton">
                        <img id="registerButtonImg" :src="registerRiviewImg" />
                    </button>
                    <b-modal
                        :no-close-on-backdrop="true"
                        @ok="modalCilck()"
                        id="modal"
                        size="lg"
                        title="Review"
                    >
                        <ReviewForm />
                    </b-modal>
                </div>
                <!-- .more-content -->
            </section>
            <!-- .more -->
        </main>

        <!-- .sidebar -->

        <footer class="footer">
            <aside style="font-size: 1.5em;">요기딱</aside>
            <aside>
                Content, layout, design:
                <a href target="_blank" rel="nofollow">D105</a>.
            </aside>
        </footer>
        <UpFocusButton />
        <profileEditPage v-if="isEdit" :getEmail="this.email" :isFullSize="false" />
    </div>
    <!-- .site -->
</template>
<script>
import SmallCard from '@/components/cards/SmallCard'
import UpFocusButton from '@/components/buttons/UpFocusButton'
import infiniteScroll from 'vue-infinite-scroll'
import ReviewForm from '@/components/forms/ReviewForm.vue'
import profileEditPage from './profileEditPage.vue'

import { mapState, mapMutations } from 'vuex'
export default {
    data() {
        return {
            email: '',
            testCardDate: [
                {
                    img: 'https://loremflickr.com/700/400',
                    gender: '남',
                    title: 'Reivew Title',
                    reg_time: '2020-04-09 03:48:40.799058',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                    score: 4,
                },
                {
                    img: 'https://picsum.photos/700/400',
                    gender: '여',
                    title: 'Reivew Title2',
                    reg_time: '2020-04-09 03:48',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                    score: 1,
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
            ],
        }
    },
    components: {
        SmallCard,
        UpFocusButton,
        infiniteScroll,
        ReviewForm,
        profileEditPage,
    },
    created: function () {
        window.addEventListener('scroll', this.handleScroll)
    },
    beforeDestroy: function () {
        window.removeEventListener('scroll', this.handleScroll)
    },
    computed: {
        ...mapState('app', ['isEdit']),
    },
    methods: {
        ...mapMutations('app', ['switchIsEdit']),
        profileEdit() {
            this.switchIsEdit()
        },
        handleScroll() {
            if (this.timer === null) {
                this.timer = setTimeout(
                    function () {
                        this.scrollY = window.scrollY || document.documentElement.scrollTop
                        this.registerButtonUX(this.scrollY)
                        clearTimeout(this.timer)
                        this.timer = null
                    }.bind(this),
                    200,
                )
            }
        },
        registerButtonUX(scrollPosition) {
            var rb = document.getElementById('registerButtonImg')
            if (scrollPosition > 200 && !this.ux.rBtnFlag) {
                var player = rb.animate(
                    [{ transform: 'translate(0)' }, { transform: 'translate(0,-50px)' }],
                    150,
                )
                player.addEventListener('finish', function () {
                    rb.style.transform = 'translate(0,-50px)'
                })
                this.ux.rBtnFlag = true
            } else if (scrollPosition <= 200 && this.ux.rBtnFlag) {
                var player = rb.animate(
                    [{ transform: 'translate(0,-50px)' }, { transform: 'translate(0)' }],
                    150,
                )
                player.addEventListener('finish', function () {
                    rb.style.transform = 'translate(0)'
                })
                this.ux.rBtnFlag = false
            }
        },
        modalCilck(bvModalEvt) {
            console.log('modal ok click')
        },
    },
}
</script>
<style>
@import url(
    https://fonts.googleapis.com/css?family=Quicksand:300,
    400|Lato:400,
    300|Coda|Open + Sans
);
@font-face {
    font-family: 'Dovemayo-Medium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_four@1.0/Dovemayo-Medium.woff')
        format('woff');
    font-weight: normal;
    font-style: normal;
}

/* More section */

.more {
    padding: 2em;
}

.more-content {
    padding: 1.5em;
}

.content-title {
    font-family: 'Dovemayo-Medium';
    font-size: 40px;
}

.footer {
    font-family: 'Dovemayo-Medium';
    padding: 2em;
    background: hsl(0, 0%, 10%);
    color: white;
    text-align: center;
}

/*--------------------------------------------------------------
Basic responsive layout for all browsers:
--------------------------------------------------------------*/

.site {
    max-width: 50em;
    margin: 0 auto;
}

/*--------------------------------------------------------------
CSS Grid layout for modern browsers:
--------------------------------------------------------------*/

@supports (grid-area: auto) {
    @media screen and (min-width: 50em) {
        .site {
            max-width: none;
            display: grid;
            grid-template-columns: 15em auto;
        }

        .masthead {
            grid-column: 1/3;
        }

        .main-area {
            grid-column: 2/3;
        }

        .footer {
            grid-column: 1/3;
        }
    }

    @media screen and (min-width: 65em) {
        .site {
            grid-template-columns: 15em auto 15em;
        }

        .masthead {
            grid-column: 1/4;
        }

        .main-area {
            grid-row: 2;
            z-index: 1;
        }

        .footer {
            grid-column: 1/4;
        }
    }
}

a {
    text-decoration: none;
    color: #3498db;
}
.content-profile-page {
    margin: 1em auto;
    width: 44.23em;
}

.profile-card {
    background: #fff;
    border-radius: 0.3rem;
    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.2);
    border: 0.1em solid rgba(0, 0, 0, 0.2);
    margin-bottom: 1em;
}

.profile-user-page .img-user-profile {
    margin: 0 auto;
    text-align: center;
}
.profile-user-page .img-user-profile .profile-bgHome {
    border-bottom: 0.2em solid #f5f5f5;
    width: 44.23em;
    height: 16em;
}
.profile-user-page .img-user-profile .avatar {
    margin: 0 auto;
    background: #fff;
    width: 7em;
    height: 7em;
    padding: 0.25em;
    border-radius: 0.4em;
    margin-top: -10em;
    box-shadow: 0 0 0.1em rgba(0, 0, 0, 0.35);
    transform: translateY(65%);
}
.profile-user-page button {
    position: absolute;
    font-size: 13px;
    font-weight: bold;
    cursor: pointer;
    width: 7em;
    background: #3498db;
    border: 1px solid #2487c9;
    color: #fff;
    outline: none;
    border-radius: 0 0.6em 0.6em 0;
    padding: 0.8em;
}
.profile-user-page button:hover {
    background: #51a7e0;
    transition: background 0.2s ease-in-out;
    border: 1px solid #2487c9;
}
.profile-user-page .user-profile-data,
.profile-user-page .description-profile {
    text-align: center;
    padding: 4em 1.5em 0;
}
.profile-user-page .user-profile-data h1 {
    font-family: 'Lato', sans-serif;
    margin-top: 0.35em;
    color: #292f33;
    margin-bottom: 0;
    display: inline-block;
}
.profile-user-page .user-profile-data p {
    font-family: 'Lato', sans-serif;
    color: #8899a6;
    font-size: 1.1em;
    margin-top: 0;
    margin-bottom: 0.5em;
}
.profile-user-page .description-profile {
    color: #75787b;
    font-size: 0.98em;
}
.profile-user-page .data-user {
    font-family: 'Quicksand', sans-serif;
    margin-bottom: 0;
    cursor: pointer;
    padding: 0;
    list-style: none;
    display: table;
    width: 100.15%;
}
.profile-user-page .data-user li {
    margin: 0;
    padding: 0;
    width: 33.33334%;
    display: table-cell;
    text-align: center;
    border-left: 0.1em solid transparent;
}
.profile-user-page .data-user li:first-child {
    border-left: 0;
}
.profile-user-page .data-user li:first-child a {
    border-bottom-left-radius: 0.3rem;
}
.profile-user-page .data-user li:last-child a {
    border-bottom-right-radius: 0.3rem;
}
.profile-user-page .data-user li a,
.profile-user-page .data-user li strong {
    display: block;
}
.profile-user-page .data-user li a {
    background-color: #f7f7f7;
    border-top: 1px solid rgba(242, 242, 242, 0.5);
    border-bottom: 0.2em solid #f7f7f7;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(255, 255, 255, 0.4);
    padding: 0.93em 0;
    color: #46494c;
}
.profile-user-page .data-user li a strong,
.profile-user-page .data-user li a span {
    font-weight: 600;
    line-height: 1;
}
.profile-user-page .data-user li a strong {
    font-size: 2em;
}
.profile-user-page .data-user li a span {
    color: #717a7e;
}
.profile-user-page .data-user li a:hover {
    background: rgba(0, 0, 0, 0.05);
    border-bottom: 0.2em solid #3498db;
    color: #3498db;
}
.profile-user-page .data-user li a:hover span {
    color: #3498db;
}

#profile-edit-button {
    display: inline-block;
    position: static;
    width: auto;
    height: auto;
    padding: 0px;
    background-color: rgba(0, 0, 0, 0);
    border-color: rgba(0, 0, 0, 0);
    color: black;
    vertical-align: 30%;
    transform: translateX(35%);
}

#profile-edit-button span {
    font-size: 1rem;
}
/* footer h4 {
    display: block;
    text-align: center;
    clear: both;
    font-family: 'Coda', sans-serif;
    color: #566965;
    line-height: 6;
    font-size: 1em;
} */
/* footer h4 a {
    text-decoration: none;
    color: #3498db;
} */
</style>

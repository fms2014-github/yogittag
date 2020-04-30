<template>
    <div class="site">
        <a class="skip-link screen-reader-text" href="#content">Skip to content</a>
        <header class="masthead">
            <div class="logo">우리 로고</div>
            <h2 class="site-title">내 입맛, 네 입맛</h2>
        </header>
        <!-- .masthead -->
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
            <!-- .splash -->

            <section class="buckets">
                <ul>
                    <li>
                        <img
                            src="https://cdn.imweb.me/upload/S201701015868e87bb6cc8/32004a1f8b194.jpg"
                            alt="폴이네키친"
                        />
                        <div class="bucket">
                            <h3 class="bucket-title">폴이네 키친</h3>
                            <p>
                                친절하네요. 주말에 사람이 많았어요. 웨이팅하다가 들어갔는데 인기
                                비결은 맛이네요.
                            </p>
                        </div>
                        <!-- .bucket -->
                    </li>
                    <li>
                        <img
                            src="data:image/jpeg;base64,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"
                            alt="경동추어탕"
                        />
                        <div class="bucket">
                            <h3 class="bucket-title">경동추어탕</h3>
                            <p>와 맛있어요! 뜨끈~하고 든든~하게 추어탕 한 그릇!!</p>
                        </div>
                        <!-- .bucket -->
                    </li>
                </ul>
            </section>
            <!-- .buckets -->

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

        <aside class="sidebar">
            <div class="twin">
                <div class="donut-chart-block block">
                    <!-- DONUT CHART BLOCK (LEFT-CONTAINER) -->
                    <h2 class="titular">Seohyun's 입맛</h2>
                    <div class="donut-chart">
                        <!-- DONUT-CHART by @kseso https://codepen.io/Kseso/pen/phiyL -->
                        <div id="porcion1" class="recorte">
                            <div class="quesito ios" data-rel="21"></div>
                        </div>
                        <div id="porcion2" class="recorte">
                            <div class="quesito mac" data-rel="39"></div>
                        </div>
                        <div id="porcion3" class="recorte">
                            <div class="quesito win" data-rel="31"></div>
                        </div>
                        <div id="porcionFin" class="recorte">
                            <div class="quesito linux" data-rel="9"></div>
                        </div>
                        <!-- END DONUT-CHART by @kseso https://codepen.io/Kseso/pen/phiyL -->
                    </div>
                </div>
            </div>
            <div class="twin">
                <h2 class="content-title">추가 정보 넣기</h2>
            </div>
        </aside>
        <!-- .sidebar -->

        <footer class="colophon">
            <aside>우리로고</aside>
            <aside>
                Content, layout, design:
                <a href target="_blank" rel="nofollow">우리 팀명</a>.
            </aside>
        </footer>
        <profileEditPage v-if="isEdit" :getEmail="this.email" />
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
/*--------------------------------------------------------------
Accessibility
--------------------------------------------------------------*/
/* Text meant only for screen readers */
.screen-reader-text {
    clip: rect(1px, 1px, 1px, 1px);
    position: absolute !important;
    height: 1px;
    width: 1px;
    overflow: hidden;
}

.screen-reader-text:hover,
.screen-reader-text:active,
.screen-reader-text:focus {
    background-color: #f1f1f1;
    border-radius: 3px;
    box-shadow: 0 0 2px 2px rgba(0, 0, 0, 0.6);
    clip: auto !important;
    color: #21759b;
    display: block;
    font-size: 14px;
    font-weight: bold;
    height: auto;
    left: 5px;
    line-height: normal;
    padding: 15px 23px 14px;
    text-decoration: none;
    top: 5px;
    width: auto;
    z-index: 100000;
}

/*--------------------------------------------------------------
Typography
--------------------------------------------------------------*/

body {
    margin: 0;
    font-family: 'Source Sans Pro', 'Helvetica', 'Arial', sans-serif;
    font-size: 18px;
    line-height: 1.5;
}

/*--------------------------------------------------------------
General styling
--------------------------------------------------------------*/

img {
    display: block;
    border: 0;
    width: 100%;
    height: auto;
}

/* Promo section */

.logo,
.site-title {
    text-align: center;
}

.logo {
    margin-top: 0.3em;
    font-size: 6em;
}

.site-title {
    margin-top: -1em;
    margin-bottom: 2em;
}

/* Splash section */

.splash {
    background: #fff6e5;
    padding-bottom: 2em;
}

.splash-content {
    padding: 1.5em;
}

@media screen and (min-width: 600px) {
    .splash-text {
        columns: 2;
        column-gap: 2em;
    }

    .splash-text p {
        padding-top: 0;
    }
}

/* Buckets section */

.buckets {
    padding: 2em 1em 1em;
    background: #3e454c;
}

.buckets ul {
    margin: 0;
    padding: 0;
}

.buckets li {
    margin-bottom: 1em;
    background: white;
    list-style-type: none;
}

.bucket {
    padding: 1.5em;
}

/* More section */

.more {
    padding: 2em;
}

.more-content {
    padding: 1.5em;
}

/* Twins section */

.sidebar {
    background: hsl(0, 0%, 90%);
}

.twin {
    padding: 2em;
    background: #f0e0c6;
    color: black;
}

.twin:last-of-type {
    background: #f8f5f0;
}

.content-title {
    padding: 0.5em;
}

/* Colophon section */
.colophon {
    padding: 2em;
    background: hsl(0, 0%, 10%);
    color: white;
    text-align: center;
}

.colophon a {
    color: white;
}

.colophon a:hover,
.colophon a:focus {
    border-bottom: 1px solid white;
}

/*--------------------------------------------------------------
Use flex to create a three-bucket layout
--------------------------------------------------------------*/

@media screen and (min-width: 700px) {
    @supports (display: flex) {
        .buckets ul {
            display: flex;
            justify-content: space-around;
        }

        .buckets li {
            width: 48%;
        }
    }
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

        .sidebar {
            grid-column: 1/2;
            grid-row: 2/4;
        }

        .colophon {
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

        .sidebar {
            display: inherit;
            grid-template-columns: inherit;
            grid-column: 1/4;
            grid-row: 2/3;
        }

        .twin:last-of-type {
            grid-column: 3/4;
        }

        .main-area {
            grid-row: 2;
            z-index: 1;
        }

        .colophon {
            grid-column: 1/4;
        }
    }
}

/******************************************
DONUT-CHART by @kseso https://codepen.io/Kseso/pen/phiyL
******************************************/
.donut-chart {
    position: relative;
    width: 200px;
    height: 200px;
    margin: 2rem auto;
    border-radius: 100%;
}
p.center-date {
    background: #394264;
    position: absolute;
    text-align: center;
    font-size: 28px;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    width: 130px;
    height: 130px;
    margin: auto;
    border-radius: 50%;
    line-height: 35px;
    padding: 15% 0 0;
}
.center-date span.scnd-font-color {
    line-height: 0;
}
.recorte {
    border-radius: 50%;
    clip: rect(0px, 200px, 200px, 100px);
    height: 100%;
    position: absolute;
    width: 100%;
}
.quesito {
    border-radius: 50%;
    clip: rect(0px, 100px, 200px, 0px);
    height: 100%;
    position: absolute;
    width: 100%;
    font-family: monospace;
    font-size: 1.5rem;
}
#porcion1 {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
}

#porcion1 .quesito {
    background-color: #e64c65;
    -webkit-transform: rotate(76deg);
    transform: rotate(76deg);
}
#porcion2 {
    -webkit-transform: rotate(76deg);
    transform: rotate(76deg);
}
#porcion2 .quesito {
    background-color: #11a8ab;
    -webkit-transform: rotate(140deg);
    transform: rotate(140deg);
}
#porcion3 {
    -webkit-transform: rotate(215deg);
    transform: rotate(215deg);
}
#porcion3 .quesito {
    background-color: #4fc4f6;
    -webkit-transform: rotate(113deg);
    transform: rotate(113deg);
}
#porcionFin {
    -webkit-transform: rotate(-32deg);
    transform: rotate(-32deg);
}
#porcionFin .quesito {
    background-color: #fcb150;
    -webkit-transform: rotate(32deg);
    transform: rotate(32deg);
}
/******************************************
END DONUT-CHART
        */

/*********************************** */

@import url(
    https://fonts.googleapis.com/css?family=Quicksand:300,
    400|Lato:400,
    300|Coda|Open + Sans
);

body {
    background: #f8f5f0;
    font-family: 'Open sans', sans-serif;
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

<template>
    <div id="spinner">
        <div class="sk-chase">
            <div class="sk-chase-dot"></div>
            <div class="sk-chase-dot"></div>
            <div class="sk-chase-dot"></div>
            <div class="sk-chase-dot"></div>
            <div class="sk-chase-dot"></div>
            <div class="sk-chase-dot"></div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
#spinner {
    position: absolute;
    top: 0px;
    left: 0px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
    background-color: rgba(255, 255, 255, 0.4);
    z-index: 9999;
    .sk-chase {
        width: 60px;
        height: 60px;
        position: relative;
        animation: sk-chase 2.5s infinite linear both;
        .sk-chase-dot {
            width: 100%;
            height: 100%;
            position: absolute;
            left: 0;
            top: 0;
            animation: sk-chase-dot 2s infinite ease-in-out both;
        }

        .sk-chase-dot:before {
            content: '';
            display: block;
            width: 24%;
            height: 24%;
            background-color: #000;
            border-radius: 100%;
            animation: sk-chase-dot-before 2s infinite ease-in-out both;
        }

        .sk-chase-dot:nth-child(1) {
            animation-delay: -1.1s;
        }
        .sk-chase-dot:nth-child(2) {
            animation-delay: -1s;
        }
        .sk-chase-dot:nth-child(3) {
            animation-delay: -0.9s;
        }
        .sk-chase-dot:nth-child(4) {
            animation-delay: -0.8s;
        }
        .sk-chase-dot:nth-child(5) {
            animation-delay: -0.7s;
        }
        .sk-chase-dot:nth-child(6) {
            animation-delay: -0.6s;
        }
        .sk-chase-dot:nth-child(1):before {
            animation-delay: -1.1s;
        }
        .sk-chase-dot:nth-child(2):before {
            animation-delay: -1s;
        }
        .sk-chase-dot:nth-child(3):before {
            animation-delay: -0.9s;
        }
        .sk-chase-dot:nth-child(4):before {
            animation-delay: -0.8s;
        }
        .sk-chase-dot:nth-child(5):before {
            animation-delay: -0.7s;
        }
        .sk-chase-dot:nth-child(6):before {
            animation-delay: -0.6s;
        }
    }
}

@keyframes sk-chase {
    100% {
        transform: rotate(360deg);
    }
}

@keyframes sk-chase-dot {
    80%,
    100% {
        transform: rotate(360deg);
    }
}

@keyframes sk-chase-dot-before {
    50% {
        transform: scale(0.3);
    }
    100%,
    0% {
        transform: scale(1);
    }
}
</style>

<template>
    <div id="clock">
        <span id="utc" style="font-family: 'BMEULJIRO'; margin-right: 10px;">봄</span>
        <span id="day" style="font-family: 'BMEULJIRO'; margin-right: 10px;">MON</span>
        <span id="time">10:15:40 AM</span>
    </div>
</template>
<script>
export default {
  name: 'TimeNow',
  data: {
    textContent: '',
  },
  methods: {
    // START CLOCK SCRIPT
    showTime(){
        let h1 = document.querySelector('#time');
        let day = document.querySelector('#day');
        let utc = document.querySelector('#utc');
        let date = new Date();
        let h = date.getHours();
        let m = date.getMinutes();
        let s = date.getSeconds();
        let month = date.getMonth();
        // let datenum = date.getDate();
        // let fullYear= date.getFullYear();
        let session; 
        let mon;
        if(h>11){
            session = "PM"
        }else {
            session = "AM";
        }
        if(h>12){
          h=h-12;
        }

        let daynum = date.getDay();
        let dayText= daynum;
        if(daynum==0){
            day.textContent="일요일";
        }else if(daynum == 1){
            day.textContent="월요일";
        }else if(daynum==2){
            day.textContent="화요일";
        }else if(daynum==3){
            day.textContent="수요일"
        }else if(daynum==4){
            day.textContent="목요일"
        }else if(daynum==5){
            day.textContent="금요일"
        }else if(daynum==6){
            day.textContent="토요일"
        }

        if(s<10){
            s=`0${s}`;
        }
        if(m<10){
            m=`0${m}`
        }
        if(h<10){
            h=`0${h}`;
        }

        if(h==0){
            h=`12`;
        }
        switch(month){
            case 2:
            case 3:
            case 4:
            mon = "봄";
            break;
            case 5:
            case 6:
            case 7:
            mon = "여름";
            break;
            case 8:
            case 9:
            case 10:
            mon = "가을";
            break;
            case 11:
            case 0:
            case 1:
            mon = "겨울";
            break;
        }
        if (daynum == 6) {
            document.getElementById('day').classList.add('saturday')
        } else if(daynum == 0) {
             document.getElementById('day').classList.add('sunday')
        }
        utc.textContent = `${mon}`;
        let time = `${h}:${m}:${s} ${session}`;
        h1.textContent = time;
        setTimeout(this.showTime,1000);
    }
// END CLOCK SCRIPT
  },
  mounted() {
    this.showTime(); 
  }
}
    
</script>
<style>
@font-face {
    font-family: 'BMEULJIRO';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/BMEULJIRO.woff')
        format('woff');
    font-weight: normal;
    font-style: normal;
}
.saturday {
    color: #0000ff; /* 토요일 */
}
.sunday {
    color: #ff0000; /* 일요일 */
}

#clock {
    height: 50px;
    text-align: center;
    vertical-align: center;
    padding: 13px 15px;
    #utc {
        margin-right: 15px;
    }
    #time {
        font-size: 60px;
        color: #1b9cfc;
        font-weight: 100;
        margin-bottom: 0;
    }
    #day {
        font-size: 30px;
        color: #e6e0e0;
        text-align: center;
        margin-top: 0;
        text-transform: uppercase;
    }
}
@media (max-width: 767px) {
    h1 {
        font-size: 30px !important;
    }
    h3 {
        font-size: 20px !important;
    }
}
</style>
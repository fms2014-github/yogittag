<template>
    <!-- <div onLoad="initClock()"> -->
    <div id="clock">
        <p>
            <span id="day">MON</span> &nbsp;
            <span id="utc">10 APRIL 2019</span>
        </p>
        <p id="time">10:15:40 AM</p>
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
        console.log(date);
        let h = date.getHours();
        let m = date.getMinutes();
        let s = date.getSeconds();
        let month = date.getMonth();
        let datenum = date.getDate();
        let fullYear= date.getFullYear();
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
        if(dayText==0){
            day.textContent="SUN";
        }else if(dayText == 1){
            day.textContent="MON";
        }else if(dayText==2){
            day.textContent="TUE";
        }else if(dayText==3){
            day.textContent="WEB"
        }else if(dayText==4){
            day.textContent="THUR"
        }else if(dayText==5){
            day.textContent="FRI"
        }else if(dayText==6){
            day.textContent="SAT"
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
            case 0:
            mon = "January";
            break;
            case 1:
            mon = "February";
            break;
            case 2:
            mon = "March";
            break;
            case 3:
            mon = "April";
            break;
            case 4:
            mon = "MAY";
            break;
            case 5:
            mon = "June";
            break;
            case 6:
            mon = "July";
            break;
            case 7:
            mon = "August";
            break;
            case 8:
            mon = "September";
            break;
            case 9:
            mon = "October";
            break;
            case 10:
            mon = "November";
            break;
            case 11:
            mon = "December";
            break;
        }
        utc.textContent = `${datenum} ${mon} ${fullYear}`;
        let time = `${h} : ${m} : ${s} ${session}`;
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
#clock {
    /* position: absolute; */
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
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
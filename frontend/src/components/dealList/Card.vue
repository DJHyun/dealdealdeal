<template>
  <v-list-item>
    <v-card class="mx-auto" width="80%" :href="this.link" target="_blank" tile>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="card-title">
            <!-- <div class="category">{{this.category}}</div> -->
            {{this.title}}
          </v-list-item-title>
          <div>
            <div class="date font-weight-light">{{this.dataFrom}} / {{this.time}}</div>
            <!-- <div class="price">
              {{this.itemPrice}} |
              <v-icon style="color:red; margin-right: 2px; font-size:18px;">mdi-truck</v-icon>{{this.expressPrice}}
            </div> -->
          </div>
        </v-list-item-content>
      </v-list-item>

      <v-img
        @mouseover="mouseOver"
        @mouseout="mouseOver"
        class="thumb"
        :src="images.default"
      />
      <div class="hover" :style="{right:imgPosX, top:imgPosY}">
        <img
          v-show="hoverActive"
          height="400px"
          :src="images.default"
        />
      </div>
    </v-card>
  </v-list-item>
</template>

<script>
export default {
  props: ["title", "link", "time"],
  data: () => ({
    hoverActive: false,
    imgPosX: "80px",
    imgPosY: 0,
    dataFrom: "",
    category: "",
    itemPrice:"",
    expressPrice:"",
    images: {
      default: require('@/assets/no_image.png')
    }
  }),
  methods: {
    mouseOver: function() {
      let e = window.event;
      if (e.pageX || e.pageY) {
        this.imgPosX = e.pageX;
        this.imgPosY = e.pageY;
      } else if (e.clientX || e.clientY) {
        this.imgPosX =
          e.clientX +
          document.body.scrollLeft +
          document.documentElement.scrollLeft;
        this.imgPosY =
          e.clientY +
          document.body.scrollTop +
          document.documentElement.scrollTop;
      }
      this.hoverActive = !this.hoverActive;
    }
  },
  mounted() {
    if (/(ppomppu)/g.test(this.link)) {
      this.dataFrom = "뽐뿌";
    } else if (/(clien)/g.test(this.link)) {
      this.dataFrom = "클리앙";
    } else if (/(ruliweb)/g.test(this.link)) {
      this.dataFrom = "루리웹";
    } else if (/(quasarzone)/g.test(this.link)) {
      this.dataFrom = "퀘이사존";
    } else if (/(coolenjoy)/g.test(this.link)) {
      this.dataFrom = "쿨엔조이";
    }

    // let regex = /^(\[|\()[^\]]*(\]|\))(\s*)/
    // let category = regex.exec(this.title)[0];
    
    // if (category) {
    //   this.title = this.title.replace(regex, "");
    //   if (/(G마켓|g마켓|지마켓|gmarket)/g.test(category)) {
    //     this.category = "지마켓";
    //   } else if (/(네이버|smartstore|스토어팜|스마트스토어)/g.test(category)) {
    //     this.category = "스토어팜";
    //   } else if (/(인터파크|interpark)/g.test(category)) {
    //     this.category = "인터파크";
    //   } else if (/(옥션|auction)/g.test(category)) {
    //     this.category = "옥션";
    //   } else if (/(amazon|아마존)/g.test(category)) {
    //     this.category = "아마존";
    //   } else if (/(ebay|이베이)/g.test(category)) {
    //     this.category = "이베이";
    //   } else if (/(티몬|Tmon|tmon)/g.test(category)) {
    //     this.category = "티몬";
    //   } else if (/(ssg|쓱|신세계)/g.test(category)) {
    //     this.category = "ssg";
    //   } else if (/(쿠팡)/g.test(category)) {
    //     this.category = "쿠팡";
    //   } else if (/(위메프)/g.test(category)) {
    //     this.category = "위메프";
    //   }
    // } else this.category = "기타";
    
    // regex = /(\[|\()[^\]]*(\]|\))/
    // let price = regex.exec(this.title)[0]
    // if (price) {
    //   price = price.slice(1,-1).split('/')
    //   this.itemPrice = price[0]
    //   this.expressPrice = price[1]
    // }
  }
};
</script>

<style scoped>
a:hover{
  text-decoration: none;
}
.card-title {
  white-space: normal;
  font-size: 12pt;
  padding-right: 80px;
}

.date {
  display: inline;
  margin-right: auto;
  font-size: 8pt;
}
.category {
  display: inline;
  background-color: darkgrey;
  color: white;
  border-radius: 5px;
  border: 1px solid;
  padding: 1px 2px;
  font-size: 10pt;
  margin-right: 3px;
}
.price {
  display: inline;
  position: absolute;
  right: 90px;
  font-size: 11pt;
  font-weight: 600;
  color: red;
}
.thumb {
  position: absolute;
  top: 0;
  right: 0;
  width: 80px;
  height: 100%;
  background-repeat: no-repeat;
  background-size: 80px auto;
  transition: transform 0.2s;
  z-index: 9;
}
.hover {
  position: absolute;
  z-index: 10;
}
</style>
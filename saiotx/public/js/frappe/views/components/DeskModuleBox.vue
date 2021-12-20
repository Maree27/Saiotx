<template>
 <div v-if="!hidden" :class="get_color">
    <div class="card-block">
        <div class="level">
          <a class="module-box-link" :href="type === 'module' ? '#modules/' + module_name : link">
            <h4 class="h4">
              
              <h2 class="m-b-20"><i :class="icon_class"></i></h2>
              <h6 class="text-left">{{ label }}</h6>
            </h4>
          </a>
        </div>
    </div>
  </div>
  
</template>

<script>
import Dropdown from "./Dropdown.vue";

export default {
  props: [
    "index",
    "name",
    "label",
    "category",
    "type",
    "module_name",
    "link",
    "count",
    "onboard_present",
    "links",
    "description",
    "hidden",
    "icon"
  ],
  components: {
    Dropdown
  },
  data() {
    return {
      hovered: 0
    };
  },
  
  computed: {
    icon_class() {
      if (this.icon) {
        return this.icon;
      } else {
        return "octicon octicon-file-text";
      }
  },
  get_color() {
    // let colors_list = ["green","blue","yellow","pink"];
    // var color = colors_list[Math.floor(Math.random() * colors_list.length)];

    return "card order-card"
  },
	dropdown_links() {
		return this.type === 'module' ? this.links
			.filter(link => !link.hidden)
			.concat([
				{ label: __('Customize'), action: () => this.$emit('customize'), class: 'border-top' }
			]) : [];
	}
  },
};
</script>

<style lang="less" scoped>
@import "frappe/public/less/variables";

.module-box {
  border-radius: 4px;
  padding: 5px 15px;
  display: block;
  background-color: #ffffff;
}

.module-box.sortable-chosen {
	background-color: @disabled-background;
	border-color: @disabled-background;
}

.modules-container:not(.dragging) .module-box:hover {
	border-color: @text-muted;
}

.hovered-box {
  background-color: @light-bg;
}

.octicon-chevron-down {
  font-size: 14px;
  padding: 4px 6px 2px 6px;
  border-radius: 4px;

  &:hover {
	background: @btn-bg;
  }
}

.octicon-chevron-down:hover {
  cursor: pointer;
}

.module-box-content {
  width: 100%;

  p {
    margin-top: 5px;
    font-size: 80%;
    display: flex;
    overflow: hidden;
  }
}

.module-box-link {
  flex: 1;
  padding-top: 5px;
  padding-bottom: 5px;
  text-decoration: none;
  --moz-text-decoration-line: none;
}

.icon-box {
  padding: 15px;
  width: 54px;
  display: flex;
  justify-content: center;
}

.icon {
  font-size: 24px;
}

.open-notification {
  top: -2px;
}

.shortcut-tag {
  margin-right: 5px;
}

.drag-handle {
  font-size: 12px;
}


.order-card {
    color: #fff;
}

.bg-c-blue {
    background: linear-gradient(45deg,#4099ff,#73b4ff);
}

.bg-c-green {
    background: linear-gradient(45deg,#2ed8b6,#59e0c5);
}

.bg-c-yellow {
    background: linear-gradient(45deg,#FFB64D,#ffcb80);
}

.bg-c-pink {
    background: linear-gradient(45deg,#FF5370,#ff869a);
}


.card {
    border-radius: 12px;
    -webkit-box-shadow: 0 1px 2.94px 0.06px rgba(4,26,55,0.16);
    box-shadow: 0 1px 2.94px 0.06px rgba(4,26,55,0.16);
    border: none;
    margin-bottom: 30px;
    -webkit-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
}

.card .card-block {
    padding: 25px;
}

.order-card i {
    font-size: 65px;
}

.order-card i.octicon-chevron-down{
    font-size: 35px;
}
.card.order-card:hover{
  cursor: pointer;
  background-color: #48C1C9;
} 
.card.order-card:hover .card-block .text-muted,.card.order-card:hover .card-block *{
  color: white!important;
}

.f-left {
    float: left;
}

.f-right {
    float: right;
}
.card-block *{
  color:#48C1C9;
  font-size: 18px;
  text-align: center;
}
.card-block .text-muted{
  color:#48C1C9!important;
}

ul.list-reset *{
  color:black;
}
.m-b-20{
  font-size:20px;
  margin:auto;
  width:fit-content;
  margin-bottom:25px;
}
.module-box-link h6{
  width: fit-content;
  margin: auto;
  color: black;
}
</style>

安装 vue-cli

```bash
npm install -g @vue/cli
```

# component-demo
## 饿了么开源Vue组件库
https://element.eleme.cn/#/zh-CN/component/date-picker

## 第三方图标库
[fontawesome.com](https://fontawesome.com/icons)
``` bash
npm install font-awesome
```

``` vue
<i class="fa-solid fa-house"></i>
```
# Axios
[Official Doc Link ](https://axios-http.com/zh/docs/intro)
``` bash
npm install axios
```

main.js

``` Vue
import axios from 'axios'; 
axios.defaults.baseURL = "http://localhost:8084";
Vue.prototype.$http=axiosd
```

Hello.vue
```

    created:function(){ 
    this.$http.get("queryUsers").then((res) => {
     this.tableData = res.data 
    })
    }
```

# VueRouter
```
npm install vue-router@3
```
Version 4 only for Vue3

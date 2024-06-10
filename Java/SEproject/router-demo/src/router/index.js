import VueRouter from 'vue-router';
import Vue from 'vue';

import Discover from '../components/Discover.vue'
import My from '../components/My.vue'
import Friend from '../components/Friend.vue'
import Toplist from '../components/Toplist.vue'
import Playlist from '../components/Playlist.vue'


Vue.config.productionTip = false

Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
        {path:'/',redirect:'/Discover'},
        {path:'/Discover',
            component:Discover,
            children:[
                {path:'Toplist',component:Toplist},
                {path:'Playlist',component:Playlist}
            ]
        
        },
        {path:'/My',component:My},
        {path:'/Friend',component:Friend}
    ]
})


export default router
const router = new VueRouter({
    routes: [
        { path: 'https://172.16.16.7:8086/team6/', component: httpVueLoader('./top.vue') },
        { path: 'https://172.16.16.7:8086/team6/review', component: httpVueLoader('./review.vue') },
    ]
})

const app = new Vue({
    el: "#app",
    router, 
}).$mount('#app');

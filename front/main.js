const router = new VueRouter({
    routes: [
        { path: '/', component: httpVueLoader('./top.vue') },
        { path: '/review', component: httpVueLoader('./review.vue') },
    ]
})

const app = new Vue({
    el: "#app",
    router
});

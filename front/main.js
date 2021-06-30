const Top = {
    template: '<h1>hello 2</h1>',
    data: function(){
        return {
            Menus: {}
        }
    },
    created: function(){
        GetMenuData()
    },
    methods: {
        GetMenuData: function(){
            const Url = "https://172.16.16.7:8086/api/get-menu"
            axios.get(Url)
            .then(res => {
                this.Menus = res.menu_detail
            })
            console.log(this.Menus)
        }
    }
}

const Review = {
    template: '<h1>hello 1</h1>',
    data: function(){
        return {
            Reviews: {},
            error: {
                require: false,
                tooLong: false,
                tooShort: false
            }
        }
    },
    created: function(){
        GetReviewData()
    },
    methods: {
        GetReviewData: function(){
            const Url = "https://172.16.16.7:8086/api/get-review"
            axios.get(Url)
            .then(res => {
                this.Reviews = res.reviews
            })
            console.log(this.Reviews)
        }
    }, 
    watch: {
        message: function(newVal, oldVal) {
            this.error.require = (newVal.length < 1) ? true : false;
            this.error.tooLong = (newVal.length > 255) ? true : false;
            this.error.tooShort = (newVal.length < 4) ? true : false;
        }
    }
}

const app = new Vue({
    el: "#app",
    components: {
        'top-component': Top,
        'Review-component': Review
    }
}).$mount('#app');

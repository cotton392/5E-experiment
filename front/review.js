Vue.component('review-component', {
    template:`<div>
    <select v-model="reviewed_menu_id">
    <option disabled value="">選択してください</option>
    <option v-for="menu in menus" v-bind:value="menu.name" v-bind:key="menu.id">
        {{ menu.name }}
    </option>
</select>
</div>`,
    data: function(){
        return {
            Reviews: {},
            menus: [
                {id: 1, name: "Aセット"},
                {id: 2, name: "Bセット"},
                {id: 3, name: "カレーライス"},
                {id: 4, name: "カツカレー"},
                {id: 5, name: "親子丼"},
                {id: 6, name: "カツ丼"},
                {id: 7, name: "カレーうどん"},
                {id: 8, name: "ラーメン"},
                {id: 9, name: "かけうどん"},
                {id: 10, name: "かけそば"},
                {id: 11, name: "チャーハン"},
                {id: 12, name: "ライス"},
            ],
            reviewed_menu_id: 0,
            review_detail: ''
        }
    },
    created: function(){
        this.GetReviewData()
    },
    methods: {
        GetReviewData: function(){
            const Url = "https://172.16.16.7:8086/api/get-review"
            axios.get(Url)
            .then(res => {
                this.Reviews = res.data.reviews
                console.log(this.Reviews[0])
            })
        },
        PostReviewData: function(){
            const Url = "https://172.16.16.7:8086/api/post-review"
            console.log(this.reviewed_menu_id)
            console.log(this.review_detail)
            axios.post(Url, {
                reviewed_menu_id: this.reviewed_menu_id,
                review_detail: this.review_detail
            })
            .then(res => {
                console.log(res.data)
            })
        }
    }, 
    watch: {
        message: function(newVal, oldVal) {
            this.error.require = (newVal.length < 1) ? true : false;
            this.error.tooLong = (newVal.length > 255) ? true : false;
            this.error.tooShort = (newVal.length < 4) ? true : false;
        }
    }
})
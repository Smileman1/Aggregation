const express = require('express')
const path = require('path')
const PORT = process.env.PORT || 5000
const mongoose = require('mongoose');
var bodyParser = require('body-parser');

var app = express();

app
    .use(express.static(path.join(__dirname, 'public')))
    .set('views', path.join(__dirname, 'views'))
    .set('view engine', 'ejs')
    .get('/', (req, res) => res.render('pages/index'))
    .listen(PORT, () => console.log(`Listening on ${ PORT }`))

//body-parser 등록
app.use(bodyParser.json()); app.use(bodyParser.urlencoded({extended : true}));

//DB연결
let url = "mongodb+srv://아이디자리:" + encodeURIComponent("비번자리")+"@주소자리/test"
mongoose.connect(url, {useNewUrlParser: true, useUnifiedTopology: true, dbName:'test'}, function(err){
    console.log('err::' + err)
});

//다이어리 데이터모델 설정
var Schema = mongoose.Schema;

//데이터 형태는 {date, title, imgLIst, content}

var dairySchema = new Schema(
    {date: String, title:String, imgList: String, content: String}
)

//위와 같은 모델로 쓰기위해 변수 생성
var datas = mongoose.model('dairy', dairySchema,'콜렉션이름');

//다이어리 데이터 모델에 기반하여 저장된 전체 데이터를 불러옴->항목별 보기
datas.find(function(error, dairy){
    if(error){
        console.log("error::"+error);
    } else{
        dairy.forEach(function(row){
            console.log("data::" + row.title);
        });
    }
})

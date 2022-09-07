const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });



var http = require('http');

function sleep(ms) {
  const wakeUpTime = Date.now() + ms;
  while (Date.now() < wakeUpTime) {}
}







client.on('ready', () => {
  client.user.setActivity('안녕하세여! 저는 공룡이에여!', { type: 'PLAYING' })
  console.log("디스코드 봇이 준비되었습니다");

  

  //data = ["시발", "개새끼", "이개새끼가 뒤질", "바보", "멍청이", "샤팔넘아", "애미"]
});

client.on('message', (message) => {
  if (!message.guild) return;
  if (message.author.bot) return;
  //TextChannel.sendTyping("하하")
  sleep(500);

  me = message.content




  var options = {
      host: 'dcs.r-e.kr',
      port: 80,
      method: 'POST',
      path: '/bots/' + encodeURIComponent(me) + '/' + message.guild.id,
      headers: {}
  };

  var resData = '';

  var req = http.request(options, function(res){
      res.on('data', function(chunk){
          resData += chunk;
      });
      
      res.on('end', function(){
          //console.log(resData + "-");
          //return resData;
          if (resData === "nots") {
            return;
          }
          console.log(me + "-" + resData)
          message.channel.send(resData)
      });
  });

  options.headers['Content-Type'] = 'application/x-www-form-urlencoded';
  req.data = "q=actor";
  options.headers['Content-Length'] = req.data.length;

  req.on('error', function(err){
      message.channel.send("처리 서버와 연결을 실패했습니다. (0) ⛌")
      //(당신의서버가 화이트리스트에 등록되있지 않습니다 등록:DCeocdoeddeids#5172)
      console.log('처리 오류 발생: ' + err.message);
  });

  req.write(req.data);
  req.end();


















  //message.channel.send(ai(me))
});


// 여러분의 디스코드 토큰으로 디스코드에 로그인합니다
client.login('token!');